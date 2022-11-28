from os import path
from django.conf import settings
import random


def shuffle(x): return random.shuffle(x)


def random_words(size=10):
    filename = path.join(settings.BASE_DIR, 'wordlist.txt')
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        start_at = random.randint(size, len(words) - size)
        shuffle(words)
        shuffle(words)
        return words[start_at: start_at + size]


def generate_password_secret_key(size=10):
    return ' '.join(random_words(size))
