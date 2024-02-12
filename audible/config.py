import os
import dotenv
from dotenv import dotenv_values


def get_config():
    """Get the config"""

    no_api_key = "No API Key Found sush as 'X-RapidAPI-Key' found in the environment variables or in .env file"
    no_host_key = "No API Host Found as 'X-RapidAPI-Host' found in the environment variables or in .env file"

    env_key = os.getenv("X-RapidAPI-Key", no_api_key)
    env_host = os.getenv("X-RapidAPI-Host", no_host_key)

    if os.path.exists(".env/.env.prod"):
        values = dotenv_values(".env/.env.prod")
    elif os.path.exists(".env"):
        values = dotenv_values(".env")

    config = {
        "X-RapidAPI-Key": values.get("X-RapidAPI-Key", env_key),
        "X-RapidAPI-Host": values.get("X-RapidAPI-Host", env_host),
    }

    return config


config = get_config()
