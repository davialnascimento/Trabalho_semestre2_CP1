# e implemente as quatro operações sobre uma coleção
#vulnerabilidades. Insira, busque por severidade,
#atualize corrigida para True e delete por cve_id
from pymongo import MongoClient 

#Conecte ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["seguranca"]
vulnerabilidades = db["vulnerabilidades"]
# para inserir muitos insert_many()


vulns = [
    {"cve_id": "CVE-2024-001", "tipo": "SQL Injection", "severidade": "Alta",  "corrigida": False},
    {"cve_id": "CVE-2024-002", "tipo": "XSS",           "severidade": "Media", "corrigida": True},
    {"cve_id": "CVE-2024-003", "tipo": "Path Traversal","severidade": "Critica","corrigida": False},
]

def falhas_vivas(falha):
    falha=vulns
    if falha is True:
        return falha
    else:
        return falha.remove()


#cve
