import os

from dotenv import load_dotenv

base_file_path = os.path.dirname(__file__)
data_folder = os.path.join(base_file_path, "data")

load_dotenv(os.path.abspath(os.path.join(base_file_path, "..", "..", "..", ".env")))

DATABASE_URI = os.getenv("DATABASE_URL") or "postgresql://postgres:postgres@localhost:5432/lummerland"

if DATABASE_URI and DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)
