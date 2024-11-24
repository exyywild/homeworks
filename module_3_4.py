def single_root_words(root_word, *other_words):
    same_words = []
    root_word_low = root_word.lower()

    for word in other_words:
        word_low = word.lower()
        if root_word_low in word_low or word_low in root_word_low:
            same_words.append(word)

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))