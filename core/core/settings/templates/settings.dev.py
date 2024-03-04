# local settings sits here
#  such as logging
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = str(os.getenv("SECRET_KEY"))

# region Customize DB Data

DB_NAME = ""
DB_HOST = ""
DB_USER = ""
DB_PASSWORD = ""

# endregion
