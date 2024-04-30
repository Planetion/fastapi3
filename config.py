from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=5432
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")  

DB_NAME_TEST=os.environ.get("DB_NAME_TEST")
DB_USER_TEST=os.environ.get("DB_USER_TEST")
DB_PASS_TEST=os.environ.get("DB_PASS_TEST")
DB_PORT_TEST=5432
DB_HOST_TEST=os.environ.get("DB_HOST_TEST")
