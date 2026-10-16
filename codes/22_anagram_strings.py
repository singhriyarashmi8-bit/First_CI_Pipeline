

def is_anagram(first, second):
    first_clean = "".join(first.lower().split())
    second_clean = "".join(second.lower().split())

    return sorted(first_clean) == sorted(second_clean)
