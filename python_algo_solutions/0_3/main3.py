
def lns(s):
    possible_substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(substring) == len(set(substring)):
                possible_substrings.add(substring)
    return max(possible_substrings, key=len) if possible_substrings else ""



print(lns("abcabcbb"))