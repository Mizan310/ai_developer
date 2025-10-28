## **Problem-5**

# Write a function that merges two dictionaries. Keys can be different. If a key exists in both dictionaries, sum their values.

# **Example:**
# Input: d1 = {'a': 100, 'b': 200, 'c': 300}, d2 = {'a': 300, 'b': 200, 'd': 400}
# Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

marged = d1.copy()

for key, value in d2.items():
    if key in marged:
        marged[key] += value
    else:
        marged[key] = value

print(marged)