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

vulns_true= [ {"cve_id": "CVE-2024-002", "tipo": "XSS",           "severidade": "Media", "corrigida": True}, ]

#como eu posso fazer que seja checkado se é uma vulnerabilidade verdadeira ou falsa?
cves_true = {vuln["cve_id"] for vuln in vulns_true}

for vuln in vulns:
    if vuln["cve_id"] in cves_true:
        print(f"{vuln['cve_id']} -> Vulnerabilidade verdadeira")
    else:
        print(f"{vuln['cve_id']} -> Vulnerabilidade falsa")

vulnerabilidades.delete_many({})

resultado = vulnerabilidades.insert_many(vulns)

print(f"\n{len(resultado.inserted_ids)} vulnerabilidades inseridas.")



print("\nBuscar severidade='Alta'")

resultado = vulnerabilidades.find({"severidade": "Alta"})

for vuln in resultado:
    print(f"{vuln['cve_id']}: {vuln['tipo']}")




resultado = vulnerabilidades.update_one(
    {"cve_id": "CVE-2024-001"},
    {"$set": {"corrigida": True}}
)

print(f"\nUpdate corrigida=True em 001 -> "
      f"{resultado.modified_count} documento modificado")



quantidade = vulnerabilidades.count_documents(
    {"corrigida": False}
)

print(f"\nCount corrigida=False -> {quantidade}")




resultado = vulnerabilidades.delete_one(
    {"cve_id": "CVE-2024-002"}
)

print(f"\nDelete CVE-2024-002 -> "
      f"{resultado.deleted_count} documento removido")
