# This creates a function (a reusable piece of code) called "greet"
# It takes two pieces of information: a person's first name and last name
def greet(first_name, last_name):
    # This returns (gives back) a greeting message
    # The f before the quote makes it a "formatted string" - it lets us insert the names directly into the text
    # Whatever is in {first_name} and {last_name} gets replaced with the actual names
    return f"Hello, {first_name} {last_name}!"

# This is a special check that runs the code below ONLY when you run this file directly
# (not when you import it into another program)
if __name__ == "__main__":
    # Ask the user to type their first name and store their answer in first_name
    first_name = input("What's your first name? ")

    # Ask the user to type their last name and store their answer in last_name
    last_name = input("What's your last name? ")

    # Check if both names were provided (not just empty spaces)
    # .strip() removes any extra spaces from the beginning and end
    if first_name.strip() and last_name.strip():
        # If they entered both names, use our greet function and display the result
        print(greet(first_name, last_name))
    else:
        # If they didn't enter both names (missing one or both)
        # Display an error message
        print("Error: Both first name and last name are required!")
