import requests
import random


def shuffle(x): return random.shuffle(x)


def random_words(size=10):
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    res = requests.get(url)
    words = res.text.splitlines()
    start_at = random.randint(size, len(words) - size)
    shuffle(words)
    shuffle(words)
    return words[start_at: start_at + size]


def generate_password_secret_key(size=10):
    return ' '.join(random_words(size))
