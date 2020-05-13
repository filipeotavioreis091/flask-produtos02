from flask import Flask, render_template
app = Flask(__name__)

produtos = [
        ['Refrigerante', 4.50],
        ['Pizza', 2.50],
        ['Suco', 24.90],
        ['Salgado', 5.50],
        ['Lanche', 18.50]
    ]

@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Produtos',
        produtos=produtos
    )

@app.route('/prod/<int:id>')
def pokemon(id):
    prod = produtos[id]
    return render_template(
        'produtos.html',
        produto=prod
    )

if __name__ == '__main__':
    app.run()