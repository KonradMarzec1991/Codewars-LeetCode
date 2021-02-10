function factorial(n) {

  if (typeof n != 'number') {
      return 'Not a number!!!'
  }

  if (n < 0 || n > 12) {
      throw RangeError('Out of Range!!!')
  }

  if (n === 0 || n === 1) {
      return 1;
  }

  let m = 1;

  while (n > 0) {
      m *= n--;
  }

  return m;

}