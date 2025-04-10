from datetime import datetime, timedelta
from utils.pg_database import PGDatabase
from env import *

# Initialize the database connection
db = PGDatabase(
  dbname=POSTGRES_AGENT_DATABASE_NAME,
  user=POSTGRES_AGENT_USER,
  password=POSTGRES_AGENT_PASSWORD,
  host=POSTGRES_AGENT_HOST,
  port=POSTGRES_AGENT_PORT
)

# Migration function to create the table


def create_agent_scheduler_task_table():
    query = """
    CREATE TABLE IF NOT EXISTS agent_scheduler_task (
        task_id UUID PRIMARY KEY,
        task_name TEXT,
        task_status TEXT,
        task_result TEXT,
        task_start_time TIMESTAMP,
        task_end_time TIMESTAMP,
        task_duration INT,
        task_error TEXT,
        task_params TEXT,
        task_tool TEXT,
        next_run_id TEXT
    );
    """
    db.execute_query(query)

# Function to get a task by task_id


def get_task_by_id(task_id):
    query = "SELECT * FROM agent_scheduler_task WHERE task_id = %s;"
    return db.execute_query(query, (task_id,))

# Function to get all tasks with start time > now + 2 minutes


def get_tasks_starting_soon(minutes=2):
    query = """
    SELECT * FROM agent_scheduler_task
    WHERE task_start_time > %s;
    """
    future_time = datetime.now() + timedelta(minutes=minutes)
    return db.execute_query(query, (future_time,))

# Function to update a task by task_id


def update_task_by_id(task_id, updates):
    set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
    query = f"""
    UPDATE agent_scheduler_task
    SET {set_clause}
    WHERE task_id = %s;
    """
    params = list(updates.values()) + [task_id]
    db.execute_query(query, params)
