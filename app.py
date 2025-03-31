from fastapi import FastAPI, HTTPException, Form, File, UploadFile, Depends
import zipfile
import shutil
from dotenv import load_dotenv
import requests
import os

from Func_def import *

from GA1 import *

UPLOAD_FOLDER = "uploads"
app = FastAPI()
load_dotenv()

# API
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

# ChatGPT API Request
post_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_PROXY_TOKEN}",
}


@app.post("/api")
async def root(
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Optional file
):
    file_location = None  # Define file_location before using it
    extract_folder = None  # Also define extract_folder for safety
    if file:
        # Normal File
        file_location = f"{UPLOAD_FOLDER}/{file.filename}"
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Zip Files
        if file.filename.endswith(".zip"):
            extract_folder = file_location.replace(".zip", "")
            with zipfile.ZipFile(file_location, "r") as zip_ref:
                zip_ref.extractall(extract_folder)


    # Prepare payload for ChatGPT API
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "A question would be given to you. Only return the function name of the function description it belongs to."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "tools": [
            {
                "type": "function",
                "function": function
            } for function in GA1_functions
        ] + [
            {
                "type": "function",
                "function": function
            } for function in GA2_functions
        ] + [
            {
                "type": "function",
                "function": function
            } for function in GA3_functions
        ] + [
            {
                "type": "function",
                "function": function
            } for function in GA4_functions
        ] + [
            {
                "type": "function",
                "function": function
            } for function in GA5_functions
        ]
    }

    # Send request to ChatGPT API
    response = requests.post(post_url, headers=headers, json=payload)

    # Extract and return the response from the API
    response_data = response.json()
    print(response_data)
    try:
        final_resp = response_data["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
    except KeyError:
        final_resp = response_data["choices"][0]["message"]["content"]
    # final_resp = "GA1_3"
    if "GA1_10" in final_resp:
        result = GA1_10()
    elif "GA1_11" in final_resp:
        result = GA1_11()
    elif "GA1_12" in final_resp:
        result = GA1_12()
    elif "GA1_13" in final_resp:
        result = GA1_13()
    elif "GA1_14" in final_resp:
        file_0 = os.path.join(extract_folder, "file0.txt")
        file_1 = os.path.join(extract_folder, "file1.txt")
        file_2 = os.path.join(extract_folder, "file2.txt")
        file_3 = os.path.join(extract_folder, "file3.txt")
        file_4 = os.path.join(extract_folder, "file4.txt")
        file_5 = os.path.join(extract_folder, "file5.txt")
        file_6 = os.path.join(extract_folder, "file6.txt")
        file_7 = os.path.join(extract_folder, "file7.txt")
        file_8 = os.path.join(extract_folder, "file8.txt")
        file_9 = os.path.join(extract_folder, "file9.txt")
        result = GA1_14(file_0, file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9)
    elif "GA1_15" in final_resp:
        result = GA1_15()
    elif "GA1_16" in final_resp:
        result = GA1_16()
    elif "GA1_17" in final_resp:
        result = GA1_17()
    elif "GA1_18" in final_resp:
        result = GA1_18()
    elif "GA1_1"in final_resp:
        result = GA1_1()
    elif "GA1_2"in final_resp:
        result = GA1_2()
    elif "GA1_3"in final_resp:
        result = GA1_3(file_location)
    elif "GA1_4"in final_resp:
        result = GA1_4()
    elif "GA1_5"in final_resp:
        result = GA1_5()
    elif "GA1_6"in final_resp:
        result = GA1_6()
    elif "GA1_7"in final_resp:
        result = GA1_7()
    elif "GA1_8"in final_resp:
        csv_path = os.path.join(extract_folder, "extract.csv")
        result = GA1_8(csv_path)
    elif "GA1_9"in final_resp:
        result = GA1_9()

    return {"answer": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
