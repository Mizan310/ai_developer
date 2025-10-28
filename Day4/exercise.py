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


def good_bad(text):
    text = text.replace('good', 'positive')
    text = text.replace('bad', 'negative')
    return text


input_text = "This is a Good-looking day! It's not a bad thing @ all. I am hunghry"
def both_are(input_text):
    result1 = clean_all_text(input_text)
    result2 = good_bad(input_text)
    print(result1, result2)