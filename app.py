from flask import Flask, render_template,request, url_for
from wtforms import Form, StringField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        return render_template('game.html')

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)