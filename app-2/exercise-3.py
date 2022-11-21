import re

with open("faust.txt") as faust_file:
    faust_text = faust_file.read()

    faust_word_list = faust_text.lower().split(" ")

    faust_processed_word_list = []

    for word in faust_word_list:
        processed_word = re.sub(r"\W", "", word)

        if processed_word:
            faust_processed_word_list.append(processed_word)

    faust_processed_word_list.sort()

    print(faust_processed_word_list[:500])
