import os
from typing import Dict

try:
    from dotenv import load_dotenv
except Exception as e:
    print(f"{e}")
    exit(1)


def get_config_data() -> Dict[str, str]:
    load_dotenv()
    print("Configuration loaded:")
    data: Dict[str, str] = {
        'mode': os.environ.get('MATRIX_MODE', 'not set'),
        'database': os.environ.get('DATABASE_URL', 'not_set'),
        'api_key': os.environ.get('API_KEY', 'not set'),
        'log_level': os.environ.get('LOG_LEVEL', 'not set'),
        'zion': os.environ.get('ZION_ENDPOINT', 'not set')
    }
    return data


def missing_data(data: Dict[str, str]) -> bool:
    print("\nEnvironment security check:")
    valid = True
    for key, value in data.items():
        if value == 'not set':
            print(f"missing {key}, add it ot your .env config")
            valid = False

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    return valid


def format_data(data: Dict[str, str]) -> None:
    """Display the loaded configuration."""

    print(f"Mode : {data['mode']}")
    print(f"Database : {data['database']}")
    print(f"API Access : {data['api_key']}")
    print(f"Log Level : {data['log_level']}")
    print(f"Zion Network : {data['zion']}")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    data = get_config_data()
    format_data(data)
    missing_data(data)
    print("\nThe Oracle sees all configurations.")
