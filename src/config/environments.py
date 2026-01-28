import os
from dotenv import load_dotenv


load_dotenv()


PORT = int(os.getenv("PORT"))
if not PORT:
    raise RuntimeError("PORT is missing in the .env file")


ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")
if not ALLOWED_ORIGINS:
    raise RuntimeError("Allowed origins variable is missing in the .env file")