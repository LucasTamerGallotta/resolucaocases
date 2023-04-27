from mysql.connector import Error
from sqlalchemy import create_engine
import mysql

def conectaBD():
    """ 
    => Função utilizada para criar a conexão no banco de dados MySQL
    :return: Retorna a variável de conexão com o banco
    
    """

    # Passando as informações necessárias para criar a conexão com o MySQL
    conn = mysql.connector.connect(user='root', 
                               database='case',
                               password='minhasenha123',
                               host='localhost')
    return conn


def criaEngine():
    """
    => Função que cria a engine para realizar a conexão ao banco de dados
    :return: Returna a engine que será utilizada para as cargas de dados
    
    """
    # Informações conectar ao Banco de Dados
    host="localhost"
    database='case'
    user='root'
    password='minhasenha123'

    # Criando a engine que será utilizada para conectar ao Banco de Dados
    return create_engine('mysql+mysqlconnector://'+user+':'+password+'@'+host+':3306/'+database+'', echo = False)