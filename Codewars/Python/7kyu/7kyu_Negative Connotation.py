def connotation(strng):
    count = sum(1 for i in strng.split() if i[0].lower() in 'abcdefghijklm')
    return True if count >= len(strng.split()) - count else False
