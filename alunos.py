import random #importa a biblioteca

numero = random.randrange(1,5) #cria a variavel com a probabilidade de cada aluno
nomealuno = ("nada") #cria a variavel para escolha do aluno
lista = ["ricardo","judite", "douglas", "jorge"] #nome dos alunos

	
print('Aluno escolhido: ', random.choice(lista)) #manda o resultado no console
