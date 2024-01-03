#Criando uma gerador de nome para banda
from random import choice

#Aqui estou printando "bem vindo" na tela
print("Bem vindo ao gerador de nome de banda!!")
#Atribuo o dado "cidade"(nome da cidade do usuario) a variável city
city_name = input("Diga a cidade em que cresceu:\n")
#Faço o mesmo, ams agora com o nome do pet do usuario a variável pet
pet_name = input("Agora diga o nome do seu primeiro pet:\n")
#Crio uma lista com as duas variaveis para poder "sortear"
listofnames = [city_name, pet_name]
#Aqui eu faço duas escolhas aleatórias dentro da lista criada e printo o nome da banda a partir das duas escolhas
print("Parabens, o nome da sua banda é:", choice(listofnames), choice(listofnames))
#Aqui é um outro print, utilizando as mesmas informações, que eu estava testando de forma que fizesse mais sentido na lingua portuguesa
print(f"Parabens, o nome da sua banda é: %s de %s" %(pet_name, city_name))