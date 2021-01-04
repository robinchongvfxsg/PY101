def pig_latin_method01(text):
    say= ""
    words = text.split()
    new_words = []

    # print(words)

    for word in words:

        # print(word)

        say = word[1:] + word[0] + "ay"

        # print(say)

        new_words.append(say)

    return "Method 1: " + " ".join(new_words)

def pig_latin_method02(text):

    return "Method 2: " +' '.join([word[1:] + word[0] + "ay" for word in text.split()])






print(pig_latin_method01("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin_method02("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# Let's create a function that turns text into pig latin: a simple text transformation that modifies each
# word moving the first character to the end and appending "ay" to the end. For example, python ends
# up as ythonpay.
