# SlipVerify with Ollama API & QR Code Verification 🧾🤖✨

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Ollama](https://img.shields.io/badge/Ollama-Vision%20AI-orange)
![pyzbar](https://img.shields.io/badge/pyzbar-QR%20Scanner-brightgreen)

[**🇹🇭 อ่านภาษาไทย (#ภาษาไทย)**](#ภาษาไทย) | [**🇬🇧 Read in English (#english)**](#english)

---

<a id="english"></a>
## 🇬🇧 English

**SlipVerify with Ollama** is an advanced web application and API designed to extract and verify data from Thai bank transfer slips. It combines the power of **Ollama Vision AI (`llama3.2-vision`)** for intelligent data extraction and **QR Code verification** to cross-check transaction authenticity, ensuring robust and accurate slip validation.

### Features
- **QR Code Verification**: Scans the embedded QR code on the slip and cross-checks the reference number against the one extracted via AI.
- **AI-Powered Extraction**: Utilizes local Large Multimodal Models (LMM) via Ollama instead of fragile basic OCR regex rules.
- **Robust Data Parsing**: Automatically and intelligently extracts the Transfer Amount, Date & Time, Reference Number, and Sender Name in JSON format.
- **Fake Slip Detection**: Flags slips as potentially fake if the QR code is missing or if the reference numbers do not match.
- **Modern UI**: A premium, responsive glassmorphism Dashboard for drag-and-drop slip image testing.
- **RESTful API**: Easily integrate into other applications via standard JSON API endpoints.

### Technologies Used
- **Backend**: Python, Flask, `requests`, `pyzbar`, `Pillow`
- **AI Engine**: Ollama (Model: `llama3.2-vision`)
- **Frontend**: HTML5, CSS3 (Glassmorphism design), Vanilla JavaScript

### Prerequisites
1. **Python 3.8+**
2. **Ollama**: You must install Ollama on your system.
   - Download from [Ollama's official website](https://ollama.com/download).
   - After installation, run the following command to pull the vision model:
     ```bash
     ollama run llama3.2-vision
     ```
3. **Visual C++ Redistributable (Windows)** or **zbar (Mac/Linux)**: Required for the `pyzbar` library to read QR codes.
   - **Mac**: `brew install zbar`
   - **Linux**: `sudo apt-get install libzbar0`

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NiabKungg/slip-verification-ollama.git
   cd slip-verification-ollama
   ```

2. **Set up Virtual Environment and Install dependencies:**
   ```bash
   python -m venv venv
   # Activate venv:
   # On Windows: .\venv\Scripts\activate
   # On Mac/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Ensure Ollama is running:**
   Make sure the Ollama application is running in the background (`http://localhost:11434`).

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the Dashboard:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

### CLI Usage
You can also verify a slip directly from the command line:
```bash
python verify_slip.py <path_to_image> --model llama3.2-vision
```

### API Usage
Endpoint: `POST /api/verify`

**Request:**
Send a `multipart/form-data` request with the image file under the `slip_image` key.

**Response (JSON):**
```json
{
  "status": "success",
  "verification": {
    "is_authentic": true,
    "qr_payload": "00460006000001010301402... (truncated)",
    "reason": "Reference Number matches QR Code payload."
  },
  "data": {
    "amount": "150.00",
    "date_time": "27 ก.พ. 67 14:30 น.",
    "reference_no": "01234567890ABCDEF",
    "sender": "นาย ทดสอบ ระบบ"
  },
  "raw_text": "..."
}
```

---

<a id="ภาษาไทย"></a>
## 🇹🇭 ภาษาไทย

**SlipVerify with Ollama** เป็นเว็บแอปพลิเคชันและ API อัจฉริยะสำหรับการตรวจสอบและดึงข้อมูลสลิปโอนเงินธนาคารของไทย โดยผสานเทคโนโลยี **Ollama Vision AI (`llama3.2-vision`)** ในการอ่านข้อมูล และระบบ **ตรวจสอบ QR Code** เพื่อป้องกันสลิปปลอมหรือสลิปตัดต่อ ทำให้ระบบมีความแม่นยำสูงกว่าการใช้ OCR แบบเดิม

### ฟีเจอร์หลัก
- **ตรวจสอบสลิปปลอมจาก QR Code**: สแกน QR Code บนสลิปเพื่อนำข้อมูล Payload มาเทียบกับ "เลขที่อ้างอิง" ที่ AI อ่านได้ หากไม่ตรงกันระบบจะแจ้งเตือนทันที
- **ดึงข้อมูลด้วย AI**: ใช้ Local AI Model ผ่าน Ollama แทนการเขียน Regex แบบเก่าที่มักจะพังเมื่อสลิปอัปเดตใหม่
- **เข้าใจโครงสร้างข้อมูล**: ดึงข้อมูลยอดเงิน, วันที่เวลา, เลขที่อ้างอิง และชื่อผู้โอน แล้วจัดโครงสร้างเป็น JSON ให้อัตโนมัติ
- **UI ทันสมัย**: หน้าแดชบอร์ดล้ำสมัยแบบ Glassmorphism รองรับการลากแล้ววาง (Drag-and-Drop) รูปภาพเพื่อทดสอบ
- **RESTful API**: พร้อมสำหรับการนำไปเชื่อมต่อกับโปรแกรมหรือแอปพลิเคชันอื่นๆ

### เทคโนโลยีที่ใช้
- **Backend (ระบบหลังบ้าน)**: Python, Flask, `requests`, `pyzbar`, `Pillow`
- **AI Engine (ปัญญาประดิษฐ์)**: Ollama (ใช้โค้ดโมเดล: `llama3.2-vision`)
- **Frontend (หน้าบ้าน)**: HTML5, CSS3, Vanilla JavaScript

### สิ่งที่ต้องเตรียมก่อนใช้งาน (Prerequisites)
1. **Python 3.8+**
2. **Ollama**: จำเป็นต้องติดตั้งในเครื่อง
   - ดาวน์โหลดจาก [เว็บไซต์หลักของ Ollama](https://ollama.com/download)
   - หลังจากติดตั้งเสร็จ ให้โหลดโมเดล:
     ```bash
     ollama run llama3.2-vision
     ```
3. **โปรแกรมเสริมสำหรับอ่าน QR Code**:
   - **Windows**: โดยปกติ `pyzbar` จะใช้งานได้เลย (แต่ถ้ามีปัญหาอาจต้องลง Visual C++ Redistributable)
   - **Mac**: รันคำสั่ง `brew install zbar`
   - **Linux**: รันคำสั่ง `sudo apt-get install libzbar0`

### วิธีการติดตั้งและรันโปรแกรม

1. **โคลนโปรเจกต์ (Clone Repo):**
   ```bash
   git clone https://github.com/NiabKungg/slip-verification-ollama.git
   cd slip-verification-ollama
   ```

2. **สร้าง Virtual Environment และติดตั้งไลบรารี:**
   ```bash
   python -m venv venv
   # สำหรับ Windows: .\venv\Scripts\activate
   # สำหรับ Mac/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **ตรวจสอบ Ollama:**
   มั่นใจว่าโปรแกรม Ollama ทำงานอยู่เบื้องหลัง (`http://localhost:11434`)

4. **รันแอปพลิเคชัน Flask:**
   ```bash
   python app.py
   ```

5. **เข้าใช้งาน Dashboard:**
   เปิดเว็บเบราว์เซอร์ไปที่ `http://127.0.0.1:5000`

### การเรียกใช้งานผ่าน Command Line (CLI)
คุณสามารถตรวจสอบรูปภาพสลิปโดยตรงผ่านคำสั่ง:
```bash
python verify_slip.py <path_to_image> --model llama3.2-vision
```

### การเรียกใช้งาน API
Endpoint: `POST /api/verify`

**Request:**
ส่ง Request แบบ `multipart/form-data` โดยแนบไฟล์รูปสลิปมากับ Key ที่ชื่อว่า `slip_image`

**Response (JSON):**
```json
{
  "status": "success",
  "verification": {
    "is_authentic": true,
    "qr_payload": "00460006000001010301402... (truncated)",
    "reason": "Reference Number matches QR Code payload."
  },
  "data": {
    "amount": "150.00",
    "date_time": "27 ก.พ. 67 14:30 น.",
    "reference_no": "01234567890ABCDEF",
    "sender": "นาย ทดสอบ ระบบ"
  },
  "raw_text": "..."
}
```

---

*พัฒนาและต่อยอดเพื่อสร้างระบบจัดการสลิปโอนเงินที่น่าเชื่อถือและปลอดภัยที่สุด 🚀*
