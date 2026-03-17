import os
from dotenv import load_dotenv

def load_env(env_name="dev"):
    env_file = f".env.{env_name}"

    if not os.path.exists(env_file):
        raise Exception(f"Arquivo {env_file} não encontrado")

    load_dotenv(env_file)

    base_url = os.getenv("BASE_URL")

    if not base_url:
        raise Exception("BASE_URL não definida no .env")

    return {
        "BASE_URL": base_url
    }