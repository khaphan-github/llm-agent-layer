from utils.postgresqls_connector import connect_to_postgres, execute_query, create_table
from server import mcp

POSTGRES_CONFIG = {
    "host": "103.63.115.22",
    "port": 5432,
    "dbname": None,  # Database name will be provided as input
    "user": "postgres",
    "password": "hutechtest@123qwe.."
}


@mcp.tool
def test_postgres_connection(dbname: str):
    """
    Tests the connection to a PostgreSQL database using the provided database name.

    This function updates the global POSTGRES_CONFIG dictionary with the given
    database name and attempts to establish a connection to the PostgreSQL
    database using the configuration parameters.

    Args:
      dbname (str): The name of the PostgreSQL database to connect to.

    Returns:
      Any: The result of the `connect_to_postgres` function, which typically
      represents the connection object or an error if the connection fails.

    Raises:
      Any exceptions raised by the `connect_to_postgres` function if the
      connection cannot be established.
    """
    POSTGRES_CONFIG["dbname"] = dbname  # Set the database name from input
    return connect_to_postgres(
        host=POSTGRES_CONFIG["host"],
        port=POSTGRES_CONFIG["port"],
        dbname=POSTGRES_CONFIG["dbname"],
        user=POSTGRES_CONFIG["user"],
        password=POSTGRES_CONFIG["password"]
    )
