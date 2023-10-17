# 5. Write a Python program to find the list of words that are longer than n from a
# given list of words.
# N=3, Word List =The quick brown fox jumps over the lazy dog
# Output: ['quick', 'brown', 'jumps', 'over', 'lazy']
# Write a Python program to print the numbers from the list after removing even
# numbers from it.

word_list = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
n = 3

long_words = [word for word in word_list if len(word) > n]
print("Words longer than", n, "characters:", long_words)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [num for num in number_list if num % 2 != 0]
print("Numbers after removing even numbers:", odd_numbers)
