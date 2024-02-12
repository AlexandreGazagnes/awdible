import dotenv


from dotenv import dotenv_values


def get_config():
    return dotenv_values(".env/.env.prod")


config = get_config()
