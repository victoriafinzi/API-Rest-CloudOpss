# API Rest para cadastro de pessoas - Teste CloudOpss
API Rest desenvolvida para o teste de conhecimento da empresa CloudOpss. Essa API foi escrita utilizando Python (backend), o formulário foi escrito utilizando HTML e BootStrap (frontend) e o suporte ao banco de dados nosql utilizado foi o Mongodb. E para fazer a comunicação entre o backend, frontend e o banco de dados foi utilizado o framework Flask.
O objetivo da criação da aplicação foi possibilitar o cadastro de pessoas e que essas informações fossem armazenadas no banco de dados. 

# Funcionalidades
- página de cadastro de pessoas com informações dos dados:
  - Nome, E-mail, Telefone, Endereço Completo, Profissão e Upload de Currículo.
  - Botão de salvar, limpar e voltar.
- página de listagem das pessoas cadastradas
- informações cadastradas são armazenadas no bando de dados nosql mongodb (menos o currículo que é armazenada em memória local)

# Como utilizar a API
### Requisitos:
1. Entre em [github](https://github.com/victoriafinzi/API-Rest-CloudOpss/tree/master), clique em code e baixe o zip do repositório.  
2. Baixe o [Python](https://www.python.org/downloads/) - basta clicar em Download Python (versão que estiver).
3. Baixe o [PyCharm Community](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows) e o instale.
4. Baixe o [MongoDB Community](https://www.mongodb.com/try/download/community) version: 5.0.6, na plataforma do seu sistema operacional e msi como package. Depois de baixado o instale.

### Rodando a API:
1. Abra o Pycharm, clique em Open e selecione o diretório baixado no [github](https://github.com/victoriafinzi/API-Rest-CloudOpss/tree/master)   
![1](https://user-images.githubusercontent.com/36055318/158282541-131d50f2-97cd-4749-8d4f-fd15b4d96a91.jpg)
2. Caso apareça um popup para confirmar o projeto como confiável, basta aceitar e continuar. 
3. Vá no canto superior esquerdo e selecione o módulo main.py com o botão direito e clique em run. Irá abrir uma nova tela chamada "edit configuration" e no Python interpreter selecione o python 3.10 como indicado na imagem abaixo e clique no botão run para finalizar.   
![2](https://user-images.githubusercontent.com/36055318/158296410-90c71614-f637-4535-bf79-b9c3446449ed.jpg)
4. Feito isso, irá abrir um console com o endereço da API http://127.0.0.1:5000/ no qual você deverá clicar e será direcionado para o navegador com o frontend.
5. Agora você poderá cadastrar as pessoas e armazenar os currículos em memória local. 
