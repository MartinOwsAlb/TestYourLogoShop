"""
Action module to generate random data for tests runs.
"""
import random
import string


class Randomizer:
    @classmethod
    def random_str(cls, length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @classmethod
    def random_value(cls):
        return random.randint(2, 10)

    @classmethod
    def random_email(cls):
        return f"test{Randomizer.random_str(10)}@test.de"

    @classmethod
    def random_number_between(cls, down_range, up_range):
        return random.randrange(down_range, up_range)
