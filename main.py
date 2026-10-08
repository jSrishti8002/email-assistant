
from gmail_services import get_gmail_service
import base64
from gemini_service import ask_gemini
from send_email import send_email
import re # importing regex
from gmail_actions import mark_as_read
import sys
import os
from datetime import datetime

def extract_sender_and_subject(headers):

    subject = "No Subject"
    sender = "Unknown Sender"

    for header in headers:

        if header["name"] == "Subject":
            subject = header["value"]

        if header["name"] == "From":
            sender = header["value"]

    return sender, subject

def extract_email_body(payload):

    email_body = "No Body Found"

    # Case 1: Data directly in body

    if "body" in payload and "data" in payload["body"]:

        encoded_data = payload["body"]["data"]

        decoded_data = base64.urlsafe_b64decode(
            encoded_data
        )

        email_body = decoded_data.decode("utf-8")

    # Case 2: Data inside parts

    elif "parts" in payload:

        for part in payload["parts"]:

            if part["mimeType"] == "text/plain":

                encoded_data = part["body"]["data"]

                decoded_data = base64.urlsafe_b64decode(
                    encoded_data
                )

                email_body = decoded_data.decode("utf-8")

                break

    return email_body

def extract_email_address(sender):

    email_match = re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        sender
    )

    if email_match:
        return email_match.group(0)

    return None

def is_sensitive_email(subject, email_body):

    subject_lower = subject.lower()
    body_lower = email_body.lower()

    sensitive_keywords = [
        "otp",
        "verification code",
        "one time password",
        "password reset",
        "security alert",
        "two factor authentication",
        "2fa",
        "authentication code"
    ]

    for keyword in sensitive_keywords:

        if keyword in subject_lower or keyword in body_lower:

            print(
                f"\nSkipping sensitive email "
                f"(Detected: {keyword})"
            )

            return True

    return False

def generate_email_reply(
    sender,
    subject,
    email_body
):

    reply = ask_gemini(
        f"""
        You are a professional email assistant.

        Read the email carefully.

        Rules:

        1. If the email is a newsletter, advertisement,
        promotional message, OTP, security alert,
        automated notification, or informational update,
        respond with exactly:

        NO REPLY NEEDED

        2. If the email requires a response,
        write a professional and concise reply.

        3. Do not explain your reasoning.

        4. Return only the reply email text.

        Sender:
        {sender}
        Subject:
        {subject}
        Email:
        {email_body}
        """
    )
    
    # reply = "Thank you for your email. We have received your application and will review it shortly."
    return reply

def log_action(
    sender,
    subject,
    action
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = (
        f"\n[{timestamp}]\n"
        f"Sender: {sender}\n"
        f"Subject: {subject}\n"
        f"Action: {action}\n"
        f"{'-'*40}\n"
    )

    with open(
        "mega_project2_emailAssistant/logs/email_logs.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(log_entry)

def handle_reply_options(
    reply,
    recipient_email,
    subject,
    message_id
):

    print("\nChoose an option:")
    print("1. Send Reply")
    print("2. Edit Draft")
    print("3. Skip")

    choice = input("\nEnter choice: ")

    if choice == "1":

        send_email(
            to=recipient_email,
            subject=f"Re: {subject}",
            body=reply
        )
        mark_as_read(message_id)
        
        log_action(
        recipient_email,
        subject,
        "Reply Sent"
    )
        print("Email Sent Successfully!")

    elif choice == "2":

        with open(
            "draft.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(reply)

        print("\nOpening draft in Notepad...")

        os.system("notepad draft.txt")

        with open(
            "draft.txt",
            "r",
            encoding="utf-8"
        ) as file:

            edited_reply = file.read()

        send_email(
            to=recipient_email,
            subject=f"Re: {subject}",
            body=edited_reply
        )
        
        os.remove("draft.txt") # auto deletes drafts
        mark_as_read(message_id) # marks read to emails that have been replied to
        log_action(
        recipient_email,
        subject,
        "Edited Reply Sent"
    )
        print(
            "Edited Email Sent Successfully!"
        )

    else:

        mark_as_read(message_id)

        log_action(
            recipient_email,
            subject,
            "Skipped By User"
        )

        print("Email Skipped.")

# to fetch the all avaialable email ids
service = get_gmail_service()

results = service.users().messages().list(
    userId="me",
    labelIds=["INBOX", "UNREAD"],
    maxResults=5
).execute()

messages = results.get("messages", [])

if not messages:
    sys.exit("No unread emails found.")

for msg in messages:
    email = service.users().messages().get(
        userId="me",
        id=msg["id"]
    ).execute()
    
    # sirf subject aur sender dekhne k liye
    headers = email["payload"]["headers"]
    
    # to extract sender and subject
    sender, subject = extract_sender_and_subject(headers)    
    print("\n------------------")
    print("From:", sender)
    print("Subject:", subject)

    # Email ke payload ka structure dekhne ke liye
    payload = email["payload"]

    # Check for attachments

    if "parts" in payload:

        for part in payload["parts"]:

            if part.get("filename"):

                print(
                    f"\nAttachment found: "
                    f"{part['filename']}"
                )
    email_body = extract_email_body(payload)
    
    # to prevent seding sensitive emails to gemini
    if is_sensitive_email(subject, email_body):

        print("Sensitive email detected")
        log_action(
        sender,
        subject,
        "Sensitive Email Skipped"
    )

        mark_as_read(msg["id"])
        continue
    print("\nEMAIL BODY:\n")
    print(email_body)
    
    # to generate reply for email
    reply = generate_email_reply(
    sender,
    subject,
    email_body
)   
    print("\nEMAIL REPLY:\n")
    print(reply)
    
    if reply == "AI response could not be generated.":
        log_action(
        sender,
        subject,
        "Gemini Failed"
    )
        print("\nSkipping email because Gemini failed.")
        continue

    if "NO REPLY NEEDED" in reply.upper():
        log_action(
        sender,
        subject,
        "No Reply Needed"
    )
        
        mark_as_read(msg["id"])
        print("\nSkipping reply: Gemini marked this email as informational.")
        continue

    recipient_email = extract_email_address(sender)   
    if not recipient_email:
        print("Could not extract a valid reply email address.")
        break  # Stops the loop if no valid email is found
    
    # to send , modify or skip replies 
    handle_reply_options(
    reply,
    recipient_email,
    subject,
    msg["id"]
)