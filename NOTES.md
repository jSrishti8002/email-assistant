# Day 1 - What We Did

- Gmail API enabled
- OAuth setup completed
- credentials.json downloaded
- token.json generated
- Successfully fetched emails

# Day 1 - Core Concepts

1. **Gmail API** → Gmail API ek official bridge hai jo Python program ko Gmail se communicate karne deta hai.
2. **Google Cloud Project** → Google Cloud Project app ko Google ke saamne identify karta hai taaki API access mil sake.
3. **OAuth** → OAuth password share kiye bina kisi app ko limited permission dene ka secure system hai.
4. **credentials.json** → credentials.json app ka identity card hai jisme Client ID aur Client Secret store hote hain.
5. **token.json** → token.json Google ki taraf se mila permission pass hai jo baar-baar login karne ki zaroorat khatam karta hai.

# Day 2 - What We Did

- Fetched email IDs using the Gmail API.
- Extracted the sender and subject of emails.
- Explored the email structure (payload, body, and parts).
- Located the actual email content.
- Decoded Base64 encoded email data.
- Extracted the readable email body.
- Added logic to handle different email formats safely.

# Day 2 - Core Concepts

1. **Payload** → The main container that holds an email's content and metadata.
2. **Parts** → Different sections of an email, such as plain text, HTML, and attachments.
3. **MIME (Multi purpose Internet Mail Extension)Type** → Identifies the type of content (e.g., text/plain, text/html, image/png).
4. **Base64 Encoding** → Converting data into a safe format for storage or transmission.
5. **Base64 Decoding** → Converting Base64 encoded data back to its original form.
6. **UTF-8** → A standard encoding used to convert bytes into readable text.

## Day 3 - What We Did

* Generated and configured a Gemini API key.
* Created a Gemini service file to interact with the AI model.
* Sent email content (`email_body`) to Gemini for processing.
* Generated AI-powered summaries of emails.
* Generated professional email reply drafts using AI.
* Improved prompts by providing additional context such as sender and subject.
* Learned how prompt engineering affects AI output quality.

## Day 3 - Core Concepts

* **API Key** = A unique key that allows an application to access an API service.
* **SDK (Software Development Kit)** = A collection of tools and libraries used to interact with a service.
# Day 3 - Core Concepts

- **Gemini Service** = A separate Python module that handles all communication with the Gemini API.
- **f-String Prompt Injection** = Using Python f-strings to dynamically insert email data into AI prompts.
- **Model Invocation** = Sending a prompt to Gemini using `client.models.generate_content()` and receiving a response.
- **Response Object** = The object returned by Gemini that contains the generated AI output.
- **Input Quality Principle** = Better email data and context lead to better AI-generated outputs.
- **AI Processing Flow** = Fetch Email → Extract Content → Build Prompt → Send to Gemini → Receive Response.

# Day 4 - What We Did

- Created a separate `send_email.py` module.
- Built a function to create properly formatted email messages using `MIMEText`.
- Encoded email messages using Base64 URL-safe encoding.
- Connected Gmail API with the email sending workflow.
- Added user confirmation before sending replies.
- Integrated reply sending into `main.py`.
- Extracted the sender's email address from the `From` header.
- Implemented automatic replying to the original sender instead of a hardcoded email address.
- Fixed Gmail OAuth permission and scope issues.
- Successfully sent email replies through Gmail API.
- Added logic to skip emails that do not require a reply.
- Implemented AI-based email classification using the "NO REPLY NEEDED" response pattern.

# Day 4 - Core Concepts

- **MIMEText** = Creates a properly structured email object containing headers and body content.
- **Message Encoding Pipeline** = Raw email content must be converted into bytes and encoded before transmission.
- **API Request Execution** = `.execute()` sends the prepared request to Google's servers and returns the response.
- **Email Header Parsing** = Extracts useful metadata such as sender and subject from email headers.
- **Regular Expressions (Regex)** = Used to locate and extract the sender's email address from a text string.
- **OAuth Scopes** = Define which Gmail actions the application is allowed to perform.

# Day 5 -  What We Did

- Process only unread emails using Gmail labels (`INBOX` + `UNREAD`).
- Added filtering for sensitive emails (OTP, verification codes, password resets, security alerts, etc.).
- Added error handling for Gemini API failures.
- Prevented sending fallback error messages as email replies.
- Automatically marked processed emails as read using Gmail API.
- Added handling for cases where no unread emails exist.

# Day 5 - Core Concepts

- **List Truthiness** = In Python, an empty list evaluates to False, allowing checks like:
if not messages:
- **Program Termination** = Using sys.exit() to stop script execution in a controlled and explicit manner.
- **Message State Management** = Tracking whether an email has been processed by modifying its labels (e.g., removing UNREAD).

# Day 6 - What We Did

- Refactored the codebase by moving repeated logic into reusable functions.
- Added manual draft editing using Notepad before sending emails.
- Added a logging system to track all important email actions.
- Improved read/unread handling for processed emails.
- Added support for processing multiple unread emails in one run.
- Added attachment detection for incoming emails.
- Cleaned up the overall project structure and workflow.

# Day 6 - Core Concepts

- **Refactoring** = Reorganizing code without changing its functionality.
- **Logging** = Recording important events for debugging and monitoring.
- **Email Processing Pipeline** = Reading → Analyzing → Replying → Logging → Marking Read.