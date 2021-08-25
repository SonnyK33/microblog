from flask_mail import Message
from app import app, db
from app import mail

msg = Message('test subject', sender=app.config['ADMINS'][0],
recipients=['sonny.kushwaha@gmail.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)

from app import app
