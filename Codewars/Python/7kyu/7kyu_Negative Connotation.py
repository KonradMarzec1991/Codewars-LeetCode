def connotation(strng):
    count = sum(1 for i in strng.split() if i[0].lower() in 'abcdefghijklm')
    return True if count >= len(strng.split()) - count else False


print(connotation("A big brown fox caught a bad bunny"), True)
print(connotation("Xylophones can obtain Xenon."), False)
print(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)
print(connotation("All FOoD tAsTEs NIcE for someONe"), True)
print(connotation("Is  this the  best  Kata?"), True)