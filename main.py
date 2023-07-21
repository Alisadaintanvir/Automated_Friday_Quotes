import smtplib
import datetime as dt
import random


def send_mail(message):
    my_email = [YOUR_MAIL]
    password = [YOUR_PASSWORD]
    receiver_email = [RECIEVER_MAIL]

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(my_email, receiver_email, message)
            print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")


now = dt.datetime.now()
week_day = now.weekday()

if week_day == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)
        send_mail(f"Subject:Friday Quotes \n\n {quotes}")
