"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""


def permute_string(str1: str, str2: str) -> str:
    """1.
    permuted_list = []
    for letter in str1:  # O(m)
            if letter not in permuted_list:  # O(l)
                    permuted_list.append(letter)
    for letter in str2:  # O(n)
            if letter not in permuted_list: # O(l)
                    permuted_list.append(letter)
    return "".join(permuted_list)  # O(l)
    """
    mp = {c: i for i, c in enumerate(str1)}
    return "".join(sorted(str2, key=lambda x: mp.get(x, 26)))


if __name__ == "__main__":
    print(permute_string("cba", "abcd"))
