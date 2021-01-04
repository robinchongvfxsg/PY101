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

