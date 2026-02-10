def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    file_name = "classified_data.txt"
    file_name_2 = "security_protocols.txt"
    with open(file_name, "r") as file:
        print("SECURE EXTRACTION:")
        print(file.read())
    with open(file_name_2, "w") as file_2:
        print("\nSECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")
        file_2.write("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        ft_vault_security()
    except Exception as e:
        print("Error during operation")
        print(f"Error Details: {e}")
