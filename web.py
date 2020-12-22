import calculator
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    h1 = '<h1> Calculadora Olist </h1>'
    ol = '''
            <ol> 
                <li><a href='/soma'>Somar</a></li>
                <li><a href='/subtracao'>Subtrair</a></li> 
                <li><a href='/multiplicacao'>Multiplicar</a></li>
                <li><a href='/divisao'>Dividir</a></li>
            </ol>
        '''
    return f'{h1} {ol}'


@app.route('/soma')
def soma():
    parcela1 = 3.0
    parcela2 = 5.0
    soma = calculator.soma(parcela1, parcela2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A soma de 3+5 é : {soma}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'


@app.route('/subtracao')
def subtracao():
    minuendo = 8.0
    subtraendo = 2.0
    diferenca = calculator.subtracao(minuendo, subtraendo)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 8-2 é : {diferenca}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'


@app.route('/multiplicacao')
def multiplicacao():
    fator1 = 2.0
    fator2 = 3.0
    produto = calculator.multiplicacao(fator1, fator2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 2*3 é : {produto}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'


@app.route('/divisao')
def divisao():
    dividendo = 9.0
    divisor = 3.0
    quociente = calculator.divisao(dividendo, divisor)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 9/3 é : {quociente}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

app.run()
