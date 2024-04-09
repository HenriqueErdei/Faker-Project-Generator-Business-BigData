import datetime
from faker import Faker
import random
import csv

fake = Faker()

num_rows = 3500

headers = ["Filial", "Documento", "Nome_Cliente", "Nome_Vendedor", "Produtos", "Quantidade", "Preco_Unitario", "Total", "Estado_Cliente", "Data_Compra", "Data_Devolucao", "Status"]

FILIAL = [
    "São Paulo",
    "Parana",
    "Rio de Janeiro",
]

VENDEDOR = [
    "Paulo",
    "João",
    "Vanessa",
    "Maria",
    "Taize",
    "Henrique",
]

CLIENTE = [
    "Soluções NovaTech S.A",
    "Inovação QuantumLeap Ltda",
    "Grupo Dinâmica Horizon Ltda",
    "Empresas Esfera de Sinergia Ltda",
    "Corporação TechNex",
    "Tecnologias Ondas Futuras Ltda",
    "Laboratórios InovateX Ltda",
    "Empreendimentos NexusTech Ltda",
    "Empresa Visionária de Inovações S.A",
    "Indústrias ApexTech Ltda",
    "Soluções Núcleo Quântico Ltda",
    "InovarHub S.A",
    "Sistemas Sinérgicos Ltda",
    "Corporação TechVantage",
    "Inovação Esfera Quântica Ltda",
    "Empreendimentos NovaGenius Ltda",
    "Grupo Borda de Inovação Ltda",
    "VisionáriaTech S.A",
    "Corporação NexusGen",
    "Tecnologias Impulso Quântico Ltda",
]

PRODUTO = [
    {"nome": "PlayStation 2", "preco": 499},
    {"nome": "Nintendo DS", "preco": 389},
    {"nome": "Game Boy", "preco": 79},
    {"nome": "PlayStation 4", "preco": 1399},
    {"nome": "PlayStation 1", "preco": 199},
    {"nome": "Nintendo Wii", "preco": 1699},
    {"nome": "XBOX 360", "preco": 1299},
    {"nome": "XBOX ONE S", "preco": 1499},
]

ESTADO = [
    "AC", 
    "AL",
    "AM", 
    "AP", 
    "BA", 
    "CE", 
    "DF", 
    "ES", 
    "GO", 
    "MA", 
    "MG", 
    "MS", 
    "MT", 
    "PA", 
    "PB", 
    "PE", 
    "PI", 
    "PR", 
    "RJ", 
    "RN", 
    "RO", 
    "RR", 
    "RS", 
    "SC", 
    "SE", 
    "SP", 
    "TO"
]

with open("input.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for i in range(num_rows):
        date = fake.date_between_dates(
            date_start=datetime.date(2020, 1, 1),
            date_end=datetime.date(2024, 12, 31)
        )

        Filial = random.choice(FILIAL)
        Documento = random.randint(1000, 9999)
        Nome_Vendedor = random.choice(VENDEDOR)
        Nome_Cliente = random.choice(CLIENTE)
        Produto = random.choice(PRODUTO)
        Quantidade = random.randint(1, 40)
        Preco_Unitario = Produto["preco"]
        Total = Preco_Unitario * Quantidade
        Estado_Cliente = random.choice(ESTADO)


        # Verifica se a transação deve ter uma devolução
        if random.random() < 0.33:
            # Adiciona uma data de devolução aleatória até 30 dias após a data de compra
            data_devolucao = fake.date_between_dates(date_start=date, date_end=date + datetime.timedelta(days=30))
            # Calcula o valor da transação de devolução (33% do valor total da compra)
            valor_devolucao = Total * 0.33
            Status = "Com Devolução"
        else:
            data_devolucao = ""
            valor_devolucao = ""
            Status = "Sem Devolução"

        writer.writerow([Filial, Documento, Nome_Cliente, Nome_Vendedor, Produto["nome"], Quantidade, Preco_Unitario, Total, Estado_Cliente , date, data_devolucao, Status])
