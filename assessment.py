# write a function that checks if the amount a user wants to withdraw is more than their balance. If it is more than their balance, return "insufficeient funds" or calculate how much remains after withdraw else return this Hello, username, your balance is {balance}


def remaining(balance, withdraw, username):

    return balance - withdraw

    if withdraw > balance:
        return "insufficient funds"

    else:
        return f"Hello, {username}, your balance is {balance}"