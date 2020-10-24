from utils.constants import (
    DATABASE_CONFIG,
    DATABASE_CONFIG_SYSTEM,
    DATABASE_CONFIG_SENSOR
)
import os


def load_database_params():
    port = os.getenv("DB_PORT", DATABASE_CONFIG["DB_PORT"])
    port = int(port)

    params = {
        "host": os.getenv("DB_HOST", DATABASE_CONFIG["DB_HOST"]),
        "port": port,
        "username": os.getenv("DB_USERNAME", DATABASE_CONFIG["DB_USERNAME"]),
        "password": os.getenv("DB_PASSWORD", DATABASE_CONFIG["DB_PASSWORD"]),
        "authSource": os.getenv("authSource", DATABASE_CONFIG["authSource"]),
        "authMechanism": os.getenv(
            "authMechanism",
            DATABASE_CONFIG["authMechanism"]
        )
    }

    return params

def load_database_system_params():
    port = os.getenv("DB_PORT", DATABASE_CONFIG_SYSTEM["DB_PORT"])
    port = int(port)

    system_params = {
        "host": os.getenv("DB_HOST", DATABASE_CONFIG_SYSTEM["DB_HOST"]),
        "port": port,
        "username": os.getenv("DB_USERNAME",
                              DATABASE_CONFIG_SYSTEM["DB_USERNAME"]),
        "password": os.getenv("DB_PASSWORD",
                              DATABASE_CONFIG_SYSTEM["DB_PASSWORD"]),
        "authSource": os.getenv("authSource",
                                DATABASE_CONFIG_SYSTEM["authSource"]),
        "authMechanism": os.getenv(
            "authMechanism",
            DATABASE_CONFIG_SYSTEM["authMechanism"]
        )
    }

    return system_params

def load_database_sensor_params():
    port = os.getenv("DB_PORT", DATABASE_CONFIG_SENSOR["DB_PORT"])
    port = int(port)

    sensor_params = {
        "host": os.getenv("DB_HOST", DATABASE_CONFIG_SENSOR["DB_HOST"]),
        "port": port,
        "username": os.getenv("DB_USERNAME",
                              DATABASE_CONFIG_SENSOR["DB_USERNAME"]),
        "password": os.getenv("DB_PASSWORD",
                              DATABASE_CONFIG_SENSOR["DB_PASSWORD"]),
        "authSource": os.getenv("authSource",
                                DATABASE_CONFIG_SENSOR["authSource"]),
        "authMechanism": os.getenv(
            "authMechanism",
            DATABASE_CONFIG_SENSOR["authMechanism"]
        )
    }

    return sensor_params
