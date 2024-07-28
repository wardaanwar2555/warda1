import smtplib

email = input("SENDER EMAIL: ")
receiver_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT: ")
print("MESSAGE: ")
message = """
This is the first paragraph.

This is the second paragraph.

This is the third paragraph.
"""

text = f"Subject: {subject}\n\n{message}"

# Use the appropriate app password here
app_password = "your_app_password_here"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "jywz nzar jeuh fpmu") #your app password here

    server.sendmail(email, receiver_email, text)
    server.quit()

    print("Email has been sent to " + receiver_email)
except Exception as e:
    print("An error occurred: ", e)
