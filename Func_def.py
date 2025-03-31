# Schema definitions
schema = {
    "schema": "http://json-schema.org/draft-07/schema#",
    "title": "AnswerSchema",
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "description": "The identifier for the classified answer"
        }
    },
    "required": ["answer"],
    "additionalProperties": "false"
}

# GA1 Function Definitions
GA1_functions = [
    {
        "name":"GA1_1",
        "description":"Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of code -s?",
        "parameters": schema
    },
    {
        "name":"GA1_2",
        "description":"Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2004395@ds.study.iitm.ac.in. What is the JSON output of the command?",
        "parameters": schema
    },
    {
        "name":"GA1_3",
        "description":"Download . In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum.What is the output of the command?",
        "parameters": schema
    },
    {
        "name":"GA1_4",
        "description":"Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 9, 9), 1, 10))What is the result?",
        "parameters": schema
    },
    {
        "name":"GA1_5",
        "description":"Let's make sure you can write formulas in Excel. Type this formula into Excel.Note: This will ONLY work in Office 365.=SUM(TAKE(SORTBY({14,4,2,4,14,3,4,15,5,5,11,6,1,3,9,0}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 12))What is the result?",
        "parameters": schema
    },
    {
        "name":"GA1_6",
        "description":"Just above this paragraph, there's a hidden input with a secret value.What is the value in the hidden input?",
        "parameters": schema
    },
    {
        "name":"GA1_7",
        "description":"How many Wednesdays are there in the date range 1981-10-24 to 2015-06-29?",
        "parameters": schema
    },
    {
        "name":"GA1_8",
        "description":"Download and unzip file which has a single extract.csv file inside.What is the value in the 'answer' column of the CSV file?",
        "parameters": schema
    },
    {
        "name":"GA1_9",
        "description":"Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines.",
        "parameters": schema
    },
    {
        "name":"GA1_10",
        "description":"Download  and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?",
        "parameters": schema
    },
    {
        "name":"GA1_11",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_12",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_13",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_14",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_15",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_16",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_17",
        "description":"",
        "parameters": schema
    },
    {
        "name":"GA1_18",
        "description":"",
        "parameters": schema
    },
]

GA2_functions = []
GA3_functions = []
GA4_functions = []
GA5_functions = []