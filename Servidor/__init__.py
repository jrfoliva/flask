# Importações

from flask import Flask, render_template, render_template_string, session, request, flash, url_for, redirect
from Persistencia.PerfilBD import PerfilBD
from Utilitarios.metodosAuxiliares import validacaoDadosPet
from Utilitarios.metodosAuxiliares import validacaoDadosCliente
from Utilitarios.metodosAuxiliares import validacaoDadosPerfil
from Modelo.Pet import Pet
from Persistencia.PetBD import PetBD
from Modelo.Cliente import Cliente
from Persistencia.ClienteBD import ClienteBD
from Modelo.Perfil import Perfil

app = Flask(__name__)

app.secret_key = 'minha chave secreta'  # necessário para roda o flask


def verificarAutenticacao():
    if session.get('id_usuario'):
        return True
    else:
        return False


# Requisição do tipo GET ou POST
@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    dados = {}
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        for campo in request.form:
            dados[campo] = request.form[campo]
        #print(dados)
        #print(request.form['usuario'] + ' - ' + request.form['senha'])
        #req_usuario = request.form['usuario']
        #req_senha = request.form['senha']
        if dados['usuario'] == 'jose' and dados['senha'] == '123':
            session.clear()
            session['id_usuario'] = '123456'
            return render_template('menu.html')
        else:
            flash('Usuário ou senha inválido!')
            return render_template('login.html')


@app.route("/menu")  #endpoint stático
def menu():
    if verificarAutenticacao():
        return render_template('menu.html')
    else:
        return render_template('login.html')


@app.route("/clientes", methods=['GET', 'POST'])
def cadClientes():
    if verificarAutenticacao():
        cliDB = ClienteBD()
        listaDeClientes = cliDB.consultar("")
        if request.method == "GET":
            return render_template('clientes.html', listaDeClientes=listaDeClientes)
        elif request.method == "POST":
            dados = {}
            for campo, valor in request.form.items():
                dados[campo] = valor
            if validacaoDadosCliente.validaDadosCliente(dados):
                novoCliente = Cliente(dados['nome'], dados['rg'], dados['cpf'], dados['dtNasc'], dados['cep'],
                                      dados['logradouro'], dados['numero'], dados['complemento'], dados['bairro'],
                                      dados['cidade'], dados['uf'], dados['telefone'], dados['email'])

                try:
                    cliDB.incluir(novoCliente)
                    listaDeClientes = cliDB.consultar("")
                    flash('Cliente cadastrado com sucesso!')
                    return render_template('clientes.html', exibeSucesso=True, listaDeClientes=listaDeClientes)
                except Exception as erro:
                    flash(erro)
                    return render_template('clientes.html', exibeSucesso=False, novoCliente=dados, listaDeClientes=listaDeClientes)
            else:
                flash("Informações inválidas!")
                return render_template('clientes.html', exibeSucesso=False, novoCliente=dados, listaDeClientes=listaDeClientes)
    else:
        return render_template('login.html')


# Atualizar Clientes
@app.route("/atualizarCliente", methods=["GET", "POST"])
def atualizarCliente():
    """
        Método devolve uma requisição do tipo GET com os dados para o preenchimento do formulário de clientes,
        ao receber requisição POST, altera as informações no banco de dados.
    """
    if verificarAutenticacao():
        cliDB = ClienteBD()
        if request.method == "GET":
            cpf = request.args.get('cpf')  # recupera o cpf da requisição GET 
            #print(f'Que tipo é o cpf: {type(cpf)}')
            consultaCliente = cliDB.consultar(cpf)
            #print(f'Qual o resultado da consulta?\n{consultaCliente}')
            return render_template("atualizarcliente.html", cliente=consultaCliente)
        else:
            dados = {}
            for campo, valor in request.form.items():
                dados[campo] = valor
            if validacaoDadosCliente.validaDadosCliente(dados):
                cliAlterado = Cliente(dados['nome'], dados['rg'], dados['cpf'], dados['dtNasc'], dados['cep'],
                    dados['logradouro'], dados['numero'], dados['complemento'], dados['bairro'], dados['cidade'], dados['uf'],
                    dados['telefone'], dados['email'])
                try:
                    cliDB.alterar(cliAlterado)
                    listaDeClientes = cliDB.consultar("")
                    flash('Cliente atualizado com sucesso!')
                    return render_template('clientes.html', exibeSucesso=True, listaDeClientes=listaDeClientes)
                except Exception as erro:
                    flash(erro)
                    return render_template('atualizarCliente.html', exibeSucesso=False, listaDeClientes=listaDeClientes)
            else:
                flash("Informações inválidas!")
                return render_template('clientes.html', exibeSucesso=False, listaDeClientes=listaDeClientes)
                
    else:
        return render_template('login.html')


# Excluir Cliente
@app.route("/excluirCliente", methods=["GET", "POST"])
def excluirCliente():
    if verificarAutenticacao():
        cliBD = ClienteBD()
        if request.method == "GET":
            cpf = request.args.get('cpf')
            consultaCliente = cliBD.consultar(cpf)
            return render_template('excluirCliente.html', cliente=consultaCliente)
        else:
            dados = {}
            for campo, valor in request.form.items():
                dados[campo] = valor
            clienteExcluir = Cliente(dados['nome'], dados['rg'], dados['cpf'], dados['dtNasc'], dados['cep'],
                    dados['logradouro'], dados['numero'], dados['complemento'], dados['bairro'], dados['cidade'], dados['uf'],
                    dados['telefone'], dados['email'])
            try:
                cliBD.apagar(clienteExcluir)
                flash("Cliente excluído com sucesso!")
                listaDeClientes = cliBD.consultar('')
                return render_template("clientes.html", exibeSucesso=True, listaDeClientes=listaDeClientes)
            except Exception as erro:
                flash(erro)
                return render_template("clientes.html", exibeSucesso=False)                 
    else:
        return render_template('login.html')


