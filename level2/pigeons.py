"""
When I start to feed my pigeon, a minute later two more fly by. And a minute later another 3.
Then 4, and so on. One portion of food lasts a pigeon for a minute.
In case there's not enough food for all the birds, the pigeons that came first, eat first.
Pigeons are hungry animals and eat without stopping.
How many pigeons I'd have to feed at least once if I have N portions wheat?

Input: A quantity of portions wheat, a positive integer.
Output: The number of fed pigeons, an integer.
"""


def checkio(number):
    portion = 0
    new_pigeons = 0
    while number > portion:
        new_pigeons += 1
        new_portion = portion + new_pigeons
        if new_portion <= number:
            portion = new_portion
        else:
            portion += number - portion
        number -= new_portion
    return portion

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"