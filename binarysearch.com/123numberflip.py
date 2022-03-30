"""You are given an integer n consisting of digits 1, 2, and 3 and you can flip one digit to a 3. Return the maximum number you can make.

Constraints

1 ≤ n < 2 ** 31
Example 1
Input
n = 123
Output
323
"""


def numberflip(n):
    ans = list(str(n))
    for idx, char in enumerate(ans):
        if char != "3":
            ans[idx] = "3"
            return int("".join(ans))
    return int("".join(ans))


print(numberflip(123))
print(numberflip(1))
