# API Rest de Cadastro de currículos desenvolvido para o teste Dev da empresa CloudOpss

from flask import Flask, render_template, request, redirect, flash, url_for
import pymongo
from cadastro import Cadastro

client = pymongo.MongoClient()
mydb = client["mydb"]

mycollection = mydb["lista_cadastro"]

app = Flask(__name__)
app.secret_key = 'palavrasecreta'

lista_cadastro = []

@app.route('/cadastro')
def inicio():
    return render_template('cadastro.html')


@app.route('/cadastrando', methods=['POST', ])
def cadastrando():
    nome = request. form['nome']
    email = request. form['email']
    telefone = request. form['telefone']
    endereco = request. form['endereco']
    cidade = request. form['cidade']
    estado = request. form['estado']
    numero = request. form['numero']
    complemento = request. form['complemento']
    profissao = request. form['profissao']
    curriculo = request.files['curriculo']
    if curriculo.filename != '':
        curriculo.save(curriculo.filename)
    cadastro = Cadastro(nome, email, telefone, endereco, cidade, estado, numero, complemento, profissao, curriculo)
    lista_cadastro.append(cadastro)
    flash('Usuário Cadastrado')
    data = {'nome': cadastro.nome, 'email': cadastro.email, 'telefone': cadastro.telefone, 'endereco': cadastro.endereco, 'cidade': cadastro.cidade,
            'estado': cadastro.estado, 'numero': cadastro.numero, 'complemento': cadastro.complemento, 'profissao': cadastro.profissao}
    mycollection.insert_one(data)
    return redirect(url_for('lista_de_cadastrados'))


@app.route('/index')
def lista_de_cadastrados():
    return render_template('lista.html', titulo='Lista de Cadastrados', cadastro=lista_cadastro)

app.run()
