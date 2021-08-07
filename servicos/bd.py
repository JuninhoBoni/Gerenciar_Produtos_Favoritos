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
    
    def criar_cliente(self):
        colunas = list(self.dados_cliente)
        query = f'''
                    INSERT INTO PUBLIC.CLIENTES
                        ({', '.join(colunas)})
                        VALUES(%s, %s, %s, %s);
                '''
        valores = [self.dados_cliente[coluna] for coluna in colunas]
        
        try:
            self.cursor.execute(query, valores)
            self.conexao.commit()
        except Exception as error:
            return str(error)
