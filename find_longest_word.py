def find_longest_word(document, longest_word=""):
    if(document==""):
        return longest_word
    longest_word = document.split(' ',1)[0] if len(document.split(' ',1)[0]) > len(longest_word) else longest_word
    if(len(document.split(" ",1))>1):
        return find_longest_word(document.split(" ",1)[1],longest_word)
    else:
        return find_longest_word("",longest_word)