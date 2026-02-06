def ft_crisis_response(file_name, mode) -> None:
    try:
        with open(file_name, mode) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            content = f.read()
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system stable")
    except Exception as e:
        print("Chaos in the Matrix")
        print(f"Crisis Details: {e}")


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
        file_name = "lost_archive.txt"
        mode = "r"
        ft_crisis_response(file_name, mode)
        print()
        file_name = "classified_vault.txt"
        mode = "r"
        ft_crisis_response(file_name, mode)
        print()
        file_name = "standard_archive.txt"
        mode = "r"
        ft_crisis_response(file_name, mode)
    except Exception as e:
        print(f"Unhandled Error: {e}")
