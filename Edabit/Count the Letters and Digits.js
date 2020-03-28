function countAll(str) {
    const letters = /^[A-Za-z]+$/;
    const digits = /^[0-9]+$/;

    const result = {letters: 0, digits: 0};
    for (let x = 0; x < str.length; x++) {
        let char = str.charAt(x);
            if (char.match(letters)) {
                result.letters++;
            } else if (char.match(digits)) {
                result.digits++;
            }
    }
    return result;
}
