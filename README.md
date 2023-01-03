# Email Link Collector

This tool allows you to connect to your email account, search through your emails for specific links, and write those links to a file. The tool utilizes the imaplib library to establish a secure connection to the email server and uses Regular Expression patterns to search through the emails.

## How to Use

1. Enter your email account information (email address and password) in the designated variables at the beginning of the code.
2. Specify the email server you are using (e.g. imap.gmail.com for Gmail).
3. Choose the folder that contains the emails you want to search (e.g. "inbox").
4. Modify the Regular Expression pattern to fit your specific link search needs.
5. Run the code and the collected links will be written to the result26.txt file.

## Customization

You can customize the tool to fit your specific link search needs by modifying the Regular Expression pattern in the code. You can also change the output file name and location.

## Note

- ProtonMail: You will need a premium account to use ProtonMail.
- ThunderBird: You can use ThunderBird as an alternative email client.
- Hotmail/Outlook: The IMAP4 server for Hotmail and Outlook is "outlook.office365.com".
- Gmail: The IMAP4 server for Gmail is "imap.gmail.com". You will need to create and use an app password.
- Yahoo: The IMAP4 server for Yahoo is "imap.mail.yahoo.com". You will need to create and use a third-party app password.
- Yandex: The IMAP4 server for Yandex is "imap.yandex.com.tr". You will need to allow your mail client to access your mailbox.
