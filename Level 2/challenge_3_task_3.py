'''
iterates through the input list converting each index to a string
forming a dictionary from the number and its unicode counterpart 
which is then added to the list
'''
def num_obj(s):
    conv_s = []
    for num in s:
        object = {str(num): chr(num)}
        conv_s.append(object)
    return conv_s
