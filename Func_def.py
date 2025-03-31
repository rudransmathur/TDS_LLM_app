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
    "additionalProperties": False
}

# GA1 Function Definitions
GA1_functions = [
    {
        "name":"GA1_1",
        "description":"Install and run Visual Studio Code. In your Terminal (or Command Prompt)",
        "parameters": schema
    },
    {
        "name":"GA1_2",
        "description":"Send a HTTPS request to https://httpbin.org/get",
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
        "description":"Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes?Sum of data-value attributes:",
        "parameters": schema
    },
    {
        "name":"GA1_12",
        "description":"Download and process the files in  which contains three files with different encodings:data1.csv: CSV file encoded in CP-125data2.csv: CSV file encoded in UTF-data3.txt: Tab-separated file encoded in UTF-16Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches „ OR ™ OR › across all three files.What is the sum of all values associated with these symbols?",
        "parameters": schema
    },
    {
        "name":"GA1_13",
        "description":"Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called email.json with the value {'email': '23f2004395@ds.study.iitm.ac.in'} and push it.Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)",
        "parameters": schema
    },
    {
        "name":"GA1_14",
        "description":"Download  and unzip it into a new folder, then replace all 'IITM' (in upper, lower, or mixed case) with 'IIT Madras' in all files. Leave everything as-is - don't change the line endings.What does running cat * | sha256sum in that folder show in bash?",
        "parameters": schema
    },
    {
        "name":"GA1_15",
        "description":"Download  and extract it. Use ls with options to list all files in the folder along with their date and file size.What's the total size of all files at least 9525 bytes large and modified on or after Sat, 10 Sept, 1994, 4:32 am IST?",
        "parameters": schema
    },
    {
        "name":"GA1_16",
        "description":"Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?",
        "parameters": schema
    },
    {
        "name":"GA1_17",
        "description":"Download  and extract it. It has 2 nearly identical files, a.txt and b.txt, with the same number of lines.ow many lines are different between a.txt and b.txt?",
        "parameters": schema
    },
    {
        "name":"GA1_18",
        "description":"There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.",
        "parameters": schema
    },
]

GA2_functions = [{
        "name":"GA2_1",
        "description":"Write documentation in Markdown for an **imaginary** analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include:",
        "parameters": schema
    },{
        "name":"GA2_2",
        "description":"Download the image below and compress it losslessly to an image that is less than 1,500 bytes.By losslessly, we mean that every pixel in the new image should be identical to the original image.Upload your losslessly compressed image (less than 1,500 bytes)",
        "parameters": schema
    },{
        "name":"GA2_3",
        "description":"Publish a page using GitHub Pages that showcases your work. Ensure that your email address 23f2004395@ds.study.iitm.ac.in is in the page's HTML.GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:",
        "parameters": schema
    },{
        "name":"GA2_4",
        "description":"Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: 23f2004395@ds.study.iitm.ac.in.",
        "parameters": schema
    },{
        "name":"GA2_5",
        "description":"Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:",
        "parameters": schema
    },{
        "name":"GA2_6",
        "description":"Download this  which has the marks of 100 imaginary students.Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this:",
        "parameters": schema
    },{
        "name":"GA2_7",
        "description":"Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address 23f2004395@ds.study.iitm.ac.in. For example:",
        "parameters": schema
    },{
        "name":"GA2_8",
        "description":"Create and push an image to Docker Hub. Add a tag named 23f2004395 to the image.What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general",
        "parameters": schema
    },{
        "name":"GA2_9",
        "description":"Download . This file has 2-columns:studentId: A unique identifier for each student, e.g. 1, 2, 3, ..class: The class (including section) of the student, e.g. 1A, 1B, ... 12A, 12B, ... 12ZWrite a FastAPI server that serves this data. For example, /api should return all students data (in the same row and column order as the CSV file) as a JSON like this:",
        "parameters": schema
    },{
        "name":"GA2_10",
        "description":"Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6_K.llamafile model with it.Create a tunnel to the Llamafile server using ngrok.",
        "parameters": schema
    }]
