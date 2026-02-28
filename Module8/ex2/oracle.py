import dotenv
import os

def a_function() -> None:
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        config = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT']
        a_dict = {}
        err = 0
        hardcoded = 0
        for c in config:
            token = os.getenv(c)
            if token:
                a_dict.update({c:token})
            else:
                print(f"Missing configuration: {c}")
                err = 1337
        print("\nConfiguration loaded:")
        print(f"Mode: {a_dict.get('MATRIX_MODE')}")
        print(f"Database: {a_dict.get('DATABASE_URL')}")
        print(f"API Access: {a_dict.get('API_KEY')}")
        print(f"Log Level: {a_dict.get('LOG_LEVEL')}")
        print(f"Zion Network: {a_dict.get('ZION_ENDPOINT')}")

        print("\nEnvironment security check:")
        for val in globals():
            if val.upper() in config:
                print("[KO] hardcoded secrets detected")
                hardcoded = 1
                break
        if hardcoded == 0:
            print("[OK] No hardcoded secrets detected")
        if err == 0:
            print("[OK] .env file properly configured")
        else:
            print("[KO] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(f"Erro: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    a_function()