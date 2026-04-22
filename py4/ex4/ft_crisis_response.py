def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", 'r') as f:
            result = f.read()
            print(f"{result}\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", 'r') as f:
            result = f.read()
            print(result)
    except Exception:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    try:
        print("ROUTINE ACCESS: Attempting access to "
              "'standard_archive.txt'...")
        with open("standard_archive.txt", 'r') as f:
            result = f.read()
            print(f"SUCCESS: Archive recovered - {result}")
            print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(e)
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
