from flask import Flask

class Cadastro:
    def __init__(self, nome, email, telefone, endereco, cidade, estado, numero, complemento, profissao, curriculo):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento
        self.profissao = profissao
        self.curriculo = curriculo


