import pandas as pd
import funcoesConexao

def bulkUpload(df,file):
    """ 
    => Função utilizada para subir os dados brutos na tabela raw_bases do MySQL 
    :param df: Pandas Data Frame com o schema já setado
    :param file: Arquivo que está alimentando o Pandas Data Frame atual
    :return: Sem retorno

    """
    
    # Criando a engine que será utilizada para conectar ao Banco de Dados
    my_engine = funcoesConexao.criaEngine()

    # Realizando o bulk upload na camada de dados Raw
    df.to_sql(name = 'raw_bases', con = my_engine, if_exists = 'append', index = False)
    print(f"Upload do arquivo {file} realizado com sucesso!")


def executaQuerysConsolidados(name,query):
        """ 
        => Função utilizada para realizar a ingestão dos dados na camada Trusted, a partir
        da camada Raw.
        :param name: Nome da tabela onde irá realizar a ingestão 
        :param query: A query que será utilizada para realizar a ingestão
        """

        # Criando a engine que será utilizada para conectar ao Banco de Dados
        my_engine = funcoesConexao.criaEngine()

        # Establish a connection
        conn = funcoesConexao.conectaBD()

        query = query

        # Create a pandas dataframe
        df = pd.read_sql(query, con=conn)

        # Fechando a conexão com o BD
        conn.close()

        # Populando as tabelas Trusted com os dados filtrados
        df.to_sql(name = name, con = my_engine, if_exists = 'append', index = False)