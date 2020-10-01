from flask import Flask, render_template,request
from flask_mail import Mail,Message
app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME ="stardeepam1@gmail.com", #enable less secure apps in your email's settings
    MAIL_PASSWORD="cheetachug"
)
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help', methods = ['GET', 'POST'])
def help():
    if (request.method == 'POST'):
        message = request.form.get('message')
        msg = Message("Someone needs help call him/her",
                      sender="stardeepam1@gmail.com",
                      recipients=["stardeepam1@gmail.com"])
        msg.body =message
        mail.send(msg)
    return render_template('help.html')



@app.route('/origin')
def origin():
    return render_template('origin.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/India')
def India():
    return render_template('India.html')

@app.route('/evolution')
def evolution():
    return render_template('evolution.html')

@app.route('/findings')
def findings():
    return render_template('findings.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')

@app.route('/types')
def types():
    return render_template('Types of Coronaviruses.html')

@app.route('/outlook')
def outlook():
    return render_template('outlook.html')

app.run(debug=True)