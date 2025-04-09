"""
A FastMCP server that provides tools for calculating dimensions based on aspect ratios
and retrieving the current time. This server specifically handles 16:9 aspect ratio calculations.
"""
import os
from mcp.server.fastmcp import FastMCP
from utils.pg_database import PGDatabase

mcp = FastMCP("my-mcp-ratio-server",
              instructions='''
# You are an AI agent. You need to:
- When the user asks to query a database, use the `query_data_basse` tool defined in `/workspaces/llm-agent-layer/mcp-fast/server.py`. Ensure the query is a SELECT query and provide the database name as required.
- Ensure the tool is used securely and only for SELECT queries, as per the implementation.
- Follow the existing tools and utilities provided in the environment for database operations.
''')


@mcp.tool()
def query_data_basse(query_string: str, dbname: str):
    """
    This tool help query database to get info
    Executes a SELECT query on the specified PostgreSQL database.
    Ensures that only SELECT queries are allowed for security reasons.

    Args:
      query_string (str): The SQL query string to execute. Must be a SELECT query.
      dbname (str): The name of the PostgreSQL database to connect to.

    Returns:
      Any: The result of the SELECT query execution.

    Raises:
      ValueError: If the query is not a SELECT query.

    Example:
      >>> result = query_data_basse("SELECT * FROM users;", "my_database")
      >>> print(result)
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
