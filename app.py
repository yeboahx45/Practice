"""This application asks users for their voter registration details and verifies
their eligibility to vote. It shows a summary of the user's details and thanks
them for registering if they are eligible to vote. If a user is not eligible to vote,
the program tells them why they cannot vote."""

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 120

def is_valid_state(state):
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    return state.upper() in states
What is an “organization” in reference to GitHub?
    """Ask the user if they want to continue with the registration."""
    while True:
        response = prompt_for_input(
            "Do you want to continue with the voter registration? (Yes/No): "
        ).strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("Please respond with 'Yes' or 'No'.")

def is_valid_citizen(citizen):
    """Check if the response indicates U.S. citizenship."""
    return citizen.lower() in ["yes", "no"]

def get_validated_input(prompt, validation_func, error_msg):
    """Prompt for input until valid according to the given validation function."""
    while True:
        user_input = prompt_for_input(prompt)
        if validation_func(user_input):
            return user_input
        print(error_msg)

def main():
    """Main function to run the voter registration application."""
    print("Welcome to the Python Voter Registration Application.")

    if not continue_registration():
        return

    first_name = get_validated_input("What is your first name? ", bool,
                                     "Please enter your first name.")

    if not continue_registration():
        return

    last_name = get_validated_input("What is your last name? ", bool,
                                    "Please enter your last name.")

    if not continue_registration():
        return

    age = get_validated_input("What is your age? ", is_valid_age,
                              "Please enter a valid age (0-120).")

    if int(age) < 18:
        print("You must be at least 18 years old to register.")
        return

    citizen = get_validated_input("Are you a U.S. Citizen? (Yes/No): ", is_valid_citizen,
                                  "Please respond with 'Yes' or 'No'.")

    if citizen.lower() == "no":
        print("You must be a U.S. citizen to register.")
        return

    if not continue_registration():
        return

    state_of_residence = get_validated_input("What state do you live? ", is_valid_state,
                    "Please enter a valid U.S. state abbreviation (e.g., 'CA' for California).")

    zipcode = prompt_for_input("What is your zipcode? ")

    print("\nThanks for registering to vote. Here is the information we received:")
    print(f"Name (first last): {first_name} {last_name}")
    print(f"Age: {age}")
    print(f"U.S. Citizen: {citizen.capitalize()}")
    print(f"State: {state_of_residence}")
    print(f"Zipcode: {zipcode}")
    print("Thanks for trying the Voter Registration Application. "
          "Your voter registration card should be shipped within 3 weeks.")

if __name__ == "__main__":
    main()
