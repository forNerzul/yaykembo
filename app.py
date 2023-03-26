from flask import Flask, render_template,request, url_for, redirect, session
from wtforms import Form, StringField, validators
from controller.entidades import Jugador, Computadora, Juego

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pollo_frito'

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        session['username'] = username
        return redirect(url_for('game'))

    return render_template('home.html', form=form)

@app.route('/game')
def game():
    desicion = request.args.get('desicion', None, type=str)
    print(f'Esto es desicion {desicion}')
    if desicion == None:
        print('Entro aca')
        username = session.get('username')
        return render_template('game.html', username=username)
    else:
        print(f'Entro aca 2, {desicion}')
        return redirect(url_for('resultado', desicion=desicion))

@app.route('/resultado')
def resultado():
    desicion = request.args.get('desicion', None, type=str)
    print(f'Esto es desicion desde resultado {desicion}')
    if desicion == None:
        return redirect(url_for('home'))
    else:
        username = session.get('username')
        jugador1 = Jugador(username, desicion)
        jugador2 = Computadora()
        juego = Juego(jugador1, jugador2)
        resultado = juego.jugar()

    return render_template('result.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)