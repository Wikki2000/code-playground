#!/usr/bin/python3
"""
Extract data from excel sheet (e.g., Name, Email etc),
Send bulk email to register members using this data.
"""
import sib_api_v3_sdk
import pandas as pd
from typing import Dict
from os import getenv
import json


def fwd_token(mail: str, kwargs: Dict[str, str]) -> bool:
    """Send token to email.

    Args:
        mail (string): The mail to be sent.
        kwargs (dict): key-values pairs of name and emai of recipeint.
    """
    config = sib_api_v3_sdk.Configuration()
    config.api_key["api-key"] = getenv("MAIL_API_KEY")
    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(config)
    )

    sender = {"name": "Gofamints Corper Fellowship - GCF", "email": getenv("SENDER_MAIL")}
    email_subject = "[GCF] Invitation for GCF Skill Acquisation"
    recipient = [kwargs]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=recipient, sender=sender, subject=email_subject,
        html_content=mail
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def read_html_file(file_path: str, name: str) -> str:
    """Read email from file and substitue placeholder."""
    with open(file_path, "r") as f:
        content = f.read()

    # Replace content with placeholder
    content = content.replace("{{ name }}", name)
    return content


def read_excel_file(file_path: str) -> Dict[str, str]:
    """Read the data from excel file into json data"""

    # Load the Excel file
    data = pd.read_excel(file_path)

    # Convert DataFrame to JSON and extract email and name using their key
    selected_columns = data[["Name", "E-mail Address"]]

    json_data = selected_columns.to_json(orient="records", indent=4)
    return json_data


def main():
    """ Entry of other functions
    """
    
    data = read_excel_file("gcf_skills.xlsx")
    parsed_data = json.loads(data)

    # Get the name and email for each participant
    for item in parsed_data:

        # Read the email content and interpolate with user name in placeholder
        # Sent the email to each user or participant
        email_content = read_html_file("mail.html", item["Name"])
        recipient = {"name": item["Name"], "email": item["E-mail Address"]}
        is_send = fwd_token(email_content, recipient)
        if is_send:
            print(f"Email sent to {item['Name']}")
        else:
            print(f"Email was'nt sent to {item['Name']}")
    print("Email completely sent to all participant")


if __name__ == "__main__":
    main()
