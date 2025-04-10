from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Access the environment variables
POSTGRES_HR_USER = os.getenv("POSTGRES_HR_USER")
POSTGRES_HR_PASSWORD = os.getenv("POSTGRES_HR_PASSWORD")
POSTGRES_HR_HOST = os.getenv("POSTGRES_HR_HOST")
POSTGRES_HR_PORT = os.getenv("POSTGRES_HR_PORT")

# Example: Print the variables (optional, for debugging purposes)
print(f"POSTGRES_HR_USER: {POSTGRES_HR_USER}")
print(f"POSTGRES_HR_PASSWORD: {POSTGRES_HR_PASSWORD}")
print(f"POSTGRES_HR_HOST: {POSTGRES_HR_HOST}")
print(f"POSTGRES_HR_PORT: {POSTGRES_HR_PORT}")
