from google.auth.transport.requests import Request # token renewal request
from google.oauth2.credentials import Credentials # convert token to object
from google_auth_oauthlib.flow import InstalledAppFlow # to start browser login flow
from googleapiclient.discovery import build # to control gmail API
import os # to work with files and folders

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly" , 
          "https://www.googleapis.com/auth/gmail.send" ,
          "https://www.googleapis.com/auth/gmail.modify"
         ] # ye batata hai hamari app gmail me kya kar sakti hai jaise ki yaha sirf read aur send

def get_gmail_service():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TOKEN_PATH = os.path.join(BASE_DIR, "token.json")

    creds = None
    # to load stored login permissions
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(
        TOKEN_PATH,
        SCOPES
    )
    if not creds or not creds.valid:
        
        # if token expired take new token....Browser open nahi hoga.Sab automatic.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        # agar token ho hi nahi
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Current file ka folder path nikalta hai.

            flow = InstalledAppFlow.from_client_secrets_file(
            os.path.join(BASE_DIR, "credentials.json"),
            SCOPES
        )

            creds = flow.run_local_server(port=0)
        
        # to save current login permission to token file
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    
    # to control gmail API
    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service