GA3_functions = [
    {
        "name":"GA3_1",
        "description":"DataSentinel Inc. is a tech company specializing in building advanced natural language processing (NLP) solutions. Their latest project involves integrating an AI-powered sentiment analysis module into an internal monitoring dashboard. The goal is to automatically classify large volumes of unstructured feedback and text data from various sources as either GOOD, BAD, or NEUTRAL. As part of the quality assurance process, the development team needs to test the integration with a series of sample inputs—even ones that may not represent coherent text—to ensure that the system routes and processes the data correctly.Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:",
        "parameters": schema
    },
    {
        "name":"GA3_2",
        "description":"LexiSolve Inc. is a startup that delivers a conversational AI platform to enterprise clients. The system leverages OpenAI’s language models to power a variety of customer service, sentiment analysis, and data extraction features. Because pricing for these models is based on the number of tokens processed—and strict token limits apply—accurate token accounting is critical for managing costs and ensuring system stability.To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.One specific test case an understanding of text tokenization. Your task is to generate data for that test case.",
        "parameters": schema
    },
    {
        "name":"GA3_3",
        "description":"""
        RapidRoute Solutions is a logistics and delivery company that relies on accurate and standardized address data to optimize package routing. Recently, they encountered challenges with manually collecting and verifying new addresses for testing their planning software. To overcome this, the company decided to create an automated address generator using a language model, which would provide realistic, standardized U.S. addresses that could be directly integrated into their system.

The engineering team at RapidRoute is tasked with designing a service that uses OpenAI's GPT-4o-Mini model to generate fake but plausible address data. The addresses must follow a strict format, which is critical for downstream processes such as geocoding, routing, and verification against customer databases. For consistency and validation, the development team requires that the addresses be returned as structured JSON data with no additional properties that could confuse their parsers.
                      """,
        "parameters": schema
    },
    {
        "name":"GA3_4",
        "description":"Acme Global Solutions manages hundreds of invoices from vendors every month. To streamline their accounts payable process, the company is developing an automated document processing system. This system uses a computer vision model to extract useful text from scanned invoice images. Critical pieces of data such as vendor email addresses, invoice or transaction numbers, and other details are embedded within these documents.",
        "parameters": schema
    },
    {
        "name":"GA3_5",
        "description":"SecurePay, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:",
        "parameters": schema
    },
    {
        "name":"GA3_6",
        "description":"ShopSmart has written a Python program that has the 5 phrases and their embeddings as an array of floats. It looks like this:Your task is to write a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.Write your Python code here:",
        "parameters": schema
    },
    {
        "name":"GA3_7",
        "description":"InfoCore Solutions is a technology consulting firm that maintains an extensive internal knowledge base of technical documents, project reports, and case studies. Employees frequently search through these documents to answer client questions quickly or gain insights for ongoing projects. However, due to the sheer volume of documentation, traditional keyword-based search often returns too many irrelevant results.To address this issue, InfoCore's data science team decides to integrate a semantic search feature into their internal portal. This feature uses text embeddings to capture the contextual meaning of both the documents and the user's query. The documents are pre-embedded, and when an employee submits a search query, the system computes the similarity between the query's embedding and those of the documents. The API then returns a ranked list of document identifiers based on similarity.",
        "parameters": schema
    },
    {
        "name":"GA3_8",
        "description":"For example, the query 'What is the status of ticket 83742?' should return:Make sure you enable CORS to allow GET requests from any origin.What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/executeWe'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition.",
        "parameters": schema
    },
    {
        "name":"GA3_9",
        "description":"SecurePrompt Technologies is a cybersecurity firm that specializes in deploying large language models (LLMs) for sensitive enterprise applications. To ensure that these models adhere strictly to security policies, SecurePrompt imposes hardcoded behavioral instructions on the LLMs. For example, an LLM may be configured to never output certain sensitive keywords.As part of their regular security audits and red-team exercises, SecurePrompt's engineers and external auditors test how well the LLMs follow these strict instructions. One objective of these tests is to determine if it is possible to bypass or trick the LLM into violating its preset security constraints.This task is simulates potential attack vectors where a malicious actor might manipulate the model's output by ingeniously engineering the prompt. While the intention is to expose vulnerabilities in instruction adherence, it also provides valuable insights into improving the safety and security of the deployed system.",
        "parameters": schema
    }
]
GA4_functions = [
    {
        "name":"GA4_1",
        "description":"What is the total number of ducks across players on page number 8 of ESPN Cricinfo's ODI batting stats?",
        "parameters": schema
    },
    {
        "name":"GA4_2",
        "description":"Imagine you are a data analyst at StreamFlix, responsible for expanding the platform's movie library. Your task is to identify titles that have received favorable ratings on IMDb, ensuring that the selected titles meet the company's quality standards and resonate with subscribers.What is the JSON data?",
        "parameters": schema
    },
    {
        "name":"GA4_3",
        "description":"Write a web application that exposes an API with a single query parameter: ?country=. It should fetch the Wikipedia page of the country, extracts all headings (H1 to H6), and create a Markdown outline for the country. The outline should look like this:",
        "parameters": schema
    },
    {
        "name":"GA4_4",
        "description":"AgroTech Insights is a leading agricultural technology company that provides data-driven solutions to farmers and agribusinesses. By leveraging advanced analytics and real-time data, AgroTech helps optimize crop yields, manage resources efficiently, and mitigate risks associated with adverse weather conditions. Accurate and timely weather forecasts are crucial for making informed decisions in agricultural planning and management.Farmers and agribusinesses rely heavily on precise weather information to plan planting schedules, irrigation, harvesting, and protect crops from extreme weather events. However, accessing and processing weather data from multiple sources can be time-consuming and technically challenging. AgroTech Insights seeks to automate the extraction and transformation of weather data to provide seamless, actionable insights to its clients.",
        "parameters": schema
    },
    {
        "name":"GA4_5",
        "description":"UrbanRide is a leading transportation and logistics company operating in major metropolitan areas worldwide. To enhance their service efficiency, optimize route planning, and improve customer satisfaction, UrbanRide relies heavily on accurate geospatial data. Precise bounding box information of cities helps in defining service zones, managing fleet distribution, and analyzing regional demand patterns.As UrbanRide expands into new cities, the company faces the challenge of accurately delineating service areas within these urban environments. Defining the geographical boundaries of a city is crucial for:",
        "parameters": schema
    },
    {
        "name":"GA4_6",
        "description":"Search using the Hacker News RSS API for the latest Hacker News post mentioning Venture Capital and having a minimum of 32 points. What is the link that it points to?Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of pointsExtract and Present Data: Extract the most recent <item> from this result. Get the <link> tag inside it.Share the result: Type in just the URL in the answer.What is the link to the latest Hacker News post mentioning Venture Capital having at least 32 points?",
        "parameters": schema
    },
    {
        "name":"GA4_7",
        "description":"By automating this data retrieval and filtering process, CodeConnect gains several strategic advantages:Targeted Recruitment: Quickly identify new, promising talent in key regions, allowing for more focused and timely recruitment campaigns.Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly.Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building.Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research.nter the date (ISO 8601, e.g. '2024-01-01T00:00:00Z') when the newest user joined GitH",
        "parameters": schema
    },
    {
        "name":"GA4_8",
        "description":"DevSync Solutions is a mid-sized software development company specializing in collaborative tools for remote teams. With a growing client base and an expanding portfolio of projects, DevSync emphasizes efficient workflow management and robust version control practices to maintain high-quality software delivery.As part of their commitment to maintaining seamless and transparent development processes, DevSync has identified the need to implement automated daily updates to their GitHub repositories. These updates serve multiple purposes:",
        "parameters": schema
    },
    {
        "name":"GA4_9",
        "description":"This file,  contains a table of student marks in Maths, Physics, English, Economics, and Biology.Calculate the total Economics marks of students who scored 55 or more marks in Physics in groups 37-69 (including both groups).",
        "parameters": schema
    },
    {
        "name":"GA4_10",
        "description":"As part of the Documentation Transformation Project, you are a junior developer at EduDocs tasked with developing a streamlined workflow for converting PDF files to Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients.has the contents of a sample document.",
        "parameters": schema
    }
]
GA5_functions = [
    {
        "name":"GA5_1",
        "description":"RetailWise Inc. is a retail analytics firm that supports companies in optimizing their pricing, margins, and inventory decisions. Their reports depend on accurate historical sales data, but legacy data sources are often messy. Recently, RetailWise received an Excel sheet containing 1,000 transaction records that were generated from scanned receipts. Due to OCR inconsistencies and legacy formatting issues, the data in the Excel sheet is not clean.The Excel file has these columns, and they are messy:",
        "parameters": schema
    },
    {
        "name":"GA5_2",
        "description":"EduTrack Systems is a leading provider of educational management software that helps schools and universities maintain accurate and up-to-date student records. EduTrack's platform is used by administrators to monitor academic performance, manage enrollment, and generate reports for compliance and strategic planning.",
        "parameters": schema
    },
    {
        "name":"GA5_3",
        "description":"As a data analyst, you are tasked with determining how many successful GET requests for pages under hindi were made on Thursday between 14 and 18 during May 2024. This metric will help:Scale Resources: Ensure that servers can handle the peak load during these critical hoursContent Planning: Determine the popularity of regional content to decide on future content investments.Marketing Insights: Tailor promotional strategies for peak usage times.",
        "parameters": schema
    },
    {
        "name":"GA5_4",
        "description":"s-anand.net is a personal website that had region-specific music content. One of the site's key sections is telugump3, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.By analyzing the server’s Apache log file, the author can identify heavy users and take measures to manage bandwidth, improve site performance, or even investigate potential abuse.",
        "parameters": schema
    },
    {
        "name":"GA5_5",
        "description":"As a data analyst at GlobalRetail Insights, you are tasked with extracting meaningful insights from this dataset. Specifically, you need to:Group Mis-spelt City Names: Use phonetic clustering algorithms to group together entries that refer to the same city despite variations in spelling. For instance, cluster 'Tokyo' and 'Tokio' as one.Filter Sales Entries: Select all entries where:The product sold is Mouse.The number of units sold is at least 8.Aggregate Sales by City: After clustering city names, group the filtered sales entries by city and calculate the total units sold for each city.By performing this analysis, GlobalRetail Insights will be able to:",
        "parameters": schema
    },
    {
        "name":"GA5_6",
        "description":"ReceiptRevive Analytics is a data recovery and business intelligence firm specializing in processing legacy sales data from paper receipts. Many of the client companies have archives of receipts from past years, which have been digitized using OCR (Optical Character Recognition) techniques. However, due to the condition of some receipts (e.g., torn, faded, or partially damaged), the OCR process sometimes produces incomplete JSON data. These imperfections can lead to truncated fields or missing values, which complicates the process of data aggregation and analysis.One of ReceiptRevive’s major clients, RetailFlow Inc., operates numerous brick-and-mortar stores and has an extensive archive of old receipts. RetailFlow Inc. needs to recover total sales information from a subset of these digitized receipts to analyze historical sales performance. The provided JSON data contains 100 rows, with each row representing a sales entry. Each entry is expected to include four keys:",
        "parameters": schema
    },
    {
        "name":"GA5_7",
        "description":"DataSure Technologies is a leading provider of IT infrastructure and software solutions, known for its robust systems and proactive maintenance practices. As part of their service offerings, DataSure collects extensive logs from thousands of servers and applications worldwide. These logs, stored in JSON format, are rich with information about system performance, error events, and user interactions. However, the logs are complex and deeply nested, which can make it challenging to quickly identify recurring issues or anomalous behavior.Recently, DataSure's operations team observed an increase in system alerts and minor anomalies reported by their monitoring tools. To diagnose these issues more effectively, the team needs to perform a detailed analysis of the log files. One critical step is to count how often a specific key (e.g., 'errorCode', 'criticalFlag', or any other operational parameter represented by TBI) appears in the log entries.",
        "parameters": schema
    },
    {
        "name":"GA5_8",
        "description":"EngageMetrics is a digital marketing analytics firm that specializes in tracking and analyzing social media engagement. Their clients, ranging from major brands to local businesses, rely on data-driven insights to optimize content strategy, measure campaign performance, and identify posts that drive significant user interaction.",
        "parameters": schema
    },
    {
        "name":"GA5_9",
        "description":"Mystery Tales Publishing is an independent publisher specializing in mystery and suspense audiobooks. To broaden their audience and improve accessibility, they have been uploading narrated versions of their stories to YouTube. In addition to reaching visually impaired users, they want to leverage transcripts for content summarization, search indexing, and social media promotion.The company has identified that certain segments of their mystery story audiobooks generate the most engagement. However, transcribing entire videos can be time-consuming and may include irrelevant content. Therefore, they have decided to focus on transcribing only the most compelling segments. For instance, a particular segment—from 117 to 229.7—is known to captivate listeners with a twist in the plot. An accurate transcript of this segment will:",
        "parameters": schema
    },
    {
        "name":"GA5_10",
        "description":"PixelGuard Solutions is a digital forensics firm specializing in the recovery and analysis of visual evidence for law enforcement and corporate investigations. One of their recurring challenges involves reconstructing damaged or deliberately scrambled images to reveal hidden details critical to solving cases.",
        "parameters": schema
    },
]