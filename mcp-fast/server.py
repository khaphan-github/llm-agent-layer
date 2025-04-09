"""
A FastMCP server that provides tools for calculating dimensions based on aspect ratios
and retrieving the current time. This server specifically handles 16:9 aspect ratio calculations.
"""

from utils.postgresqls_connector import connect_to_postgres, execute_query, create_table
from fastmcp import FastMCP

mcp = FastMCP("my-mcp-ratio-server",
              dependencies=["psycopg2", "psycopg2-binary", "sqlalchemy"])

if __name__ == "__main__":
    mcp.run(transport='sse')
