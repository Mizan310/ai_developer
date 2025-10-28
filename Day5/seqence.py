sent = '''i am xyz. i am learning python innovativeskills.
i am feeling positive about it. i do not feel negative about my past.'''
def capitalize_sent(text):
    sent_list = text.split(".")
    print(sent_list)
    # sent_list = []
    sent_list[0] = sent_list[0].strip(' ').capitalize()
    sent_list[1] = sent_list[1].strip(' ').capitalize()
    sent_list[2] = sent_list[2].strip(' ').capitalize()
    sent_list[3] = sent_list[3].strip(' ').capitalize()
    # sent_list[0] = sent_list[0].capitalize()
    # sent_list[1] = sent_list[1].capitalize()
    # sent_list[2] = sent_list[2].capitalize()
    # sent_list[3] = sent_list[3].capitalize()
    cap_text = ". ".join(sent_list)
    print(cap_text)

capitalize_sent(sent)