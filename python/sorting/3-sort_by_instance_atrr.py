class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"State(name='{self.name}')"

# Simulate the storage system with some sample State objects
storage = {
    1: State(name="California"),
    2: State(name="Texas"),
    3: State(name="Florida")
}

# Retrieve all State objects (simulating storage.all(State).values())
states = list(storage.values())
print("Original order:", states)

# Sort the states by their 'name' attribute
# K is the placeholder for state.
sorted_states = sorted(states, key=lambda k: k.name)

# Display the sorted list of State objects
print("Sorted order:", sorted_states)
