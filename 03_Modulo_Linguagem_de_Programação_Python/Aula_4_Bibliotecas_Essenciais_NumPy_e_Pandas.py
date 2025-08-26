# Dados iniciais
dados_funcionarios = {
  'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
  'Departamento': ['Vendas', 'Marketing', 'Vendas', 'RH', 'Vendas'],
  'Salario': [4500, 5200, 4800, 3900, 6100]
}


import pandas as pd

# Crie o DataFrame a partir do dicionário
df = pd.DataFrame(dados_funcionarios)

# Exiba o DataFrame para verificar
print("DataFrame Original:")
print(df)


# Filtre o DataFrame para mostrar apenas funcionários de "Vendas"
vendas_df = df[df['Departamento'] == 'Vendas']

# Imprima o DataFrame filtrado
print("\nFuncionários do departamento de Vendas:")
print(vendas_df)

import numpy as np

# Calcule a média da coluna 'Salario' usando numpy.mean()
media_salarial = np.mean(df['Salario'])

# Imprima o resultado
print(f"\nA média salarial de todos os funcionários é: R${media_salarial:.2f}")


# Adicione a nova coluna 'Bonus' ao DataFrame
df['Bonus'] = df['Salario'] * 0.10

# Exiba o DataFrame atualizado com a nova coluna
print("\nDataFrame com a nova coluna 'Bonus':")
print(df)