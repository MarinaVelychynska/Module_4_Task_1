print("Програма, допоможе перевірити чи слово палліндром")

def word_is_pallindrom(word) :
    word_pallindrom = str(word)
    return word_pallindrom == str(word)[::-1]

if __name__ == "__main__":
   items_text = input("Напиши слово: ")
   word_result = word_is_pallindrom(items_text)
   print(word_result)