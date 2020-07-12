def make_email(school):
  subject = f'Hey {school}, I was wondering something.'
  body = f'''Dear {school}, 

I was wondering if you would help.  

Thanks, 
 - Samson Goodenough'''

  return subject, body

def send_email(subject, body, school, to, server, sent_from):
  email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

  try:
    server.sendmail(sent_from, to, email_text)
    print(f'Email sent to {to}!')

  except:
    print(f'Could not send email to {to}.')