"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most
frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols and whitespaces, only letters. If you have two or more letters with the
same frequency, then return the letter which comes first in the alphabet. (Ex: we have "b" and "f" as the most frequent,
then return "b")

Input: A text for analysis. A string (Unicode).

Output: The most frequent letter. A string.
"""
from collections import Counter
import re


def checkio(text):
    p = re.compile('\W+?')
    clear_text = p.sub('', text.lower())
    c = Counter(clear_text)
    max_count = max(c.values())
    max_letters = [k for k, i in c.items() if i == max_count]
    max_letters.sort()
    return max_letters[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello?,..,.-- World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."