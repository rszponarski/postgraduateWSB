import keyring


def save_password(service_name, username, password):
    try:
        keyring.set_password(service_name, username, password)
        print(f"Password for {username} at {service_name} saved successfully.")
    except Exception as e:
        print(f"Error saving password: {e}")


def retrieve_password(service_name, username):
    try:
        password = keyring.get_password(service_name, username)
        if password:
            print(f"Retrieved password for {username} at {service_name}: {password}")
        else:
            print(f"No password found for {username} at {service_name}")
    except Exception as e:
        print(f"Error retrieving password: {e}")


def delete_password(service_name, username):
    try:
        keyring.delete_password(service_name, username)
        print(f"Password for {username} at {service_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting password: {e}")


def main():
    service_name = "example_service"
    username = "example_user"

    while True:
        print("\nKeyring Example Program")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            password = input(f"Enter password for {username} at {service_name}: ")
            save_password(service_name, username, password)
        elif choice == '2':
            retrieve_password(service_name, username)
        elif choice == '3':
            delete_password(service_name, username)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
