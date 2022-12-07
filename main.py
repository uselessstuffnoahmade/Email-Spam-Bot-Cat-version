import requests # request img from web
import shutil # save img locally
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import ssl

url = 'https://cataas.com/cat'
file_name = 'Image'
res = requests.get(url, stream = True)
if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
strFrom = 'EMAIL THATS SENDING EMAIL'
strTo = 'WHOS BEING SENT EMAIL'
email_sender = 'EMAIL THATS SENDING EMAIL'
email_password ='EXTERNAL APP TWO FACTOR AUTHENTICATION PASSWORD'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Random Cat'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'Multi-part message in MIME format.'
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)
msgText = MIMEText('<b>Here is a random Cat! <i></i> </b> .<br><img src="cid:image1"><br>', 'html')
msgAlternative.attach(msgText)
fp = open('Image', 'rb') #Read image
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
context = ssl.create_default_context()
import smtplib
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())