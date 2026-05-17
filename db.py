import oracledb
import pandas as pd

def get_connection():
    """
        estabelece a conexão com o banco de dados Oracle usando as credenciais fornecidas
    """
    connection = oracledb.connect(
        user="RM570379",
        password="300484",
        dsn="oracle.fiap.com.br:1521/ORCL"
    )
    return connection

def get_data():
    """
        executa uma consulta SQL para obter os dados.
    """
    connection = get_connection()
    query = "SELECT * FROM FARM_DATA"
    df = pd.read_sql(query, con=connection)
    connection.close()
    return df