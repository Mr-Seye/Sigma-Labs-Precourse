def num_obj(s):
    conv_s = []
    for num in s:
        object = {str(num): chr(num)}
        conv_s.append(object)
    return conv_s
