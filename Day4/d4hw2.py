# # hw-2
# '''I am syz. i am learning python innovativeskills.
# i am feeling positive about it. i do not feel negative about my past.'''
# # capitalize all the first character of each sentence

def capitalize_sentences(text):
    # special_chars = f"!@#$%^&*()_+=-`~[];:'\",/<>?\\|`"
    # text = text.lower()
    # for char in special_chars:
    #     text = text.replace(char, " ")
    sentences = text.split(".")
    capitalize_sentences = [] # create a list to hold sentences
    for sentence in sentences:
        sentence = sentence.strip() # remove extra spaces
        if sentence: # if sentence is not empty
            capitalize_sentences.append(sentence.capitalize())
    clean_text = ". ".join(capitalize_sentences)
    return clean_text

input_text = '''I am syz. i am learning python innovativeskills.
i am feeling positive about it. i do not feel negative about my past.'''
output_text = capitalize_sentences(input_text)
print(output_text)

