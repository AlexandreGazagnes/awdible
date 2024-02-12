"""
Configurations for the app
"""

import os
import dotenv
from dotenv import dotenv_values

from .logger import logger


def get_config():
    """Get the config"""

    no_api_key = "No API Key sush as 'RAPID_API_KEY' found in the environment variables or in .env file"
    no_host_key = "No API Host as 'RAPID_API_HOST' found in the environment variables or in .env file"

    # Search for the API Key and Host in the environment variables
    env_key = os.getenv("RAPID_API_KEY", no_api_key)
    env_host = os.getenv("RAPID_API_HOST", no_host_key)

    if os.path.exists(".env/.env.prod"):
        values = dotenv_values(".env/.env.prod")
    elif os.path.exists(".env"):
        values = dotenv_values(".env")
    else:
        values = {}

    config = {
        "X-RapidAPI-Key": values.get("RAPID_API_KEY", env_key),
        "X-RapidAPI-Host": values.get("RAPID_API_HOST", env_host),
    }

    logger.critical(f"Config: {config.get('X-RapidAPI-Host', no_host_key)}")

    return config


config = get_config()
