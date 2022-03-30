"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
"""
from collections import Counter


def mostCommonWord(paragraph, banned):
    words = [
        # word.strip("!?',;.").lower()
        # for word in paragraph.split(" ")
        # if word.strip("!?',;.").lower() not in banned
    ]
    temp = ""
    for i in range(len(paragraph)):

        if paragraph[i] in "!?',;. ":
            if len(temp) > 0:
                words.append(temp)
                temp = ""
        else:
            temp = temp + paragraph[i]
    words.append(temp)

    print(words)

    cnt = Counter([w.lower() for w in words if w.lower() not in banned])
    gmax = ("", 0)
    for word, ct in cnt.most_common():
        if ct > gmax[1]:
            gmax = (word, ct)
    return gmax[0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))
