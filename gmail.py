#   ██████  ▄▄▄       ███▄ ▄███▓  ██████  ▒█████   ███▄    █  ░  ▓█████▄ ▓█████ ██▒   █▓
# ▒██    ▒ ▒████▄    ▓██▒▀█▀ ██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ░░ ▒▒██▀ ██▌▓█   ▀▓██░   █▒
# ░ ▓██▄   ▒██  ▀█▄  ▓██    ▓██░░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒▀▀░░██   █▌▒███   ▓██  █▒░
#   ▒   ██▒░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░ ░ ░▓█▄   ▌▒▓█  ▄  ▒██ █░░
# ▒██████▒▒ ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒░ ████▓▒░▒██░   ▓██░░▒░░░▒████▓ ░▒████▒  ▒▀█░  
# ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒▒  ▒ ░░ ▒░ ░  ░ ░  
# ░ ░▒  ░ ░  ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░▒░ ░ ░ ▒  ▒  ░ ░  ░  ░ ░░  
# ░  ░  ░    ░   ▒   ░      ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░  ░  ░░ ░ ░ ░  ░    ░       ░░  
#       ░        ░  ░       ░         ░      ░ ░           ░  ░  ░  ░   ░       ░  ░     ░  

import smtplib
import ssl
import time
from pathlib import Path
from tqdm import trange
from email_functions import make_email, send_email

FILE_NAME = 'data/College-Emails-Sheet1.csv'

# prompt user for their gmail and 'app password'
port = 465
gmail_user = str(input('Enter your email: '))
password = str(input('Enter your password: '))
delay = int(input('Enter delay between emails (s): '))
context = ssl.create_default_context()
sent_from = gmail_user

# create list of schools and their emails
schools = []
emails = []
has_titles = True
with open(FILE_NAME, 'r') as f:
  for line in f.readlines():
    if has_titles:
      has_titles = False
    else:
      school,email = line.strip().split(',')
      schools.append(school)
      emails.append(email)

# start server
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  server.login(gmail_user, password)

  # loop through schools -> generate and send emails
  for i in trange(len(schools)):
    time.sleep(delay)
    school = schools[i]
    to = emails[i]
    subject, body = make_email(school)
    send_email(subject, body, school, to, server, sent_from)
  
server.close()
print('Terminated connection')