# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    open_file = open("./story.txt", "r")
    read_file_content = open_file.read()
    read_file_content.close()
    return read_file_content
    

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    word_count = {}
    if words in word_count:
        word_count[words] += 1
    else:
        word_count[words] = 1
    return word_count

print(count_words())