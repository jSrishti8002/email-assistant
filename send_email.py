from gmail_services import get_gmail_service # for authenticated connection with gmail account

import base64 # for encoding and decoding

from email.mime.text import MIMEText # for proper format of email (subject, body etc)

def create_message(to, subject, body): # raw text --> proper email object

    message = MIMEText(body)

    message["to"] = to

    message["subject"] = subject

    return message # returns complete email object

def encode_message(message):

    # email object --> bytes
    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    )

    return raw_message.decode()

def send_email(to, subject, body):

    service = get_gmail_service()

    # create email
    message = create_message(
        to,
        subject,
        body
    )
     # converting email to gmail api format
    encoded_message = encode_message(
        message
    )

    # sending email
    sent_message = service.users().messages().send(
    userId="me",
    body={
        "raw": encoded_message
        }
    ).execute()

    return sent_message