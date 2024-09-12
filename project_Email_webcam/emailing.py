import smtplib
from email.message import EmailMessage
import imghdr

sender = "satvik.nanda@gmail.com"
password = "jvxy rfwx uudi rhzk" #purpose: to send the email from the sender account
reciever = "satvik.nanda@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Alert! Movement detected inside the room."

    email_message.set_content("Please be aware, someone just entered the restricted area! Permission to shoot requested.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, reciever, email_message.as_string())
    gmail.quit()
    

if __name__ == "__main__":
    send_email(image_path="project_Email_webcam/images/16.png")
