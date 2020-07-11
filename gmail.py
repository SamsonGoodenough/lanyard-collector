import smtplib
import ssl

#   ██████  ▄▄▄       ███▄ ▄███▓  ██████  ▒█████   ███▄    █  ░  ▓█████▄ ▓█████ ██▒   █▓
# ▒██    ▒ ▒████▄    ▓██▒▀█▀ ██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ░░ ▒▒██▀ ██▌▓█   ▀▓██░   █▒
# ░ ▓██▄   ▒██  ▀█▄  ▓██    ▓██░░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒▀▀░░██   █▌▒███   ▓██  █▒░
#   ▒   ██▒░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░ ░ ░▓█▄   ▌▒▓█  ▄  ▒██ █░░
# ▒██████▒▒ ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒░ ████▓▒░▒██░   ▓██░░▒░░░▒████▓ ░▒████▒  ▒▀█░  
# ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒▒  ▒ ░░ ▒░ ░  ░ ░  
# ░ ░▒  ░ ░  ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░▒░ ░ ░ ▒  ▒  ░ ░  ░  ░ ░░  
# ░  ░  ░    ░   ▒   ░      ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░  ░  ░░ ░ ░ ░  ░    ░       ░░  
#       ░        ░  ░       ░         ░      ░ ░           ░  ░  ░  ░   ░       ░  ░     ░  

# prompt user for their gmail and 'app password'
port = 465
gmail_user = str(input('Email: '))
password = str(input('Password: '))
context = ssl.create_default_context()

sent_from = gmail_user
to = ['goodenough.samson@gmail.com']
subject = "OMG Super Important Message"
body = "Hey, what's up?"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  server.login("goodenough.samson@gmail.com", password)

  try:
    server.sendmail(sent_from, to, email_text)
    print('Email sent to {:}!'.format(to[0]))

  except:
    print('Something went wrong.')
  
server.close()
print('Terminated connection')
