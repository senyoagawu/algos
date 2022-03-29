def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = midT - 1
    return -1


def some_method(root):
    counter = 0
    arr = []

    def dfs(root):

        if not root:
            # counter don't count cuz we've gone past
            return
        dfs(root.left)
        arr.append(root.val)
        counter += 1
        dfs(root.left)


def clean_word(word):
    count = 0
    cleanedWord = ""
    for char in word:
        if char.isalpha():
            cleanedWord += char.lower()
    return cleanedWord


def most_common_words(text):
    tally = {}
    for word in text.split(" "):
        cleanedWord = clean_word(word)
        if cleanedWord in tally:
            tally[cleanedWord] = tally[cleanedWord] + 1
        else:
            tally[cleanedWord] = 1

    return [(k, v) for k, v in tally.items()]


print(most_common_words("It was the best of times, it was the worst of times."))

def subsets(arr):
    if len(arr) == 0:
        return [[]]
    last = arr[-1]
    subs = subsets(arr[0 : len(arr) - 1])
