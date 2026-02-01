def ft_ancient_text(file_name: str):
    try:
        if(not file_name):
            raise
        file = open(file_name)
        return file.read()
    except Exception:
        raise Exception("ERROR: Storage vault not found.")
    
    
if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        file_name = "ancient_fragment.txt"
        lines = ft_ancient_text(file_name)
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(lines)
        print("\nData recovery complete. Storage unit disconnected.")
        
    except Exception as e:
        print(e)