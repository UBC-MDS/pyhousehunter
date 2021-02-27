import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def send_email(email_recipient,
               email_subject = 'Results from PyHouseHunter',
               attachment_location = ''):
    """A function to email search results.

    Parameters
    ----------
    email_recipient : str
        The email address for recipient of results.
    email_subject : str, optional
        Subject for email results, by default 'Results from PyHouseHunter'
    attachment_location : str, optional
        Path to the result file, by default ''

    Returns
    -------
    None 

    Examples
    -------
    >>> send_email("helloworld@gmail.com", "results.csv")
    """
    # Code adapted from Michael King's Tutorial.
    email_sender = 'pyhousehunter@gmail.com'
    email_message = 'Houses matching your specifications are attached.'
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))
    
    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('pyhousehunter@gmail.com', 'dsci524group6')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return
