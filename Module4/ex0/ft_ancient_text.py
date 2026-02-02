def ft_ancient_text(file_name: str):
    try:
        if not file_name:
            raise
        with open(file_name) as file:
            return file.read()
    except Exception:
        raise Exception("ERROR: Storage vault not found.")


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
