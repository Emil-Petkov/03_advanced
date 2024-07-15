def concatenate(*words, **kv_words):
    text = ''.join(words)

    for k, v in kv_words.items():
        text = text.replace(k, v)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
