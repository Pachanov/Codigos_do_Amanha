# Variável Global: pode ser acessada de qualquer lugar do código
x = 10 
def funcao():
  print(x)
funcao() # Saida: 10

# Variável Local: só existe dentro da função onde foi criada
def funcao():
  y = 5 
  print(y)
funcao() # Saída: 5

# Variável Global com 'global': permite modificar uma variável global dentro de uma função
contador = 0
def incrementar():
  global contador 
  contador += 1
incrementar()
print(contador)


# Criação de Listas: vazias, com números ou com tipos mistos
lista_vazia = []
lista_numeros = [10, 20, 30, 40]
lista_mista = [1, "Python", 3.14, True]

# Acessando e Modificando: adicionando (append) e removendo (remove) elementos
print(lista_numeros[0])
print(lista_mista[1])
lista_numeros.append(50) 
lista_numeros.remove(20) 
print(lista_numeros)

# Percorrendo a Lista com um laço 'for'
for item in lista_mista: 
  print(item)
  
  
  # Criação de Tuplas: coleções imutáveis de elementos
tupla_exemplo = (10, 20, 30) 
tupla_mista = (1, "Python", 3.14)
print(tupla_exemplo[1])

# Iterando sobre uma lista de tuplas e desempacotando seus valores
dados_pessoas = [ 
  ("Ana", 25, "Engenharia"), 
  ("Bruno", 30, "Medicina"), 
  ("Carla", 22, "Direito") 
]
for pessoa in dados_pessoas: 
  nome, idade, curso = pessoa 
  print(f"{nome} tem {idade} anos e estuda {curso}.")
  
  
  
# Condicional if/else: executa um bloco de código com base em uma condição
idade = 20
if idade >= 18:
  print("Você é maior de idade.")
else: 
  print("Você é menor de idade.")

# Laço for: executa um bloco de código um número definido de vezes
for i in range(5):
  print(i)

# Laço while: repete um bloco de código enquanto uma condição é verdadeira
contador = 0
while contador < 5:
  print(contador)
  contador += 1

# Laço while com 'continue' e 'break': pula para a próxima iteração ou encerra o loop
print("Cadastro rápido de idades para votação (5 pessoas)")
count = 0
while count < 5: 
  idade = int(input(f"Digite a idade da pessoa {count + 1}: "))
  if idade < 0: 
    print("Idade inválida! Tente novamente.")
    continue
  if idade >= 16: 
    print("Pode votar.")
  else: 
    print("Não pode votar.")
  count += 1
  if count == 5: 
    print("Cadastro finalizado.")
    break