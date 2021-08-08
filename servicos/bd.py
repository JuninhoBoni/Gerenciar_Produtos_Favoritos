import psycopg2
from psycopg2.extensions import AsIs



class PostgreSQL:
    def __init__(self) -> None:
        self.user = "postgres"
        self.password = "juninhoboni"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "postgres"

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               database=self.database)
            self.cursor = self.conexao.cursor()
        except (Exception, psycopg2.Error) as error:
            return f'Falha no banco de dados {error}'

    def desconectar(self):
        if self.conexao:
            self.cursor.close()
            self.conexao.close()
            
    def update_insert(self):
        print(self.valores)
        try:
            self.cursor.execute(self.query, self.valores)
            self.conexao.commit()
            self.linhas = self.cursor.rowcount
        except Exception as error:
            return str(error)

    def consulta(self):
        self.cursor.execute(self.query, self.valores)
        self.registros = self.cursor.fetchall()

    def criar_cliente(self):
        colunas = list(self.dados_cliente)
        self.query = f'''
                    INSERT INTO CLIENTES ({', '.join(colunas)})
                        VALUES(%s, %s, %s, %s);
                '''
        self.valores = [self.dados_cliente[coluna] for coluna in colunas]
        return self.update_insert()

    def atualizar_cliente(self):
        self.query = f'''
                    UPDATE CLIENTES SET NOME=%s WHERE EMAIL=%s AND STATUS=%s;
                '''
        self.valores = self.dados_cliente['nome'], self.dados_cliente['email'], self.dados_cliente['status']
        return self.update_insert()
        
    def visualizar_cliente(self):
        self.query = f'''
                    SELECT {', '.join(self.colunas)} FROM CLIENTES WHERE EMAIL=%s;
                '''
        self.consulta()
        return self.registros