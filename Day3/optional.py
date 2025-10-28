# 2. make a function that will take a text and retrun list of word 
# from the text. the text may contain punctuation,  special characters 
# and newlines

def clean_all_text(text):
    special_chars = "!@#$%^&*()_+=-`~[]{};:'\",./<>?\\|`"
    print(text)
    modified_text = text
    for char in special_chars:
        modified_text = modified_text.replace(char, " ")

    correct_sentence = modified_text.split()
    return correct_sentence

input_text = "This is a good-looking day! It's not a bad thing @ all."
output_text = clean_all_text(input_text)
print(output_text)