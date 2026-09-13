def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for char in s1:
        freq[char] = freq.get(char, 0) + 1

    for char in s2:
        if char not in freq:
            return False

        freq[char] -= 1

        if freq[char] < 0:
            return False

    return True


s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

print("Anagram" if is_anagram(s1, s2) else "Not Anagram")
