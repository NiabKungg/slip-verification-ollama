import argparse
import sys
import os
import base64
import requests
import json

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

def main():
    parser = argparse.ArgumentParser(description="Slip Verification Tool using Ollama")
    parser.add_argument("image_path", help="Path to the slip image file")
    parser.add_argument("--model", default="llama3.2-vision", help="Ollama vision model to use (default: llama3.2-vision)")
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: File '{args.image_path}' not found.")
        sys.exit(1)

    try:
        print(f"Extracting data using Ollama model '{args.model}'...")
        parsed_data, raw_response = extract_slip_data_with_ollama(args.image_path, args.model)
        
        print("\n--- Extracted Information ---")
        for key, value in parsed_data.items():
            print(f"{key.capitalize()}: {value}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
