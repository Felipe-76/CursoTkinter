from tkinter import *
import sqlite3


root = Tk()
root.title("Database")
root.geometry("400x400")

# Criar ou conectar a uma base de dados
conexao = sqlite3.connect("base.db")
# Se a base ainda nao existir essa linha acima irá criar com o nome fornecido.

# Criar um cursor
c = conexao.cursor()

# Criar tabela
c.execute("""CREATE TABLE enderecos(
            primeiro_nome text,
            ultimo_nome text,
            endereco text,
            cidade text,
            estado text,
            cep integer
)""")

# Enviar mudanças
conexao.commit()

# Fechar conexão
conexao.close()
# Ao fechar o programa isso ocorreria automaticamente, mas é bom explicitar


root.mainloop()
