"""
Exercício do curso - básico sobre tipos de dados:
num = input("Digite um número de dois digitos\n")
print(int(num[0]) + int(num[1]))
"""

print("Bem vindo a calculadora de gorjeta\n")
total_conta = float(input("Qual é o total da conta?\nR$"))
pctg_gorjeta = int(input("Qual a porcetagem você quer dar de gorjeta: 10, 12 ou 15?\n"))
#Enquanto não for escolhido uma opção que encaixe ele vai continuar perguntando
while(pctg_gorjeta != 10 and pctg_gorjeta != 12 and pctg_gorjeta != 15):
    pctg_gorjeta = int(input("Por favor escolha entre as opções 10, 12 ou 15.\n"))
#Adiciona a porcentagem da gorjeta ao total da conta
novo_total = ((pctg_gorjeta/100)*total_conta)+total_conta
pagantes = int(input("A conta será dividida entre quantas pessoas?\n"))
#Dividimos o valor total para a quantidade de pessoas que vão pagar
conta_div = novo_total/pagantes
print(f"Cada pessoa deve pagar {conta_div:.2f}")