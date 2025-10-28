def clean_all_text(text):
    special_chars = "!@#$%^&*()_+=-`~[]{};:'\",/<>?\\|`"
    print(text)
    text = text.lower()
    modified_text = text
    for char in special_chars:
        modified_text = modified_text.replace(char, " ")

    correct_sentence = modified_text.split()
    # print(correct_sentence)

    clean_text = " ".join(correct_sentence)


    # change_word = clean_text.replace('good', 'positive').replace('bad', 'negative')
    # return change_word
    # clean_text = clean_text.replace('good', 'positive')
    # clean_text = clean_text.replace('bad', 'negative')
    # return clean_text
    # change_word = clean_text.replace('good', 'positive')
    # change_word = change_word.replace('bad', 'negative')
    # return change_word
    change_word = clean_text.replace('good', 'positive')
    clean_text = change_word.replace('bad', 'negative')
    return clean_text

input_text = "This is a Good-looking day! It's not a Bad thing @ all. I am hunghry"
output_text = clean_all_text(input_text)
print(output_text)
input_text2 = "This is a good-looking day! It's not a bad thing @ all. I am hunghry"
output_text2 = clean_all_text(input_text2)
print(output_text2)