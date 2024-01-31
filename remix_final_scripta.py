import imaplib
import email
import os
from datetime import datetime
from pyfiglet import Figlet

email_address = "remix.sarajevo@gmail.com"
password = "cuqi puem aslj mpik"



def generate_ascii_art(text, font="standard"):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(text)
    print(ascii_art)



def download_attachments_from_lapace(email_address, password, start_date, end_date):
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    # Connect to Gmail
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(email_address, password)
    print("Logged in successfully") 
    mail.select("inbox")
    download_folder = r"C:\Users\Amel\Desktop\Printanje"  # Replace with the desired folder path

    # Define the download folder
    download_folder = os.path.abspath(download_folder)  # Use absolute path
    print(f"Download folder: {download_folder}")

    # Search for emails within the specified date range and from specific senders
    start_date1 = datetime.strptime(start_date, "%d.%m.%Y")
    end_date1 = datetime.strptime(end_date, "%d.%m.%Y")
    start_date_str = start_date1.strftime("%d-%b-%Y")
    end_date_str = end_date1.strftime("%d-%b-%Y")

    search_criteria_izvodi = f'(FROM "izvodi.pravne@unicreditgroup.ba" SINCE {start_date_str} BEFORE {end_date_str})'
    search_criteria_info_rbbh = f'(FROM "info.rbbh@rbbh.ba" SINCE {start_date_str} BEFORE {end_date_str})'
    search_criteria_spar = f'(FROM "izvodi@sparkasse.ba" SINCE {start_date_str} BEFORE {end_date_str})'

    # Perform separate searches for each condition
    status_izvodi, messages_izvodi = mail.search(None, search_criteria_izvodi, "ALL")
    status_info_rbbh, messages_info_rbbh = mail.search(None, search_criteria_info_rbbh, "ALL")
    status_info_rbbh , messages_spar = mail.search(None, search_criteria_spar, "ALL")
    # Combine the results
    messages_combined = list(set(messages_izvodi[0].split() + messages_info_rbbh[0].split()+ messages_spar[0].split()))

    # Iterate through the combined results
    for msg_id in messages_combined:
        _, msg_data = mail.fetch(msg_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        # Iterate through the email's parts to find attachments
        for part in msg.walk():
            if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
                continue

            try:
                att_fn = part.get_filename()
                content_type = part.get_content_type()

                # Check if the attachment is a PDF
                if content_type == 'application/octet-stream' or content_type == 'application/pdf':
                    download_path = os.path.join(download_folder, att_fn)
                    print(f"Downloading PDF: {download_path}")

                    with open(download_path, "wb") as fp:
                        fp.write(part.get_payload(decode=True))
                else:
                    print(f"Skipping non-PDF attachment: {att_fn}")
            except Exception as e:
                print(f"Error downloading attachment: {str(e)}")

    generate_ascii_art("Kraj")
    # Logout and close the connection
    mail.logout()

print("Unesti Period npr. OD : 01.01.2023  DO : 01.02.2023 ") 
start_date = input("OD : ") 
end_date = input("DO : ") 


# Call the function to download PDF attachments from specific senders within the specified date range
download_attachments_from_lapace(email_address, password, start_date, end_date)
    


