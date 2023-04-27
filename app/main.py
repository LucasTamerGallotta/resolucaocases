# Importando as bibliotecas necessárias

import pandas as pd
from mysql.connector import Error
from sqlalchemy import create_engine
import mysql
import funcoesArquivo
import criaTabelas


if __name__ == "__main__":
    
    #STEP 1 CRIAR A TABELA DE RAW DATA
    # Criando a tabela que irá conter o raw data
    criaTabelas.criarRawTable()
    
    # STEP 2
    # Definindo o diretório onde irá ocorrer a busca do .xlsx
    
    directory = "C:\\Users\\lucas\\OneDrive\\Documentos\\resolucaocases\\sources"
    funcoesArquivo.obterArquivos(directory)

    #STEP 3
    # Criando as tabelas que contém os dados das vendas consolidades
    criaTabelas.CriaTabelasVendasConsolidadas('wrk_consolidado_tbl1','wrk_consolidado_tbl2','wrk_consolidado_tbl3','wrk_consolidado_tbl4')

    # STEP 4
    # Populando as tabelas Trusted com os dados das vendas consolidadas
    funcoesArquivo.populaConsolidados('\\queries.json')
