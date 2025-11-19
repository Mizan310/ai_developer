# dictionary
# key:value
# my_dict['key']
# mutable
# duplication possible for values
# Sequence type data- list, string, tuple
# but dictionary is not a sequence type data
dict1 = {"key1": 'value1', 'key2':'value2'}
dict2 = {"key4": 'value4', 'key5':'value5'}

print(dict1)
print(dict1['key1'])
# print(dict1.pop("key2"))
print(dict1)
dict1["key3"] = "value3"
print(dict1) # {'key1': 'value1', 'key3': 'value3'}

dict1['key2'] = "value3" # value update
print(dict1)
del dict1["key1"] # Accesing values # Alternative is get method
print(dict1)
print(dict1.get('key1', 'No')) # Accesing values using get method
print(dict1.get('key2'))

dict1.update(dict2)
print(dict1)

print(dict1.pop("key4"))
print(dict1)

print(dict1.pop("key4", "poped"))

print(dict1.popitem()) # removed and return last key value
print(dict1)
print(dict1.keys())
print(dict1.values())
print(list(dict1.items()))

dict1["key3"] = ["value3", "value6"]
print(dict1)

# nested dictionary
dict1["key3"] = {"key_nes":"value"}
print(dict1)

print("############################")
# set 
# it is unordered
# it is mutable
set1 = {"elm1", "elm2", "elm3"}
# set1 = set1.add('elm4')
# set1.clear()
print(set1)
# print(set1.pop())
# print(type(set1))
set1.update(['key5','key6'])
set1.update({'key5','key6'})

set1.add("keyx")
print(set1)