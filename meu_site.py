from flask import Flask, render_template

unistone = Flask(__name__)

# criar a 1° pagina do site
# route   -> www.unistorn.com/
# função  -> o que voçe quer exibir naquela pagina
# templates

@unistone.route('/')
def homepage():
    return render_template('homepage.html')

@unistone.route('/contatos')
def contatos():
    return render_template('contatos.html')

@unistone.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

# colocar site no ar
if __name__ == '__main__':
    unistone.run(debug=True)

    # servidor do heroku

