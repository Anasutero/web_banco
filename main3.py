import os
# possibilita a manipulação do servidor 
from http.server import SimpleHTTPRequestHandler
import socketserver
from urllib.parse import urlparse, parse_qs
from database import conectar

conexao = conectar()

# biblioteca que cipritografa as senhas
import hashlib

# CRIAÇÃO DO SERVIDOR
class MyHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            # Tenta abrir o arquivo idx.html
            f = open(os.path.join(path, 'index.html'), 'r')
            # Se existir, envia o conteúdo do arquivo
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass

        return super().list_directory(path)
    

    # CANAL DE COMUNICAÇÃO
    def do_GET(self):
        if self.path == '/login':
            # Tenta abrir o arquivo login.html
            try:
                with open(os.path.join(os.getcwd(), 'login.html'), 'r') as login_file:
                    content = login_file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # criação de rota para página de suscesso de login
        elif self.path == '/turmas':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'cadastro_turma.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

        # criação de rota para página de suscesso de login
        elif self.path == '/usuario_cadastrado':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'sucesso.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

        # criação de rota para página de erro
        elif self.path == '/login_failed':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'login.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()

                # Adiciona a mensagem de erro no conteúdo da página
            mensagem = "Login e/ou senha incorreta. Tente novamente"
            content = content.replace('<!-- Mensagem de erro será inserida aqui -->',
                                      f'<div class="error-message">{mensagem}</div>')
            
            self.wfile.write(content.encode('utf-8'))

        # criação do usuário não existente 
        elif self.path.startswith('/cadastro'):

            # Extraindo os parâmetros da URL
            query_params = parse_qs(urlparse(self.path).query)
            login = query_params.get('login', [''])[0]
            senha = query_params.get('senha', [''])[0]

            # Mensagem de boas-vindas
            welcome_message = f"Olá {login}, seja bem-vindo! Percebemos que você é novo por aqui. Complete o seu cadastro."

            # Responde ao cliente com a página de cadastro
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Lê o conteúdo da página cadastro.html
            with open(os.path.join(os.getcwd(), 'cadastro.html'), 'r', encoding='utf-8') as cadastro_file:
                content = cadastro_file.read()

            # Substitui os marcadores de posição pelos valores correspondentes
            content = content.replace('{login}', login)
            content = content.replace('{senha}', senha)
            content = content.replace('{welcome_message}', welcome_message)

            # Envia o conteúdo modificado para o cliente
            self.wfile.write(content.encode('utf-8'))
            return  # Adicionando um return para evitar a execução do restante do código
        
        # criação de rota para página de suscesso do cadastro da turma
        elif self.path == '/cad_turma':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'cadastro_turma.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

        # criação de rota para página de erro do cadastro de turma
        elif self.path == '/failed_turma':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'erro.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

          # criação de rota para página de suscesso do cadastro da turma
        elif self.path == '/cad_ativ':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'cadastro_atividade.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

        elif self.path == '/tela_professor':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'tela_professor.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))

        elif self.path == '/tela_atividades':
            # Responde ao cliente com a menssagem de login/senha incorreta
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Lê o conteúdo da página html
            with open(os.path.join(os.getcwd(), 'tela_atividades.html'), 'r', encoding='utf-8') as login_file:
                content = login_file.read()            
            self.wfile.write(content.encode('utf-8'))        

        else:
            # Se não for a rota "/login", continua com o comportamento padrão
            super().do_GET()

    # FUNÇÕES PARA REAIZAR AS VALIDAÇÕES DE LOGIN
    def usuario_existente(self,login,senha):
        cursor = conexao.cursor()
        cursor.execute('SELECT senha FROM dados_login WHERE login = %s' , (login ,))
        resultado = cursor.fetchone()#LEITURA LINHA A LINHA
        cursor.close()
        if resultado:
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            return senha_hash == resultado[0]
        return False
        
    def adicionar_usuário(self, login, senha, nome):
        cursor = conexao.cursor()
        senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        cursor.execute('INSERT INTO dados_login (login,senha,nome)VALUES (%s,%s,%s)',(login,senha_hash,nome))
        conexao.commit()
        cursor.close()


    def remover_ultima_linha(self, arquivo):
        print ("Vou excluir ultima linha")
        with open(arquivo, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.writelines(lines[:-1])

    # Funções para Cadastro da Turma
    def turma_existente(self, turma):
        cursor = conexao.cursor()
        cursor.execute("SELECT descricao FROM turmas WHERE descricao =%s " ,(turma,))
        resultado = cursor.fetchone()
        cursor.close()


        if resultado == "":
            return True
        return False
       
    #aqui mexendo
    def adicionar_turma(self, turma):
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO turmas (descricao) VALUES (%s)" ,(turma ,))
        conexao.commit()
        cursor.close()
       

    
    # Funções para Cadastro da Atividade
    def atividade_existente(self, descricao):
        cursor = conexao.cursor()
        cursor.execute("SELECT descricao FROM  atividades WHERE descricao =%s " ,(descricao,))
        resultado = cursor.fetchone()
        cursor.close()


        if resultado =="":
            return True
        return False
      
    
    def adicionar_atividade(self, descricao):
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO atividades (descricao) VALUES (%s)" ,(descricao ,))
        conexao.commit()
        cursor.close()
        
    

    # Captura dos dados do formulário através do 'action' inserir nor 'form'
    def do_POST(self):
        # Usuário logado com Sucesso
        # Verifica se a rota é "/enviar_login"
        if self.path == '/enviar_login':
            content_length = int(self.headers['Content-Length'])
            # Lê o corpo da requisição
            body = self.rfile.read(content_length).decode('utf-8')
            # Parseia os dados do formulário
            form_data = parse_qs(body, keep_blank_values=True)

            # Exibe os dados no terminal
            print("Dados do formulário:")
            print("Email:", form_data.get('email', [''])[0])
            print("Senha:", form_data.get('senha', [''])[0])

            # Verifica se o usuário já existe
            login = form_data.get('email', [''])[0]
            senha = form_data.get('senha', [''])[0]
            
            #NO DA PRO ISSO MUDA -- POREM NAO SEI
            if self.usuario_existente(login, senha):
                # Responde ao cliente indicando que o usuário logou com sucesso
                self.send_response(302)
                self.send_header('Location', '/turmas')
                self.end_headers()
                # Adicionando um return para evitar a execução do restante do código
                return 
        
            else:
                #vERIFICA SE O USUARIO JÁ ESTA CADASTRADO. Caso esteja foi caso de login errado
                # Verifica se o login já existe no arquivo
                cursor = conexao.cursor()
                cursor.execute('SELECT login FROM dados_login WHERE  login = %s' ,(login,))
                resultado = cursor.fetchone()

                if resultado:
                    # Redireciona o cliente para a rota "/login_failed"
                    self.send_response(302)
                    self.send_header('Location', '/login_failed')
                    self.end_headers()
                    cursor.close()
                    # Adicionando um return para evitar a execução do restante do código
                    return 

                else:
                    self.send_response(302)
                    self.send_header('Location', f'/cadastro?login={login}&senha={senha}')
                    self.end_headers()
                    cursor.close()
                    # Adicionando um return para evitar a execução do restante do código
                    return  


        elif self.path.startswith('/confirmar_cadastro'):
            # Obtém o comprimento do corpo da requisição
            content_length = int(self.headers['Content-Length'])
            # Lê o corpo da requisição
            body = self.rfile.read(content_length).decode('utf-8')
            # Parseia os dados do formulário
            form_data = parse_qs(body, keep_blank_values=True)

            #query_params = parse_qs(urlparse(self.path).query)
            login = form_data.get('email', [''])[0]
            senha = form_data.get('senha', [''])[0]
            nome = form_data.get('nome', [''])[0]

            #chamo a função de adicionar o usuario
            self.adicionar_usuário(login,senha,nome)
            #imprimo que o registro foi armazenado com sucesso
            with open(os.path.join(os.getcwd(), 'cadastro_turma.html'), 'r') as login_file:
                    content = login_file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))

          
        # CADASTRAR TURMA
        elif self.path == '/cad_turma':
            # Cadastra a turma se ela não existir
            content_length = int(self.headers['Content-Length'])
            # Lê o corpo da requisição
            body = self.rfile.read(content_length).decode('utf-8')
            # Parseia os dados do formulário
            form_data = parse_qs(body, keep_blank_values=True)

            
            turma = form_data.get('turma', [''])[0]

            # Verifica se o valor está vazio e da erro
            if  turma.strip() == '':
                # Se algum campo estiver vazio, redireciona para a página de falha cadastro 
                self.send_response(302)
                self.send_header("Location", "/failed_turma")
                self.end_headers()
                return
        
            # Verifica se o usuário já existe
            elif self.turma_existente(turma) == True:
                # Se algum campo estiver vazio, redireciona para a página de falha cadastro 
                self.send_response(302)
                self.send_header("Location", "/failed_turma")
                self.end_headers()
                return

            # Adiciona a turma
            else:
                self.adicionar_turma(turma)
                self.send_response(302)
                self.send_header('Location', '/tela_professor')#CRIAR UMA NOVA ROTA PARA COLOCAR A TELA QUE EU DESEJO
                self.end_headers()
                return
            

        # CADASTRAR ATIVIDADE
        elif self.path == '/cad_ativ':
            # Cadastra a turma se ela não existir
            content_length = int(self.headers['Content-Length'])
            # Lê o corpo da requisição
            body = self.rfile.read(content_length).decode('utf-8')
            # Parseia os dados do formulário
            form_data = parse_qs(body, keep_blank_values=True)

            descricao = form_data.get('descricao', [''])[0]

            print( descricao)

            # Verifica se o valor está vazio e da erro
            if descricao.strip() == '':
                # Se algum campo estiver vazio, redireciona para a página de falha cadastro 
                self.send_response(302)
                self.send_header("Location", "/failed_turma")
                self.end_headers()
                return
        
            # Verifica se o usuário já existe
            elif self.atividade_existente( descricao) == True:
                # Se algum campo estiver vazio, redireciona para a página de falha cadastro 
                self.send_response(302)
                self.send_header("Location", "/failed_turma")
                self.end_headers()
                return

            # Adiciona a atividade
            else:
                self.adicionar_atividade( descricao)
                self.send_response(302)
                self.send_header('Location', '/tela_atividades')#CRIAR UMA NOVA ROTA PARA COLOCAR A TELA QUE EU DESEJO
                self.end_headers()
                return
            

        else:
            # Se não for a rota "/enviar_login", continua com o comportamento padrão
            super(MyHandler, self).do_POST()


# Define o IP e a porta a serem utilizados
endereco_ip = "0.0.0.0"
porta = 8000

# Cria um servidor na porta e IP especificados
with socketserver.TCPServer((endereco_ip, porta), MyHandler) as httpd:
    print(f"Servidor iniciado em {endereco_ip}:{porta}")
    # Mantém o servidor em execução
    httpd.serve_forever()