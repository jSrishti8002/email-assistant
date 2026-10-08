# to prevent processing of same email again. it marks email as read

from gmail_services import get_gmail_service

def mark_as_read(message_id):

    service = get_gmail_service()

    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "removeLabelIds": ["UNREAD"]
        }
    ).execute()