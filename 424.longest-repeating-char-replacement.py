def characterReplacement(str, k):
    def recursively(str, k, children):
        if k == 0:
            return children
        charSet = set(str)
        gchildren = []
        for i in range(len(str)):
            # gchildren.extend(
            print(
                [str[0:i] + char + str[i + 1 :] for char in charSet if char != str[i]]
            )
            # print(gchildren)
        return recursively(str, k - 1, gchildren)


print(characterReplacement("ABABA", 1))
