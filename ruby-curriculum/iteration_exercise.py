# ### Factors
#
# Write a method `factors(num)` that returns an array containing all the
# factors of a given number.


def factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]


print(factors(2))
print(factors(3))
print(factors(7))
print(factors(24))


def isPrime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    factors = []

    from math import sqrt

    def my_reduce(num):
        print(num)
        for n in range(2, int(sqrt(num)) + 1):
            if num % n == 0:
                return (n, num // n)
        return None

    while not isPrime(n):
        fac, n = my_reduce(n)
        factors.append(fac)

    if n > 1:
        factors.append(n)
    return factors


print(prime_factorization(2))
print(prime_factorization(20))
print(prime_factorization(100))
print(prime_factorization(2384912))
# ### Bubble Sort
#
# http://en.wikipedia.org/wiki/bubble_sort
#
# Implement Bubble sort in a method, `Array#bubble_sort!`. Your method should
# modify the array so that it is in sorted order.
#
# > Bubble sort, sometimes incorrectly referred to as sinking sort, is a
# > simple sorting algorithm that works by repeatedly stepping through
# > the list to be sorted, comparing each pair of adjacent items and
# > swapping them if they are in the wrong order. The pass through the
# > list is repeated until no swaps are needed, which indicates that the
# > list is sorted. The algorithm gets its name from the way smaller
# > elements "bubble" to the top of the list. Because it only uses
# > comparisons to operate on elements, it is a comparison
# > sort. Although the algorithm is simple, most other algorithms are
# > more efficient for sorting large lists.
#
# Hint: Ruby has parallel assignment for easily swapping values:
# http://rubyquicktips.com/post/384502538/easily-swap-two-variables-values
#
# After writing `bubble_sort!`, write a `bubble_sort` that does the same
# but doesn't modify the original. Do this in two lines using `dup`.
#
# Finally, modify your `Array#bubble_sort!` method so that, instead of
# using `>` and `<` to compare elements, it takes a block to perform the
# comparison:
#
# ```ruby
# [1, 3, 5].bubble_sort! { |num1, num2| num1 <=> num2 } #sort ascending
# [1, 3, 5].bubble_sort! { |num1, num2| num2 <=> num1 } #sort descending
# ```
#
# #### `#<=>` (the **spaceship** method) compares objects. `x.<=>(y)` returns
# `-1` if `x` is less than `y`. If `x` and `y` are equal, it returns `0`. If
# greater, `1`. For future reference, you can define `<=>` on your own classes.
#
# http://stackoverflow.com/questions/827649/what-is-the-ruby-spaceship-operator


class List:
    def __init__(self, iterable):
        self.iter = list(iterable)

    def bubble_sort(self, prc):
        while True:
            swapped = False
            for i, n1 in enumerate(self.iter):
                for j, n2 in enumerate(self.iter):
                    if j == i + 1 and prc(n1, n2) and not swapped:
                        self.iter[i], self.iter[j] = n2, n1
                        swapped = True
            if not swapped:
                return self.iter

    def bubble_sort_safe(self, prc):
        copy = List(self.iter)
        return copy.bubble_sort(prc)


x = List([4, 20, 3, 4, 1, 8, 2, 9])
y = List([4, 20, 3, 4, 1, 8, 2, 9])
print(x.bubble_sort(lambda x, y: x > y))
print(x.__dict__)
print(y.bubble_sort_safe(lambda x, y: x > y))
print(y.__dict__)

# ### Substrings and Subwords
#
# Write a method, `substrings`, that will take a `String` and return an
# array containing each of its substrings. Don't repeat substrings.
# Example output: `substrings("cat") => ["c", "ca", "cat", "a", "at",
# "t"]`.
#
# Your `substrings` method returns many strings that are not true English
# words. Let's write a new method, `subwords`, which will call
# `substrings`, filtering it to return only valid words. To do this,
# `subwords` will accept both a string and a dictionary (an array of
# words).


def substrings(string):
    subs = []
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string) + 1):
            subs.append(string[i:j])
    return subs


print(substrings("cat"))  # ["c", "ca", "cat", "a", "at",
# "t"]


def subwords(word, dictionary):
    return [w for w in substrings(word) if w in dictionary]


print(subwords("cat", ["at", "a", "cat"]))
# ### Doubler
# Write a `doubler` method that takes an array of integers and returns an
# array with the original elements multiplied by two.


def doubler(array):
    return [i * 2 for i in array]


print(doubler([1, 5, 2, 7, 4]))

# ### My Each
# Extend the Array class to include a method named `my_each` that takes a
# block, calls the block on every element of the array, and then returns
# the original array. Do not use Enumerable's `each` method. I want to be
# able to write:
#
# ```ruby
# # calls my_each twice on the array, printing all the numbers twice.
# return_value = [1, 2, 3].my_each do |num|
#   puts num
#   puts num:
# # => 1:
#      2
#      3
#      1
#      2
#      3
#
# p return_value # => [1, 2, 3]
# ```


class Array:
    def my_each(prc):
        pass


# ### My Enumerable Methods
# * Implement new `Array` methods `my_map` and `my_select`. Do
#   it by monkey-patching the `Array` class. Don't use any of the
#   original versions when writing these. Use your `my_each` method to
#   define the others. Remember that `each`/`map`/`select` do not modify
#   the original array.
# * Implement a `my_inject` method. Your version shouldn't take an
#   optional starting argument; just use the first element. Ruby's
#   `inject` is fancy (you can write `[1, 2, 3].inject(:+)` to shorten
#   up `[1, 2, 3].inject { |sum, num| sum + num }`), but do the block
#   (and not the symbol) version. Again, use your `my_each` to define
#   `my_inject`. Again, do not modify the original array.


class Array:
    def my_map(prc):
        pass

    def my_select(prc):
        pass

    def my_inject(blk):
        pass


# ### Concatenate
# Create a method that takes in an `Array` of `String`s and uses `inject`
# to return the concatenation of the strings.
#
# ```ruby
# concatenate(["Yay ", "for ", "strings!"])
# # => "Yay for strings!"
# ```


def concatenate(strings):
    pass
