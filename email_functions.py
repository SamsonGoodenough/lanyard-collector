import unicodedata

def make_email(school):
  subject = f'Hey {school}, I was wondering something.'
  body = f'''Dear {school}, 

My name is Samson Goodenough, and yes, that's my real name.  I'm a student studying computer science and mathematics currently living in London Ontario, Canada. 

I have a bit of an odd hobby, I like to travel to many universities and colleges to attend their school fairs in order to collect a lanyard from them to add to my growing collection.
Right now I have just over 40 lanyards in my collection, and this is where you come in! I was wondering if you would like to help me further expand my collection by sending me one of your school's lanyards.  

As I said before, I live in Canada.  Although I've gone very out of my way to acquire more for my collection, somewhere that I've never gotten the chance to go hunting for them is just over the border.
So now I ask you, would you please send me a {school} branded lanyard?

I would be so gracious if you were to consider sparing one, please let me know if you think this is possible. 

Sincerely, 
 - Samson Goodenough'''

  body = unicodedata.normalize("NFKD", body)
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