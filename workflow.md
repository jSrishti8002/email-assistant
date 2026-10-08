# PROJECT - AI EMAIL ASSISTANT

**TECH STACK**

* Python
* Gmail API
* OAuth 2.0
* Gemini API
* Google API Client
* Regular Expressions (Regex)
* File Handling
* OS Module
* Datetime Module

**Complete Workflow**

START
│
├── Authenticate Gmail Account (OAuth 2.0)
│
├── Connect to Gmail API
│
├── Fetch Unread Emails
│   │
│   └── maxResults = 5
│
├── For Each Unread Email
│   │
│   ├── Extract Sender
│   │
│   ├── Extract Subject
│   │
│   ├── Extract Email Body
│   │
│   ├── Detect Attachments
│   │
│   └── Check Sensitive Keywords
│       │
│       ├── OTP
│       ├── Verification Code
│       ├── Password Reset
│       ├── Security Alert
│       ├── 2FA
│       └── Authentication Code
│
├── Sensitive Email?
│   │
│   ├── YES
│   │   │
│   │   ├── Log Action
│   │   ├── Mark Email Read
│   │   └── Skip Email
│   │
│   └── NO
│
├── Send Email Content to Gemini
│
├── Gemini Generates Response
│   │
│   ├── Gemini Failure?
│   │   │
│   │   ├── Log Failure
│   │   └── Leave Email Unread
│   │
│   └── Success
│
├── Gemini Returns "NO REPLY NEEDED"?
│   │
│   ├── YES
│   │   │
│   │   ├── Log Action
│   │   ├── Mark Email Read
│   │   └── Skip Email
│   │
│   └── NO
│
├── Extract Sender Email Address
│
├── Display AI Generated Reply
│
├── User Choice
│   │
│   ├── Option 1: Send Reply
│   │   │
│   │   ├── Send Email
│   │   ├── Log Action
│   │   └── Mark Email Read
│   │
│   ├── Option 2: Edit Draft
│   │   │
│   │   ├── Create draft.txt
│   │   ├── Open Notepad
│   │   ├── User Edits Reply
│   │   ├── Read Edited Draft
│   │   ├── Send Email
│   │   ├── Delete draft.txt
│   │   ├── Log Action
│   │   └── Mark Email Read
│   │
│   └── Option 3: Skip
│       │
│       ├── Log Action
│       └── Mark Email Read
│
├── Move to Next Unread Email
│
└── END

---

**FEATURES IMPLEMENTED**

✓ Gmail OAuth Authentication

✓ Gmail API Integration

✓ Read Unread Emails

✓ Multiple Email Processing

✓ Sender Extraction

✓ Subject Extraction

✓ Email Body Extraction

✓ Attachment Detection

✓ Sensitive Email Filtering

✓ OTP Protection

✓ Gemini AI Integration

✓ Automatic Reply Generation

✓ Manual Reply Review

✓ Draft Editing Through Notepad

✓ Email Sending

✓ Logging System

✓ Mark As Read System

✓ Error Handling

✓ Function-Based Architecture

✓ Temporary Draft File Handling

✓ Multi-Step Email Workflow



