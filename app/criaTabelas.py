import funcoesConexao

def criarRawTable():
  """ 
  => Função utilizada para criar a tabela raw_bases da camada Raw, que contém os dados brutos de todos
  os arquivos Excel.
  :return: Sem retorno
  
  """

  # Conectando ao Banco de Dados
  conn = funcoesConexao.conectaBD()

  # Criando o cursor
  cursor = conn.cursor()
  
  # Setando o script de criação da tabela raw_bases
  queryCreate = """CREATE TABLE IF NOT EXISTS `raw_bases` (
    `ID_MARCA` int NOT NULL,
    `MARCA` varchar(255) NOT NULL,
    `ID_LINHA` int NOT NULL,
    `LINHA` varchar(255) NOT NULL,
    `DATA_VENDA` varchar(255) NOT NULL,
    `QTD_VENDA` int NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
  
  # Executando o script que foi setado
  cursor.execute(queryCreate)
  
  # Fecheando a conexão com o Banco de Dados
  conn.close()

def CriaTabelasVendasConsolidadas(table_name,table_name2,table_name3,table_name4):
    """ 
    => Função utilizada para criar as tabelas da camada Trusted, que contém os dados filtrados 
    a partir da tabela raw_bases
    :param table_name: Informando o nome da primeira tabela
    :param table_name2: Informando o nome da quarta tabela
    :param table_name3: Informando o nome da terceira tabela
    :param table_name4: Informando o nome da quarta tabela 
    :return: Sem retorno
    
    """

    # Conectando ao Banco de Dados
    conn = funcoesConexao.conectaBD()

    # Criando o cursor
    cursor = conn.cursor()


    # Setando e executando os scripts de criação das tabelas Trusted
    queryCreate = f"""CREATE TABLE IF NOT EXISTS `{table_name}` (
        `ANO` varchar(255) NOT NULL,
        `MES` varchar(255) NOT NULL,
        `QTD_VENDA` int NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""

    cursor.execute(queryCreate)

    queryCreate2 = f"""CREATE TABLE IF NOT EXISTS `{table_name2}` (
        `MARCA` varchar(255) NOT NULL,
        `LINHA` varchar(255) NOT NULL,
        `QTD_VENDA` int NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""

    cursor.execute(queryCreate2)

    queryCreate3 = f"""CREATE TABLE  IF NOT EXISTS `{table_name3}` (
        `MARCA` varchar(255) NOT NULL,
        `ANO` varchar(255) NOT NULL,
        `MES` varchar(255) NOT NULL,
        `QTD_VENDA` int NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""

    cursor.execute(queryCreate3)

    queryCreate4 = f"""CREATE TABLE IF NOT EXISTS `{table_name4}` (
        `LINHA` varchar(255) NOT NULL,
        `ANO` varchar(255) NOT NULL,
        `MES` varchar(255) NOT NULL,
        `QTD_VENDA` int NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""

    cursor.execute(queryCreate4)

    # Fecheando a conexão com o Banco de Dados
    conn.close()