import re


def is_pangram(sentence):
    chars = set(re.sub('[^a-z]', '', sentence.lower()))
    return len(chars) == 26
