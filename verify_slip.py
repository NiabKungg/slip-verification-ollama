import argparse
import sys
import os
import base64
import requests
import json
import re
from PIL import Image
from pyzbar.pyzbar import decode

def extract_qr_payload(image_path):
    """
    Extract payload from the QR code in the image.
    """
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        return None
    except Exception as e:
        print(f"Error reading QR code: {e}")
        return None

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_slip_data_with_ollama(image_path, model="llama3.2-vision"):
    """
    Extract text and structured data from the slip image using Ollama Vision models.
    """
    base64_image = encode_image_to_base64(image_path)
    
    prompt = """
You are an advanced OCR and data extraction AI. Extract the following information from the provided Thai bank transfer slip image.
Respond ONLY with a valid JSON block, no markdown formatting, no explanations, no extra text.

Required fields in JSON:
{
  "amount": "The exact transfer amount as a string (e.g. '500.00')",
  "date_time": "The date and time of the transaction as a string (e.g. '28 ก.พ. 2567 14:30')",
  "reference_no": "The reference or transaction number as a string (e.g. '013233140512ABC')",
  "sender": "The name of the sender as a string. If it has a title (like นาย, นาง, นางสาว, MR., MS.), include it."
}

If you cannot find a specific field, return null for that field. Do not include any text before or after the JSON block.
"""

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [base64_image],
        "stream": False,
        "format": "json"
    }

    try:
        response = requests.post(url, json=payload, timeout=180)
        response.raise_for_status()
        result = response.json()
        
        response_text = result.get("response", "").strip()
        
        # Clean up possible markdown wrappers if the model ignores the instruction
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        parsed_data = json.loads(response_text.strip())
        return parsed_data, response_text
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to connect to Ollama API. Make sure Ollama is running at localhost:11434. Error: {str(e)}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON from Ollama response. Raw response: {response_text}. Error: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

def verify_slip_image(image_path, model="llama3.2-vision"):
    """
    Full verification flow: read QR code, read text with Ollama, cross-check reference numbers.
    """
    qr_payload = extract_qr_payload(image_path)
    
    # Even if QR code is not found, we might still want the data from Ollama,
    # but the slip is likely fake or incomplete. Let's still extract using Ollama for logging/info.
    try:
        parsed_data, raw_text = extract_slip_data_with_ollama(image_path, model)
    except Exception as e:
        if not qr_payload:
            return {
                "is_authentic": False,
                "reason": f"No QR Code found, and Ollama extraction failed: {str(e)}",
                "qr_payload": None,
                "data": None
            }, ""
        raise e
        
    if not qr_payload:
        return {
            "is_authentic": False,
            "reason": "QR Code not found or unreadable. Suspected fake or incomplete slip.",
            "qr_payload": None,
            "data": parsed_data
        }, raw_text

    reference_no = parsed_data.get("reference_no")
    if not reference_no:
        return {
            "is_authentic": False,
            "reason": "Reference Number not found by OCR. Cannot cross-check.",
            "qr_payload": qr_payload,
            "data": parsed_data
        }, raw_text
        
    # Clean up strings for comparison
    clean_ref = re.sub(r'[^a-zA-Z0-9]', '', str(reference_no)).lower()
    clean_qr = re.sub(r'[^a-zA-Z0-9]', '', str(qr_payload)).lower()
    
    # Normalize visually similar characters to handle OCR inaccuracies
    # 'l' (lowercase L) and 'i' (lowercase I) become '1'
    # 'o' (lowercase O) becomes '0'
    clean_ref = clean_ref.replace('l', '1').replace('i', '1').replace('o', '0')
    clean_qr = clean_qr.replace('l', '1').replace('i', '1').replace('o', '0')
    
    # The reference number from OCR should be entirely contained within the QR payload
    if clean_ref and clean_ref in clean_qr:
        is_authentic = True
        reason = "Reference Number matches QR Code payload."
    else:
        is_authentic = False
        reason = "Reference Number does NOT match QR Code payload. Suspected fake slip."
        
    return {
        "is_authentic": is_authentic,
        "reason": reason,
        "qr_payload": qr_payload,
        "data": parsed_data
    }, raw_text

def main():
    parser = argparse.ArgumentParser(description="Slip Verification Tool using Ollama")
    parser.add_argument("image_path", help="Path to the slip image file")
    parser.add_argument("--model", default="llama3.2-vision", help="Ollama vision model to use (default: llama3.2-vision)")
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: File '{args.image_path}' not found.")
        sys.exit(1)

    try:
        print(f"Verifying slip using QR Code cross-check and Ollama model '{args.model}'...")
        verification_result, raw_response = verify_slip_image(args.image_path, args.model)
        
        print("\n--- Verification Result ---")
        print(f"Authentic: {verification_result['is_authentic']}")
        print(f"Reason:    {verification_result['reason']}")
        print(f"QR Payload:{verification_result['qr_payload']}")
        
        print("\n--- Extracted Information ---")
        if verification_result['data']:
            for key, value in verification_result['data'].items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("No data extracted.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
