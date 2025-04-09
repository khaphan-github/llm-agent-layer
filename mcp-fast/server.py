"""
A FastMCP server that provides tools for calculating dimensions based on aspect ratios
and retrieving the current time. This server specifically handles 16:9 aspect ratio calculations.
"""
import os
from mcp.server.fastmcp import FastMCP
from utils.pg_database import PGDatabase

mcp = FastMCP("my-mcp-ratio-server")


@mcp.tool()
def query_data_basse(query_string: str, dbname: str):
    """
    Executes a SELECT query on the specified PostgreSQL database.
    Ensures that only SELECT queries are allowed for security reasons.

    Args:
      query_string (str): The SQL query string to execute. Must be a SELECT query.
      dbname (str): The name of the PostgreSQL database to connect to.

    Returns:
      Any: The result of the SELECT query execution.

    Raises:
      ValueError: If the query is not a SELECT query.
    """
    if not query_string.strip().lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    db = PGDatabase(
        dbname=dbname,
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", ""),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )
    return db.execute_query(query_string)


if __name__ == "__main__":
    mcp.run(transport='sse')
