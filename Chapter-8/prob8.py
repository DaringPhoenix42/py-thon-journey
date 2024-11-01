# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
#
# def remove_word_from_list(word, word_list):
#     return [w.strip() for w in word_list
#              if w.strip() != word.strip()
#     ]
l=["hi","hello","world"]
def remove_word_from_list(word, word_list):
    if word in word_list:
        word_list.remove(word)
    else:
        word_list.append(word)

 
print(remove_word_from_list("hello", l))
print(("hello",l))