# cadastrar Pet
@app.route("/pets", methods=["GET", "POST"])
def cadPets():
    if verificarAutenticacao():
        petDB = PetBD()
        listaDePets = petDB.consultar("")
        if request.method == "GET":
            return render_template('pets.html', listaDePets=listaDePets) # quer apenas obter a página
        elif request.method == "POST":  # está submetendo dados ao servidor
            # Um dicionário para armazenar os campos e os dados enviados pelo form
            dados = {}
            for campo, valor in request.form.items():
                dados[campo] = valor
            if validacaoDadosPet.validaDadosPet(dados):
                novoPet = Pet(0, dados['nomePet'], dados['especiePet'], dados['racaPet'], dados['corPet'],
                                dados['dataNascPet'], dados['numMicroChipPet'], dados['rgaPet'])
                petDB.incluir(novoPet)
                listaDePets = petDB.consultar("")
                flash("Pet cadastrado com sucesso!")
                return render_template('pets.html', exibeSucesso=True, listaDePets=listaDePets)
            else:
                flash("Informação inválida!")
                return render_template('pets.html', novoPet=dados, exibeSucesso=False, listaDePets=listaDePets)
    else:
        return render_template('login.html')


# Atualizar Pet
# é possivel passar parâmetro para o endpoint ou rota estipulando
# parâmetro entre os caracteres < e >
@app.route("/atualizarPet/<int:id>", methods=['GET', 'POST'])  
def atualizarPet(id):
    if verificarAutenticacao():
        petBD = PetBD()
        pet = petBD.consultar(id)
        listaDePets = petBD.consultar('')
        if pet:
            if request.method == "GET":
                return render_template('atualizarPet.html', pet=pet)
            else:
                #requisição do tipo POST, então prosseguir com a atualização.
                dados = {}
                for campo, valor in request.form.items():
                    dados[campo] = valor
                    
                if validacaoDadosPet.validaDadosPet(dados):
                    petAtualizado = Pet(id, dados['nomePet'], dados['especiePet'], dados['racaPet'], dados['corPet'],
                                dados['dataNascPet'], dados['numMicroChipPet'], dados['rgaPet'])
                    try:
                        petBD.alterar(petAtualizado)
                        flash("Atualização realizada com sucesso")
                        listaDePets = petBD.consultar("")
                        return render_template('pets.html', exibeSucesso=True, listaDePets=listaDePets)
                    except Exception as erro:
                        flash(erro)
                        return render_template('pets.html', exibeSucesso=False, listaDePets=listaDePets)

                else:
                    flash("Informações inválidas!")
                    return render_template('atualizarPet.html', pet=pet)
        else:
            flash("Registro não encontrado no banco de dados.")
            return render_template('pets.html', listaDePets=listaDePets)
    else:
        return render_template('login.html')


# Exclusão de Pet
@app.route("/excluirPet/<int:id>", methods=["GET", "POST"])
def excluirPet(id):
    """
        Método que consulta a existência do registro, retorna a consulta,
        passa um objeto do tipo Pet e seu registro, e aguarda a submit para a 
        exclusão do mesmo.
    """
    if verificarAutenticacao():
        petDB = PetBD()
        consultarPet = petDB.consultar(id)
        if consultarPet:
            if request.method == "GET":
                return render_template('excluirPet.html', pet=consultarPet)
            elif request.method == "POST":
                pet = Pet(consultarPet.codigo, consultarPet.nome, consultarPet.especie, consultarPet.raca,
                    consultarPet.cor, consultarPet.dataNasc, consultarPet.numMicroChip, consultarPet.rga)
                try:
                    petDB.apagar(pet)
                    flash("Exclusão realizada com sucesso!")
                    consultarPet = petDB.consultar("")
                    return render_template('pets.html', exibeSucesso=True, listaDePets=consultarPet)
                except Exception as erro:
                    flash(erro)
            else:
                flash("Informações inválidas!")
                return render_template('pets.html', exibeSucesso=False, listaDePets=consultarPet)
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return render_template('login.html')


@app.route("/produtos", methods=['GET', 'POST'])
def cadProdutos():
    if request.method == 'GET':
        return render_template('produtos.html')
    elif request.method == "POST":
        return render_template('produtos.html')


@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if verificarAutenticacao():
        perfilBD = PerfilBD()
        resultado = perfilBD.consultar("")
        if request.method == "GET":
            return render_template('perfil.html', listaDePerfil=resultado)
        else:
            #verfica se as informações do form são válidas
            dados = {'perfil': '', 'consultar': 0, 'incluir': 0, 'alterar': 0, 'excluir': 0}
            for campo, valor in request.form.items():
                dados[campo] = valor
            print(f"Como são os campos e dados do form?\n{dados}")
            if validacaoDadosPerfil.validaDadosPerfil(dados):
                perfil = Perfil(dados['perfil'], dados['consultar'], dados['incluir'], dados['alterar'], dados['excluir'])
                perfilBD.incluir(perfil)
                listaDePerfil = perfilBD.consultar("")
                flash('Perfil cadastado com sucesso!')
                return render_template('perfil.html', exibeSucesso=True, listaDePerfil=listaDePerfil)
            else:
                flash("Dados inválidos")
                return render_template('perfil.html', exibeSucesso=False, listaDePerfil=resultado)
    else:
        return render_template('login.html')


app.run(host="0.0.0.0", port=5000, debug=1)