# Função que recebe um nome e imprime uma saudação
def saudacao(nome): # "nome" é um parâmetro
  print(f"Olá, {nome}!")
saudacao("Maria") # "Maria" é o argumento

# Exemplo de função com argumentos posicionais (*args) e nomeados (**kwargs)
def exemplo(a, b=10, *args, **kwargs):
  print("a =", a)
  print("b =", b)
  print("args =", args)
  print("kwargs =", kwargs)
exemplo(1, 2, 3, 4, x=100, y=200)

# Função para incrementar uma variável global
contador = 0
def incrementar():
  global contador
  contador += 1
incrementar()
print(contador)


# Verifica se a pessoa é maior de idade
idade = 20
if idade >= 18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")
  
  
# Laço for para repetir uma ação um número específico de vezes
for i in range(5):
  print(i)
  
  
# Laço while para repetir enquanto uma condição for verdadeira
contador = 0
while contador < 5:
  print(contador)
  contador += 1
  
# Exemplo de laço while com break e continue
print("Cadastro rápido de idades para votação (5 pessoas)")
count = 0
while count < 5:
  idade = int(input(f"Digite a idade da pessoa {count + 1}: "))
  # Se idade for negativa, ignore e peça novamente
  if idade < 0:
    print("Idade inválida! Tente novamente.")
    continue # volta para o começo do while
  # Verifica se pode votar
  if idade >= 16:
    print("Pode votar.")
  else:
    print("Não pode votar.")
  count += 1
  # Se já cadastrou 5 pessoas, encerra o loop
  if count == 5:
    print("Cadastro finalizado.")
    break