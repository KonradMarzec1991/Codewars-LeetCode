def string_transformer(s):
   return ' '.join(x.swapcase() for x in reversed(s.split(' ')))