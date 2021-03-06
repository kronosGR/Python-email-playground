import smtplib                            # creates smtp server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Kronos'
email['to'] = 'geo.elgeo@gmail.com'
email['subject'] = 'You won 10000000 dollars'

# email.set_content('Learning python')
email.set_content(html.substitute({'name': 'Kronos'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('geo.elgeo@gmail.com', '123456')
    smtp.send_message(email)
    print('Email was sent')
