# Automated Graded Assignment Solution System  
**IIT Madras Online Degree in Data Science - Tools in Data Science Course Project**

---
GitHub Repository: [github.com/rudransmathur/TDS_LLM_app](https://github.com/rudransmathur/TDS_LLM_app)  
API Endpoint: [https://tds-proj-2-seven.vercel.app/api](https://tds-proj-2-seven.vercel.app/api/)

## API Endpoint Usage

The API endpoint accepts **POST** requests at:

```
https://tds-proj-2-seven.vercel.app/api
```

- **Content-Type:** `multipart/form-data`
- **Required parameters:**
  - `question` (string): The assignment question to be answered.
  - `file` (file, optional): Any file (e.g., a ZIP or CSV) needed to answer the question.

### Example Request

```
curl -X POST "https://tds-proj-2-seven.vercel.app/api"
-H "Content-Type: multipart/form-data"
-F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?"
-F "file=@abcd.zip"
```

### Example Response

```
{
"answer": "1234567890"
}
```

> **Note:** Only `POST` requests with `multipart/form-data` are accepted.  
> The API will return a JSON object with an `answer` field containing the response.

---
## 1. Project Overview

This system automates solving graded assignments (GA1-GA5) through an LLM-powered API that processes questions and file attachments, returning answers in IITM's required format. The solution combines file handling, data processing, and large language models to replicate human problem-solving capabilities.

*This implementation meets all project requirements while adhering to IIT Madras' academic standards and technical specifications. The system demonstrates practical application of data engineering concepts taught in the Tools in Data Science course.*

---

## 2. System Architecture

- **FastAPI backend** with multipart/form-data support
- **File processing pipeline**
- **LLM integration layer**
- **Answer validation module**

---

## 3. API Implementation

```python
from fastapi import FastAPI, HTTPException, Form, File, UploadFile, Depends
app = FastAPI()

@app.post("/api")
async def root(
    question: str = Form(...),
    file: UploadFile | None = File(None)
):
    file_location = None
    extract_folder = None
```

---

## 4. Key Features

- **Multipart Request Handling**
  - Accepts both text questions and binary file uploads
  - Supports common formats: ZIP, CSV, JSON
  - Automatic file extraction and validation

- **Deployment Configuration**

```json
{
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "app.py" }]
}
```

---

## 5. Challenges Addressed
1. **File Handling Complexity**

- Utilized Python’s `zipfile` and `shutil` modules.
- If the uploaded file is a regular file (e.g., CSV), it is saved directly to the `uploads` folder.
- If the uploaded file is a ZIP archive, it is extracted and its contents are placed in the `uploads` folder.
- Ensured validation and security by using temporary directories and checking file types.

2. **LLM Integration**

- Used API Proxy tokens provided by IIT Madras for secure access.
- Sent questions to the LLM endpoint with a system prompt to ensure concise, relevant answers.
- Implemented error handling and caching for efficiency and reliability.

## 6. Repository Structure
```
├── app.py 
├── Func_def.py
├── GA1.py
├── GA2.py
├── pyproject.toml # Project metadata and dependencies
├── uv.lock # Locked dependency versions for reproducibility
├── uploads/ # Directory for storing uploaded and extracted files
├── requirements.txt 
├── vercel.json # Vercel deployment configuration
├── LICENSE
└── README.md
```


