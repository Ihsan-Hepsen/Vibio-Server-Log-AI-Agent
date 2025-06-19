import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "info@vibio.co"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = "info@vibio.co"


def send_report_email(log_report: str) -> None:
    msg = MIMEMultipart()
    msg["From"] = "Vibio Log Agent Report"
    msg["To"] = TO_EMAIL
    msg["Subject"] = "Latest Server Log Report"

    body = f"\n{log_report}\n"
    body = MIMEText(body)
    msg.attach(body)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print("[info]: Log report mail is sent")
    except Exception as e:
        print("[error]: Failed to send email: {e}")
