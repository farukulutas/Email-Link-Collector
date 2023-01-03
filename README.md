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

- You may need to enable access for less secure apps or create and use an app password for certain email servers (e.g. Gmail).
- You may need to allow your mail client to access your mailbox for certain email servers (e.g. Yandex).
