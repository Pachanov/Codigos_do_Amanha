# Dados iniciais para a análise
dados_funcionarios = {
  'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
  'Departamento': ['Vendas', 'Marketing', 'Vendas', 'RH', 'Vendas'],
  'Salario': [4500, 5200, 4800, 3900, 6100]
}

# Título: Criar o DataFrame
import pandas as pd

# Crie o DataFrame a partir do dicionário
df = pd.DataFrame(dados_funcionarios)

# Exiba o DataFrame para verificação
print("DataFrame Original:")
print(df)


# Título: Filtrar funcionários do departamento de Vendas
# Use a sintaxe de filtro com colchetes: df[df['Coluna'] == 'valor']
vendas_df = df[df['Departamento'] == 'Vendas']

# Imprima o DataFrame filtrado
print("\nFuncionários do departamento de Vendas:")
print(vendas_df)

# Título: Calcular a média salarial com NumPy
import numpy as np

# Passe a coluna 'Salario' do DataFrame diretamente para a função np.mean()
media_salarial = np.mean(df['Salario'])

# Imprima a média salarial
print(f"\nA média salarial de todos os funcionários é: R${media_salarial:.2f}")

# Título: Adicionar uma nova coluna 'Bonus'
# df['Nova_Coluna'] = operação
df['Bonus'] = df['Salario'] * 0.10

# Exiba o DataFrame com a nova coluna
print("\nDataFrame com a nova coluna 'Bonus':")
print(df)