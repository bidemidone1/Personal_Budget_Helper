def budget_remaining(budget, food, transport):
    """Calculates the remaining budget after subtracting food and transport expenses."""
    return budget - food - transport


def budget_message(name, remaining):
    """Returns a formatted status message with the name and remaining amount."""
    return f"{name} has {remaining} naira remaining."


# --- Testing and Verification ---

# Normal case

remaining = budget_remaining(2000, 900, 600)
print(remaining)

message = budget_message("Ada", remaining)
print(message)


# Zero case

remaining = budget_remaining(1500, 0, 0)
print(remaining)

message = budget_message("Ada", remaining)
print(message)


# Overspend case

remaining = budget_remaining(1000, 800, 500)
print(remaining)

message = budget_message("Ada", remaining)
print(message)


# Reflection


"""
Short Reflection

1. What part of the mission was easiest for you?
Implementing the budget_remaining function was the easiest part, as it was a straightforward arithmetic operation subtracting food and transport costs from the initial budget.

2. What test exposed a mistake or gave you confidence that your code was correct?
The overspend test case (budget of 1000, food 800, transport 500, gave an error) then I rechecked the code.

3. What feedback did you receive?
I received feedback pointing out that the message format needed to strictly match the required punctuation, specifically ensuring the final full stop is included.

4. What exactly did you change after the feedback?
I updated the return string in budget_message to make sure the trailing period was correctly placed at the end of the sentence (e.g., f"{name} has {remaining} naira remaining.").

5. If you had ten more minutes, what would you check again?
I would re-verify all acceptance criteria to ensure neither function accidentally uses print() instead of return, and test an extra edge case with zero values across all parameters.
"""