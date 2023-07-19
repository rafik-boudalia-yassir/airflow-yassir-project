import smtplib

def send():
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        email = "rafik.boudalia@yassir.com"
        password = "mhpsuspjqzcutoak"
        
        recipient = "rafik.boudalia.2001@gmail.com"

        subject = "Testing SMTP Script"
        body_text = "Testing the tutorial is success (just a test)"
        message = f"Subject: {subject}\n\n{body_text}"

        x = smtplib.SMTP(smtp_server, smtp_port)
        x.starttls()
        x.login(email, password)
        x.sendmail(email, recipient, message)
        x.quit()
        print("Success")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))
        print("Failure")

send()
