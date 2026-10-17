
def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k != 0 else items.copy()


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))
