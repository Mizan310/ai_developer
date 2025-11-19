vowels = 'aeiouAEIOU'
sentence = "Learning Python is fun"

count = 0
for word in sentence:
    # print(word)
    if word in vowels:
        count += 1
print(f"The total number of vowels is {count}.")
