function pyramid(balls) {
  if (balls <= 0) {
      throw Error('Number of balls must be integer number');
  }
  return Math.trunc((Math.sqrt(1 + 8 * balls) - 1)/2)
}