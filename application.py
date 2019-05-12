from flask import Flask, abort, redirect, render_template, request, flash, url_for
import smtplib
from form import ContactForm
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
import os
import sqlalchemy

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sapanravalcs50@gmail.com'
app.config["MAIL_PASSWORD"] = 'spring2019'

mail.init_app(app)



@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/experience")
def experience():
    return render_template('experience.html')

@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/certification")
def certification():
    return render_template('certification.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route('/form', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['sapanravalcs50@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            flash(f'Thank you for your Message {form.name.data}! I will reach out to you soon', 'success')
            return redirect(url_for('index'))
    return render_template('form.html',form=form)

if __name__ == '__main__':
  app.run(debug=True)
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
