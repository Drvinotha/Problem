def generate_greeting(first_name, last_name):
    greeting = f"Hello, {first_name} {last_name}! Welcome."
    return greeting

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    message = generate_greeting(first_name, last_name)
    print(message)

if __name__ == "__main__":
    main()

