function sumTriangularNumbers(n) {
    let total = 0;
    for (let i = 0; i <= n; i++) {
        total += i*(i+1)/2
    }
    return total;
}