-- Cria as tabelas 'clientes' e 'clientes_raw' para armazenar os dados

CREATE TABLE clientes
INSERT INTO clientes


CREATE TABLE clientes_raw
INSERT INTO clientes_raw

-- Identifica e conta registros duplicados usando GROUP BY e HAVING
SELECT nome, email, cidade, COUNT(*) AS total
FROM clientes GROUP BY
nome, email, cidade
HAVING
COUNT(*)>l;

-- Atribui um número de linha a cada registro dentro de partições, permitindo a identificação de duplicatas
SELECT
*
ROW_NUMBER() OVER (
PARTITION BY nome, email, cidade
ORDER BY id
) AS row_num
FROM
clientes;

-- Usa uma CTE (Common Table Expression) com ROW_NUMBER() para selecionar apenas a primeira ocorrência de cada registro único
WITH duplicatas AS (SELECT *,
ROW_NUMBER() OVER (
PARTITION BY nome, email, cidade
ORDER BY id
) AS row_num
FROM
clientes
) SELECT id, nome, email, cidade FROM duplicatas WHERE row_num = 1;

-- Concatena campos para criar uma chave de correspondência e identificar duplicatas
SELECT *,
CONCAT(nome, '_', cpf, '_', email) AS match_key,
ROW_NUMBER() OVER (
PARTITION BY nome, cpf, email
ORDER BY data_cadastro DESC
) AS row_num
FROM clientes;

-- Remove espaços em branco e padroniza o uso de maiúsculas/minúsculas
SELECT
nome AS nome_original,
UPPER(TRIM(nome)) AS nome_limpo,
email AS email_original,
LOWER(TRIM(email)) AS email_padronizado
FROM clientes_raw;

-- Remove caracteres indesejados (parênteses, traços, espaços) de uma string usando a função REPLACE
SELECT telefone AS original,
REPLACE(
REPLACE(
REPLACE(
REPLACE(telefone, '(', ''),
')', ''),
'-', ''),
' ', '') AS telefone_limpo
FROM clientes_raw;

-- Converte um campo de texto em data usando CAST, verificando o formato com CASE
SELECT data_nascimento AS original,
CASE
WHEN data_nascimento LIKE '____-__-__' THEN CAST(data_nascimento AS
DATE)
ELSE NULL
END AS data_convertida
FROM clientes_raw;

-- Lida com valores nulos usando NULLIF e COALESCE, substituindo valores específicos ou preenchendo com um valor padrão
SELECT
status AS original,
NULLIF(status, 'N/A') AS nullif_aplicado,
COALESCE(status, 'INDEFINIDO') AS status_preenchido
FROM clientes_raw;

-- Combina todas as técnicas de limpeza em uma única consulta para padronizar múltiplos campos
SELECT id,
LOWER(TRIM(nome)) AS nome,
REPLACE(REPLACE(REPLACE(telefone, '(', ''), ')', ''), '-', '') AS telefone,
CASE
WHEN data_nascimento LIKE '____-__-__' THEN CAST(data_nascimento AS DATE)
ELSE NULL
END AS data_nascimento,
LOWER(TRIM(email)) AS email,
COALESCE(status, 'INDEFINIDO') AS status
FROM clientes_raw;