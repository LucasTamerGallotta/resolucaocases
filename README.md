# Resoluções Case 2
Diretório airflow-docker
- docker-compose.yaml = Contém script utilizado para subir o Docker do Airflow e MySQL 

Diretório app
/configs
- conexao.json = JSON com informações necessárias para conexão com o Banco de Dados
/src
- criaTabelas.py = Script contendo a criação as tabelas da camada Raw e Trusted;
- funcoesArquivo.py =  Script contendo todas as funções utilizadas para manipulação de arquivos
- funcoesConexao.py = Script contendo todas as funções para a conexão com o banco MySQL
- ingestoes.py = Script contendo as ingestões de dados para a camada Raw e Trusted
- main.py =  Script contendo a chamada de todas as funções necessárias para a resolução do Case 2

Diretório query
- queries.json = Contém as tabelas dos dados consolidados e suas respectivas queries que as populam

Diretório sources
- Contém arquivos Excel utilizados como base para ingestão na camada Raw
