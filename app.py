import uvicorn
from fastapi import FastAPI,HTTPException, Form, File, UploadFile
import zipfile
from dotenv import load_dotenv
from io import BytesIO
import os

from Func_def import *

app = FastAPI()
load_dotenv()

# API
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

# Chatgpt API Request
post_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_PROXY_TOKEN}",
}


@app.post("/api")
async def root(question : str = Form(...), file : UploadFile = File(None)):
    try:
        if file:  # Check if a file was uploaded
            contents = await file.read()
        else:
            contents = None  # No file uploaded
    except zipfile.BadZipFile:
        raise HTTPException(status_code=400, detail="Invalid ZIP file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "A question would be given to you"
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
                         "function": another_function
                     } for function in GA2_functions
                 ] + [
                     {
                         "type": "function",
                         "function": another_function
                     } for function in GA3_functions
                 ] + [
                     {
                         "type": "function",
                         "function": another_function
                     } for function in GA4_functions
                 ] + [
                     {
                         "type": "function",
                         "function": another_function
                     } for function in GA5_functions
                 ]
    }

    response = requests.post(post_url, headers=headers, json=payload)
    print(response.json()["choices"][0]["message"]["tool_calls"][0]["function"])
    fin_resp = response.json()["choices"][0]["message"]["tool_calls"][0]["function"]
    print(fin_resp)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
