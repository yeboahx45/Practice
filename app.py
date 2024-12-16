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
