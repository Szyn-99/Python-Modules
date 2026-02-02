def ft_archive_creation() -> None:
    try:
        file_name = "new_discovery.txt"
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print(f"Initializing new storage unit: {file_name}")
        with open(file_name, "w") as new:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            new.write("[ENTRY 001] New quantum algorithm discovered\n")
            new.write("[ENTRY 002] Efficiency increased by 347%\n")
            new.write("[ENTRY 003] Archived by Data Archivist trainee")
        with open(file_name, "r") as archive:
            print(archive.read())
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except Exception:
        raise


if __name__ == "__main__":
    try:
        ft_archive_creation()
    except Exception as e:
        print("Error during operation")
        print(f"Error Details: {e}")
