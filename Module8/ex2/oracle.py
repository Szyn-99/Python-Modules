import os
import dotenv


def a_function(over_ride: bool) -> None:
    try:
        """Load and validate environment variables,
        checking for missing or hardcoded secrets."""

        print("\nORACLE STATUS: Reading the Matrix...\n")
        config = [
            'MATRIX_MODE', 'DATABASE_URL',
            'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT',
        ]
        a_dict = {}
        err = False
        hardcoded = False
        for c in config:
            token = os.getenv(c)
            if token:
                a_dict.update({c: token})
            else:
                print(f"Missing configuration: {c}")
                err = True
        print("\nConfiguration loaded:")
        print(f"Mode: {a_dict.get('MATRIX_MODE')}")
        print(f"Database: {a_dict.get('DATABASE_URL')}")
        print(f"API Access: {a_dict.get('API_KEY')}")
        print(f"Log Level: {a_dict.get('LOG_LEVEL')}")
        print(f"Zion Network: {a_dict.get('ZION_ENDPOINT')}")

        print("\nEnvironment security check:")
        check = {**globals(), **locals()}
        for val in check:
            if val.upper() in config:
                print("[KO] hardcoded secrets detected")
                hardcoded = True
                break
        if not hardcoded:
            print("[OK] No hardcoded secrets detected")
        if not err:
            print("[OK] .env file properly configured")
        else:
            print("[KO] .env file properly configured")
        if over_ride:
            print("[OK] Production overrides available")
        else:
            print("[KO] Production overrides unavailable")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(f"Erro: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    over_ride = True
    dotenv.load_dotenv(override=over_ride)
    a_function(over_ride)
