import imaplib
import email
import re

# Enter your email account information
EMAIL_ADDRESS = "your_mail@hotmail.com"
EMAIL_PASSWORD = "your_pass"

# Connect to the e-mail server
# You need premium for ProtonMail. Also, check out ThunderBird.
# hotmail & outlook imap4 => outlook.office365.com
# Enable access to less secure apps so you can use Gmail.
# You need to create and use app password.
# gmail imap4 => imap.gmail.com
# You must create and use a third-party app password to use Yahoo.
# yahoo imap4 => imap.mail.yahoo.com
# Allow mail client to access mailbox to use Yandex.
# yandex imap4 => imap.yandex.com.tr
mail = imaplib.IMAP4_SSL("outlook.office365.com")
mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Switch to the folder with all the mails
mail.select("inbox")

# Get all mails
result, data = mail.uid('search', None, "ALL")

# The list where we will collect the links
links = []

# For each mail
for uid in data[0].split():
    # Receive mail
    result, data = mail.uid('fetch', uid, '(RFC822)')
    raw_email = data[0][1]

    # Process the mail
    email_message = email.message_from_bytes(raw_email)

    # Find tracks with links
    for part in email_message.walk():
        # If the track is a link
        if part.get_content_type() == "text/html":
            # Get its content
            html = part.get_payload(decode=True)

            # Find links in content
            # (This example searches for links starting with "https://www.google.com/")
            for link in re.findall(r'https://www.google.com/\S+', html.decode('utf-8', errors='ignore')):
                # Delete any trailing quotes or double quotes.
                if link[-1] == "'" or link[-1] == '"':
                    link = link[:-1]

                # Add the link to the list
                links.append(link)

# close the connection
mail.logout()

# Write the links in the result26.txt file
with open("result26.txt", "w") as f:
    for link in links:
        f.write(link + "\n")
