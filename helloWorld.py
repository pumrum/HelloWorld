def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("What's your name? ")
    if user_name.strip():
        print(greet(user_name))
    else:
        print("Hello, stranger!")
