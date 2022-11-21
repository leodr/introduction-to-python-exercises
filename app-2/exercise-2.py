import re

with open("faust.txt") as faust_file:
    faust_text = faust_file.read()

    word_map = {}

    faust_word_list = faust_text.lower().split(" ")

    faust_processed_word_list = []

    for word in faust_word_list:
        processed_word = re.sub(r"\W", "", word)

        if processed_word:
            faust_processed_word_list.append(processed_word)

    for word in faust_processed_word_list:
        word_map[word] = word_map.get(word, 0) + 1

    print(word_map)
