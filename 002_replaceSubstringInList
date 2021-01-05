#Robin Chong updated 05-JAN

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

def replaceSubstringInList_method01(txt,newFormat):

    newList = []

    for oldFormat in txt:
        if oldFormat in txt:
            newList.append(oldFormat.replace(".hpp",newFormat))

    print("Method 1: " + str(newList))


def replaceSubstringInList_method02(txt,newFormat):

    newList = [oldFormat.replace(".hpp",newFormat) if (oldFormat.find(".hpp") != -1) else oldFormat for oldFormat in txt]

    print("Method 2: " + str(newList))

replaceSubstringInList_method01(filenames,".h")
replaceSubstringInList_method02(filenames,".h")

