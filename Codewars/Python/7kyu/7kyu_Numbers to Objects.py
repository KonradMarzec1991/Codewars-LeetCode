def num_obj(s):
    return [{f'{num}': chr(num)} for num in s]


print(num_obj([118,117,120]),[{'118':'v'}, {'117':'u'}, {'120':'x'}])