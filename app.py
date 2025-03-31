from fastapi import FastAPI, HTTPException, Form, File, UploadFile, Depends
import zipfile
from dotenv import load_dotenv
import requests
from io import BytesIO
import os

from Func_def import *

from GA1 import *

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
    # Handle file if provided
    if file:
        contents = await file.read()
    else:
        contents = None  # No file uploaded

    # Prepare payload for ChatGPT API
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
    # response = requests.post(post_url, headers=headers, json=payload)

    # Extract and return the response from the API
    # response_data = response.json()
    response_data = {
  "result": {
    "id": "chatcmpl-BH32dsc3kFprEFzu83YLnucsG3k3X",
    "object": "chat.completion",
    "created": 1743402967,
    "model": "gpt-4o-mini-2024-07-18",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": None,
          "tool_calls": [
            {
              "id": "call_Bg9UN65hSu7S4lq0rWzFhvvJ",
              "type": "function",
              "function": {
                "name": "GA1_1",
                "arguments": "{\"answer\":\"{\\\"args\\\":{\\\"email\\\":\\\"23f2004395@ds.study.iitm.ac.in\\\"},\\\"headers\\\":{\\\"Accept\\\":\\\"*/*\\\",\\\"Host\\\":\\\"httpbin.org\\\",\\\"User-Agent\\\":\\\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\\\"},\\\"origin\\\":\\\"<your_ip_address>\\\",\\\"url\\\":\\\"https://httpbin.org/get?email=23f2004395@ds.study.iitm.ac.in\\\"}\"}"
              }
            }
          ],
          "refusal": None,
          "annotations": []
        },
        "logprobs": None,
        "finish_reason": "tool_calls"
      }
    ],
    "usage": {
      "prompt_tokens": 1039,
      "completion_tokens": 137,
      "total_tokens": 1176,
      "prompt_tokens_details": {
        "cached_tokens": 0,
        "audio_tokens": 0
      },
      "completion_tokens_details": {
        "reasoning_tokens": 0,
        "audio_tokens": 0,
        "accepted_prediction_tokens": 0,
        "rejected_prediction_tokens": 0
      }
    },
    "service_tier": "default",
    "system_fingerprint": "fp_86d0290411",
    "monthlyCost": 0.00732,
    "cost": 0.003939,
    "monthlyRequests": 3,
    "costError": "crypto.createHash is not a function"
  }
}
    # final_resp = response_data["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
    final_resp = "GA1_2"
    if final_resp == "GA1_1":
        result = GA1_1()
    if final_resp == "GA1_2":
        result = GA1_2()
    if final_resp == "GA1_3":
        result = GA1_3()
    if final_resp == "GA1_4":
        result = GA1_4()
    if final_resp == "GA1_5":
        result = GA1_5()
    if final_resp == "GA1_6":
        result = GA1_6()
    if final_resp == "GA1_7":
        result = GA1_7()
    if final_resp == "GA1_8":
        result = GA1_8()
    if final_resp == "GA1_9":
        result = GA1_9()
    if final_resp == "GA1_10":
        result = GA1_10()
    if final_resp == "GA1_11":
        result = GA1_11()
    if final_resp == "GA1_12":
        result = GA1_12()
    if final_resp == "GA1_13":
        result = GA1_13()
    if final_resp == "GA1_14":
        result = GA1_14()
    if final_resp == "GA1_15":
        result = GA1_15()
    if final_resp == "GA1_16":
        result = GA1_16()
    if final_resp == "GA1_17":
        result = GA1_17()
    if final_resp == "GA1_18":
        result = GA1_18()

    return {
  "answer": str(result)
}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
