import smtplib

sender = "Private Person <from@smtp.mailtrap.io>"
receiver = "A Test User <to@smtp.mailtrap.io>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("006c3dc0bf94a4", "6063bf9a5dae7f")
    server.sendmail(sender, receiver, message)