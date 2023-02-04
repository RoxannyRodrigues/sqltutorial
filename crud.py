import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'biblioteca',
)

cursor = conexao.cursor()
print("Conectado")

#CRUD

#CREATE
#colunas
"""nome = "Uma terra prometida"
autor = "Strong"
ano = 2020
categoria = "Biografia"

cursor.close()
conexao.close()

comando = f' INSERT INTO livros (nome,autor,ano,categoria) VALUES ("{nome}","{autor}","{ano}","{categoria}")'
cursor.execute(comando)
conexao.commit()""" #se comando edita o banco de dados

#READ"""
"""comando = f' SELECT * FROM livros' 
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dadaos
print(resultado)

cursor.close()
conexao.close()"""

#colunas
nome = "O homem casaco vermelho"
autor = "Julian Barnes"
ano = 1998
categoria = "Biografia"

comando = f' UPDATE livros SET nome = "{nome}", autor = "{autor}", ano = {ano}  WHERE id = 2'  
cursor.execute(comando)
conexao.commit() 


cursor.close()
conexao.close()

