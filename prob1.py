def reverse_words(s):
    new_list = s.split(" ")
    reversed_list = new_list[::-1]
    reversed_text = " ".join(reversed_list)
    
    return reversed_text
# short solution
# def reverse_words(s):
#     return " ".join(s.split(" ")[::-1])

print (reverse_words("The greatest victory is that which requires no battle"))
