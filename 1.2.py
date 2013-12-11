# 1.2 Write code to reverse a C-Style String. (C-String means that "abcd" is represented as five characters, including the null character.)

def reverse(string):
    string = string + '*' # In this case, * represents the null char.
    tmp = ''
    i = 0
    while string[i] != '*':
        tmp = string[i] + tmp
        i += 1
    return tmp


if __name__ == '__main__':
    print reverse('abcdefghijklmnopqrstuvwxyz')
