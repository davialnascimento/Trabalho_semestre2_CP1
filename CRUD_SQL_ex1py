import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="seguranca"
)

cursor = conexao.cursor()

ativos = [
    ("SRV-WEB01", "192.168.1.10", "servidor", "alta", "ativo"),
    ("PC-RH03",   "192.168.1.45", "estacao",  "baixa", "ativo"),
    ("SW-CORE01", "192.168.1.1",  "switch",   "media", "inativo"),
]

sql = """
INSERT INTO ativos (nome, ip, tipo, criticidade, status)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(sql, ativos)
conexao.commit()

print(f"{cursor.rowcount} ativos cadastrados.")

cursor.close()
conexao.close()
