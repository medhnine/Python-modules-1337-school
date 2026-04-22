def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    try:
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", 'r') as f:
            result = f.read()
            print(f"{result}\n")
        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", 'r') as f:
            result = f.read()
            print(result)
        print("Vault automatically sealed upon completion\n")
    except Exception as e:
        print(e)
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
