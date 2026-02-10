def ft_ancient_text(file_name: str) -> str:
    file = None
    try:
        file = open(file_name)
        lines = file.read()
        return lines
    except Exception:
        raise Exception("ERROR: Storage vault not found.")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        file_name = "ancient_fragment.txt"
        lines = ft_ancient_text(file_name)
        print(f"\nAccessing Storage Vault: {file_name}")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(lines)
        print("\nData recovery complete. Storage unit disconnected.")

    except Exception as e:
        print(e)
