from sqlalchemy import create_engine, text
from typing import Dict, List, Optional, Any


def connect_to_postgres(host: str, port: int, dbname: str, user: str, password: str) -> Dict[str, Any]:
    """
    Establish a connection to a PostgreSQL database.

    Args:
        host (str): The PostgreSQL server host
        port (int): The PostgreSQL server port
        dbname (str): The database name
        user (str): The username for authentication
        password (str): The password for authentication

    Returns:
        Dict[str, Any]: Connection status and information
    """
    try:
        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        engine = create_engine(connection_string)
        conn = engine.connect()
        conn.close()
        return {"status": "success", "message": f"Successfully connected to PostgreSQL database {dbname}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to connect to PostgreSQL: {str(e)}"}


def execute_query(host: str, port: int, dbname: str, user: str, password: str,
                  query: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Execute a SQL query on a PostgreSQL database and return the results.

    Args:
        host (str): The PostgreSQL server host
        port (int): The PostgreSQL server port
        dbname (str): The database name
        user (str): The username for authentication
        password (str): The password for authentication
        query (str): The SQL query to execute
        params (Optional[Dict[str, Any]]): Parameters to use with the query

    Returns:
        Dict[str, Any]: Query results or error information
    """
    try:
        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        engine = create_engine(connection_string)

        with engine.connect() as conn:
            if params:
                result = conn.execute(text(query), params)
            else:
                result = conn.execute(text(query))

            if result.returns_rows:
                rows = [dict(row._mapping) for row in result]
                return {"status": "success", "rows": rows, "rowCount": len(rows)}
            else:
                return {"status": "success", "rowCount": result.rowcount, "message": "Query executed successfully"}

    except Exception as e:
        return {"status": "error", "message": f"Query execution failed: {str(e)}"}


def create_table(host: str, port: int, dbname: str, user: str, password: str,
                 table_name: str, columns: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Create a new table in a PostgreSQL database.

    Args:
        host (str): The PostgreSQL server host
        port (int): The PostgreSQL server port
        dbname (str): The database name
        user (str): The username for authentication
        password (str): The password for authentication
        table_name (str): Name of the table to create
        columns (List[Dict[str, str]]): List of column definitions with 'name' and 'type' keys

    Returns:
        Dict[str, Any]: Status of the table creation operation
    """
    try:
        # Build the CREATE TABLE statement
        column_defs = []
        for col in columns:
            column_defs.append(f"{col['name']} {col['type']}")

        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"

        # Execute the query
        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        engine = create_engine(connection_string)

        with engine.connect() as conn:
            conn.execute(text(create_table_sql))
            conn.commit()

        return {"status": "success", "message": f"Table {table_name} created successfully"}

    except Exception as e:
        return {"status": "error", "message": f"Failed to create table: {str(e)}"}
