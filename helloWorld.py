# This creates a function (a reusable piece of code) called "greet"
# It takes one piece of information: a person's name
def greet(name):
    # This returns (gives back) a greeting message
    # The f before the quote makes it a "formatted string" - it lets us insert the name directly into the text
    # Whatever is in {name} gets replaced with the actual name
    return f"Hello, {name}!"

# This is a special check that runs the code below ONLY when you run this file directly
# (not when you import it into another program)
if __name__ == "__main__":
    # Ask the user to type their name and store their answer in user_name
    user_name = input("What's your name? ")
    
    # Check if the user actually typed something (not just empty spaces)
    # .strip() removes any extra spaces from the beginning and end
    if user_name.strip():
        # If they entered a name, use our greet function and display the result
        print(greet(user_name))
    else:
        # If they didn't enter anything (just hit Enter or typed only spaces)
        # Display a default message
        print("Hello, stranger!")
