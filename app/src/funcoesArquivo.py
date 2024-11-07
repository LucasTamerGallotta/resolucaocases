import pandas as pd
import glob, os
import json
import ingestoes


def setSchema(df:pd.DataFrame) -> pd.DataFrame:
    """
    => Função utilizada para setar um schema para os data frames que são lidos.
    :param df: Pandas Data Frame que foi lido pela função lerArquivos
    :return: Retorna um Pandas Data Frame com o seu schema setado 

    """ 
    return df.astype(dtype= {"ID_MARCA":"int64","MARCA":"object","ID_LINHA":"int64","LINHA":"object","DATA_VENDA":"object","QTD_VENDA":"int64"})



# def bulkUpload(df,file):
#     """ 
#     => Função utilizada para subir os dados brutos na tabela raw_bases do MySQL 
#     :param df: Pandas Data Frame com o schema já setado
#     :param file: Arquivo que está alimentando o Pandas Data Frame atual
#     :return: Sem retorno

#     """
    
#     # Criando a engine que será utilizada para conectar ao Banco de Dados
#     my_engine = funcoesConexao.criaEngine()

#     # Realizando o bulk upload na camada de dados Raw
#     df.to_sql(name = 'raw_bases', con = my_engine, if_exists = 'append', index = False)
#     print(f"Upload do arquivo {file} realizado com sucesso!")


def obterArquivos(directory:str):
    """ 
    => Função utilizada para buscar por todos os arquivos Excel (.xlsx) de um diretório específico
    :param directory: Diretório no qual a busca pelo arquivo Excel será realizada 
    :return: Sem retorno

    """

    # Obtendo todos os arquivos .xlsx
    os.chdir(f"{directory}")
    # Iterando sobre os arquivos encontrados e passando para a função lerArquivos
    for file in glob.glob("*.xlsx"):
        lerArquivos(file)


def lerArquivos(file:str):
    """
    => Função utilizada para ler um arquivo Excel (.xlsx), converter para um Pandas Data Frame,
    setar o seu schema e carregar na camada Raw data
    :param file: Nome do arquivo que será lido via Pandas
    :return: Sem retorno

    """

    # Lendo o arquivo Excel e convertendo para um Pandas Data Frame
    df = pd.read_excel(file)

    # Setando o schema do Pandas Data Frame
    df = setSchema(df)

    # Escrevendo no MySQL
    ingestoes.bulkUpload(df, file)


def populaConsolidados(arqJson:str):
  """
  => Função que lê arquivo JSON que contém as tabelas da camada Trusted e os 
  scripts que serão utilizados para alimentá-las
  :param arqJson: Arquivo JSON que contém as informações para carga:
  :return: Não tem retorno
  
  """
  with open(arqJson) as f:
          querys = json.load(f)
  
  for name, query in querys.items():
          ingestoes.executaQuerysConsolidados(name, query)


