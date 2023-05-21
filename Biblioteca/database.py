import psycopg2

class Conexao:

    def __init__(self, dbname, host, port, user, password) -> None:
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
    
    def consultarBanco(self, sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)

        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado
    
    def manipularBanco(self,sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()

        conn.close()


con = Conexao(dbname = "Biblioteca" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )

def search_book(conexao, variavel):
    book = conexao.consultarBanco(f'''
    select id, titulo, autor, ano, paginas  from "livros"
    where "titulo" = '{variavel}'
    ''')
    return book

def search_book_autor(conexao, variavel):
    book = conexao.consultarBanco(f'''
    select id, titulo, autor, ano, paginas  from "livros"
    where "autor" = '{variavel}'
    ''')
    return book
    
def search_book_auto_titulo(conexao):
    lista = []
    livros = conexao.consultarBanco('''
    select titulo from "livros"''')
    for livro in livros:
        lista.append(livro[0])
    return lista

def search_book_auto_autor(conexao):
    lista = []
    autores = conexao.consultarBanco('''
    select autor from "livros"''')
    for autor in autores:
        if autor[0] != None and autor !=None:
            autor_2 = autor[0].replace("'", " ")
            lista.append(autor_2)
    return lista


def criar_tabela_aluguel(conexao):
    sql = conexao.manipularBanco (''' 
    CREATE TABLE "aluguel"(
    "id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "id_usuario" int NOT NULL,
    "id_livro" int NOT NULL,
    "data" timestamp default CURRENT_TIMESTAMP(0),
    CONSTRAINT fk_usuario
        FOREIGN KEY("id_usuario")
        REFERENCES "usuarios"("id")
        ,
    CONSTRAINT fk_livro
        FOREIGN KEY("id_livro")
        REFERENCES "livros"("id")
    )
    ''')
    return sql

