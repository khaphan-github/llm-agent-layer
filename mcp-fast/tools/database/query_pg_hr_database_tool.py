
from core.tool_config import ToolConfig
from utils.pg_database import PGDatabase
from env import *


def query_pg_hr_database_tool(query_string: str, dbname: str):
    if not query_string.strip().lower().startswith("select"):
        return "Only SELECT queries are allowed."
    db = PGDatabase(
        dbname=dbname,
        user=POSTGRES_HR_USER,
        password=POSTGRES_HR_PASSWORD,
        host=POSTGRES_HR_HOST,
        port=POSTGRES_HR_PORT
    )
    print(f"Executing query on {dbname} database: {query_string}")
    return db.execute_query(query_string)


QUERY_PG_HR_DATABASE_TOOL = ToolConfig(
    description="""
    usecase:
        Query the PostgreSQL HR database. 
        Only SELECT queries are allowed.
    rules
        Default should be public schema.
    parameters: 
    - query_string: str: query string to be executed.
    - dbname: str: contain: angular2023, angular2024
    """,
    name="query_pg_hr_database",
    fn=query_pg_hr_database_tool,
)
