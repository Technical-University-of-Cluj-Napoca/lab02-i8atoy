from collections import defaultdict

## geeks for geeks implementation

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for string in strs:
        temp = "".join(sorted(string))
        groups[temp].append(string)

    res = list(groups.values())