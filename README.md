# AI Email Assistant

An AI-powered email assistant built using Python, Gemini, and Gmail API. The project combines AI capabilities with Gmail services to assist with email-related tasks and automate parts of the email workflow.

## Features

- AI-powered email assistance using Google Gemini
- Gmail API integration
- Send emails programmatically
- Perform Gmail-related actions
- AI-based email processing
- Workflow-based email assistance
- Secure handling of authentication credentials

## Technologies Used

- Python
- Google Gemini API
- Gmail API
- Google Authentication
- Git
- GitHub

## Project Structure

```text
email-assistant/
│
├── main.py
├── gemini_service.py
├── gmail_actions.py
├── gmail_services.py
├── send_email.py
├── requirements.txt
├── NOTES.md
├── workflow.md
└── .gitignore
```

## How It Works

The project uses Python to connect Gmail services with Google's Gemini AI.

The general workflow is:

```text
User
  ↓
Email Assistant
  ↓
Gemini AI
  ↓
Email Processing / Decision
  ↓
Gmail API
  ↓
Email Action
```
## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jSrishti8002/email-assistant.git
```
### 2. Open the Project
```bash
cd email-assistant
```
### 3. Install Dependencies 
```bash
pip install -r requirements.txt
```

## Configuration

The project requires authentication and API configuration to access Gmail and Gemini services.
For security reasons, sensitive files are not included in this repository.

The following files are intentionally excluded:
1. credentials.json
2. token.json
3. config.py
4. .env

You should configure your own credentials before running the project.

## Running the Project

After completing the required configuration:
```bash 
python main.py
```

## Security

API credentials, authentication tokens, and private configuration files are excluded using .gitignore.
Never upload:
- API keys
- OAuth credentials
- Authentication tokens
- Passwords
- Private configuration files

## Project Status

This project is actively maintained and may be extended with additional AI-powered email automation features.

## Future Improvements

- Improve natural language interaction
- Add more Gmail automation features
- Improve email classification and processing
- Add a graphical user interface
- Improve error handling and logging

## Author

Srishti Jaiswal
GitHub: [jSrishti8002](https://github.com/jSrishti8002)

