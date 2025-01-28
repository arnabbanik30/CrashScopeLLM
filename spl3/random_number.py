import random

def generate_random_int():
    number = random.randint(0, 1000)
    is_negative = random.choices([True, False], weights=[6, 4])[0]
    return -number if is_negative else number