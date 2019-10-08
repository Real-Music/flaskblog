import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
import datetime

def save_picture(form_picture):
    current_date = datetime.datetime.now()
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fin = f_name + \
        current_date.strftime('%d-%m-%Y-%I:%M:%S:%f') + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/img/profile', picture_fin)

    # Resize Image
    img_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(img_size)

    i.save(picture_path)

    return picture_fin

# Send Email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com', recipients=[user.email])

    msg.body = f"""To reset your password, visit the following link: -- 
    {url_for('users.reset_token', token= token, _external=True)}

    If you did not make this request, then simply ignore this email and no changes will be made.
    """

    mail.send(msg)
