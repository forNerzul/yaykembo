from flask import Flask, render_template,request, url_for, redirect
from wtforms import Form, StringField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        return redirect(url_for('game', username=username))

    return render_template('home.html', form=form)

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method != 'POST':
        username = request.args.get('username')
        desicion = request.args.get('desicion')

        print(username)
        print(desicion)
        return render_template('game.html', username=username, desicion=desicion)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)