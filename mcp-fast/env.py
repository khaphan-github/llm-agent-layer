from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_HR_USER = os.getenv("POSTGRES_HR_USER")
POSTGRES_HR_PASSWORD = os.getenv("POSTGRES_HR_PASSWORD")
POSTGRES_HR_HOST = os.getenv("POSTGRES_HR_HOST")
POSTGRES_HR_PORT = os.getenv("POSTGRES_HR_PORT")
REDIS_CELERY_BROKER = os.getenv("REDIS_CELERY_BROKER")

POSTGRES_AGENT_USER = os.getenv("POSTGRES_AGENT_USER")
POSTGRES_AGENT_PASSWORD = os.getenv("POSTGRES_AGENT_PASSWORD")
POSTGRES_AGENT_DATABASE_NAME = os.getenv("POSTGRES_AGENT_DATABASE_NAME")
POSTGRES_AGENT_HOST = os.getenv("POSTGRES_AGENT_HOST")
POSTGRES_AGENT_PORT = os.getenv("POSTGRES_AGENT_PORT")

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
OPENAI_API_BASE_URL = os.getenv("OPENAI_API_BASE_URL")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")

MCP_SERVER_HOST = os.getenv("MCP_SERVER_HOST")
