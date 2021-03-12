import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import regex as re
import io


def send_email(
    email_recipient, filtered_data, email_subject="Results from PyHouseHunter"
):
    """A function to email search filtered search results.

    Parameters
    ----------
    email_recipient : str
        The email address for recipient of results.
    email_subject : str, optional
        Subject for email results, by default 'Results from PyHouseHunter'
    filtered_data : pandas.DataFrame
        Filtered  pandas.DataFrame generated from the pyhousehunter.filter() function.

    Returns
    -------
    None

    Examples
    -------
    >>> send_email("helloworld@gmail.com", "results.csv")
    """

    # Check User Input
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if not isinstance(email_recipient, str):
        raise TypeError("The email address must be a string.")
    if re.search(regex, email_recipient) == None:
        raise ValueError("You have input an invalid Email Address.")
    if not isinstance(email_subject, str):
        raise TypeError("The subject must be a string.")
    if not isinstance(filtered_data, pd.DataFrame):
        raise TypeError("The filtered results must be a pandas dataframe.")
    if filtered_data.empty:
        raise ValueError(
            "Your pandas dataframe is empty. There are no results to be emailed."
        )

    # Outline email details
    email_sender = "pyhousehunter@gmail.com"
    email_message = "Houses matching your specifications are attached."
    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = email_recipient
    msg["Subject"] = email_subject
    # Attach email body
    msg.attach(MIMEText(email_message, "plain"))

    # Turn cleaned pandas dataframe to csv email attachment
    buffer = io.StringIO()
    filtered_data.to_csv(buffer)
    part = MIMEBase("application", "octet-stream")
    part.set_payload(buffer.getvalue())
    part.add_header("Content-Disposition", "attachment; filename=results.csv")
    msg.attach(part)

    # Try emailing results
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("pyhousehunter@gmail.com", "dsci524group6")
        server.sendmail(email_sender, email_recipient, msg.as_string())
        print("Email has been successfully sent.")
        server.quit()
    except smtplib.SMTPException as e:
        print(
            f"The email was not sent. The following SMTP error occurred in the process: {e}"
        )

    return
