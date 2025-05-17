class State:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt
        self.transitions = {}

    def add_transition(self, input_text, next_state):
        self.transitions[input_text.lower()] = next_state

    def get_next_state(self, input_text):
        return self.transitions.get(input_text.lower())

# States
welcome = State("welcome", "Welcome to Barbeque Nation! Type 'book' to make a reservation.")
booking = State("booking", "Please provide your city (Delhi/Bangalore).")
confirmation = State("confirmation", "Booking confirmed. Type 'exit' to end.")

# Transitions
welcome.add_transition("book", booking)
booking.add_transition("delhi", confirmation)
booking.add_transition("bangalore", confirmation)

# Simple Flow
current = welcome
while True:
    print(current.prompt)
    user_input = input("You: ")
    next_state = current.get_next_state(user_input)
    if next_state:
        current = next_state
    elif user_input.lower() == "exit":
        print("Goodbye!")
        break
    else:
        print("Sorry, I didn’t understand that.")
