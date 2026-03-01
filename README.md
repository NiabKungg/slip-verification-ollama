# SlipVerify with Ollama API 🧾🤖✨

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Ollama](https://img.shields.io/badge/Ollama-Vision%20AI-orange)

[**🇹🇭 อ่านภาษาไทย (#ภาษาไทย)**](#ภาษาไทย) | [**🇬🇧 Read in English (#english)**](#english)

---

<a id="english"></a>
## 🇬🇧 English

**SlipVerify with Ollama** is an advanced web application and API designed to extract and verify data from Thai bank transfer slips. By replacing traditional OCR and fragile regular expressions with **Ollama Vision AI (`llama3.2-vision`)**, this application intelligently understands the structure of bank slips to accurately extract complex data, regardless of minor formatting changes or image noise.

### Features
- **AI-Powered Extraction**: Utilizes local Large Multimodal Models (LMM) via Ollama instead of basic OCR.
- **Robust Data Parsing**: Automatically and intelligently extracts the Transfer Amount, Date & Time, Reference Number, and Sender Name and formats it directly into JSON.
- **No Regex Maintenance**: Eliminates the need to maintain complex, bank-specific regular expressions that break easily.
- **Modern UI**: A premium, responsive glassmorphism Dashboard for drag-and-drop slip image testing.
- **RESTful API**: Easily integrate into other applications via standard JSON API endpoints.

### Technologies Used
- **Backend**: Python, Flask, `requests`
- **AI Engine**: Ollama (Model: `llama3.2-vision`)
- **Frontend**: HTML5, CSS3 (Glassmorphism design), Vanilla JavaScript

### Prerequisites
1. **Python 3.8+**
2. **Ollama**: You must install Ollama on your system.
   - Download from [Ollama's official website](https://ollama.com/download).
   - After installation, open your terminal/command prompt and pull the vision model:
     ```bash
     ollama run llama3.2-vision
     ```
     *(This model is quite large. Please wait for the initial download and loading process to complete).*

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
   Make sure the Ollama application is running in the background (API is usually available at `http://localhost:11434`).

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the Dashboard:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

### API Usage
Endpoint: `POST /api/verify`

**Request:**
Send a `multipart/form-data` request with the image file under the `slip_image` key.

**Response (JSON):**
```json
{
  "success": true,
  "data": {
    "amount": "150.00",
    "date_time": "27 ก.พ. 67 14:30 น.",
    "reference_no": "01234567890ABCDEF",
    "sender": "นาย ทดสอบ ระบบ"
  }
}
```

---

<a id="ภาษาไทย"></a>
## 🇹🇭 ภาษาไทย

**SlipVerify with Ollama** เป็นเว็บแอปพลิเคชันและ API อัจฉริยะสำหรับการดึงข้อมูลสลิปโอนเงินธนาคารของไทย โปรเจกต์นี้ได้รับการอัปเกรดจากการใช้ OCR แบบเดิมและ Regex ที่เปราะบาง มาเป็นการใช้ **Ollama Vision AI (`llama3.2-vision`)** ซึ่งให้ AI ทำความเข้าใจโครงสร้างของสลิปโดยตรง ทำให้สามารถดึงข้อมูลได้แม่นยำและทนทานต่อการเปลี่ยนแปลงรูปแบบสลิปมากกว่าเดิม

### ฟีเจอร์หลัก
- **ดึงข้อมูลด้วย AI**: ใช้ Local AI Model ผ่าน Ollama แทนระบบอิงตัวอักษรแบบเก่า
- **เข้าใจโครงสร้างข้อมูล**: ดึงข้อมูลยอดเงิน, วันที่เวลา, เลขที่อ้างอิง และชื่อผู้โอน แล้วจัดโครงสร้างเป็น JSON ให้อัตโนมัติ
- **ไม่ต้องปวดหัวกับ Regex**: หมดปัญหาเรื่องการเขียนโค้ดดักจับข้อความแบบเจาะจงธนาคารที่มักจะพังเมื่อสลิปมีการเปลี่ยนดีไซน์นิดหน่อย
- **UI ทันสมัย**: หน้าแดชบอร์ดระดับพรีเมียม สวยงาม ใช้งานง่ายดายด้วยระบบลากแล้ววาง (Drag-and-Drop)
- **RESTful API**: พร้อมสำหรับการนำไปเชื่อมต่อกับแอปพลิเคชันอื่นผ่าน JSON API 

### เทคโนโลยีที่ใช้
- **Backend (ระบบหลังบ้าน)**: Python, Flask, `requests`
- **AI Engine (ปัญญาประดิษฐ์)**: Ollama (ใช้โค้ดโมเดล: `llama3.2-vision`)
- **Frontend (หน้าบ้าน)**: HTML5, CSS3 (การออกแบบสไตล์ Glassmorphism), Vanilla JavaScript

### สิ่งที่ต้องติดตั้งก่อนใช้งาน (Prerequisites)
1. **Python 3.8+**
2. **Ollama**: จำเป็นต้องติดตั้งโปรแกรม Ollama ในเครื่องของคุณ
   - ดาวน์โหลดและติดตั้งได้จาก [เว็บไซต์หลักของ Ollama](https://ollama.com/download)
   - หลังจากติดตั้งเสร็จ ให้เปิด Terminal/Command Prompt และรันคำสั่งเพื่อโหลดโมเดล:
     ```bash
     ollama run llama3.2-vision
     ```
     *(โมเดลมีขนาดใหญ่ การโหลดครั้งแรกอาจใช้เวลานาน)*

### วิธีการติดตั้งและรันโปรแกรม

1. **โคลนโปรเจกต์ (Clone Repo):**
   ```bash
   git clone https://github.com/NiabKungg/slip-verification-ollama.git
   cd slip-verification-ollama
   ```

2. **สร้าง Virtual Environment และติดตั้งไลบรารี:**
   ```bash
   python -m venv venv
   # เปิดใช้งาน venv:
   # สำหรับ Windows: .\venv\Scripts\activate
   # สำหรับ Mac/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **ตรวจสอบ Ollama:**
   ต้องมั่นใจว่าโปรแกรม Ollama ทำงานอยู่เบื้องหลัง (ปกติจะเรียกใช้หน้าต่าง API ได้ที่ `http://localhost:11434`)

4. **รันแอปพลิเคชัน Flask:**
   ```bash
   python app.py
   ```

5. **เข้าใช้งาน Dashboard:**
   เปิดเว็บเบราว์เซอร์ไปที่ `http://127.0.0.1:5000`

### การเรียกใช้งาน API
Endpoint: `POST /api/verify`

**Request:**
ส่ง Request แบบ `multipart/form-data` โดยแนบไฟล์รูปสลิปมากับ Key ที่ชื่อว่า `slip_image`

**Response (JSON):**
```json
{
  "success": true,
  "data": {
    "amount": "150.00",
    "date_time": "27 ก.พ. 67 14:30 น.",
    "reference_no": "01234567890ABCDEF",
    "sender": "นาย ทดสอบ ระบบ"
  }
}
```

---

*พัฒนาและต่อยอดโดยการผนวก LMM (Large Multimodal Model) เพื่อความแม่นยำในการวิเคราะห์สลิป 🚀*
