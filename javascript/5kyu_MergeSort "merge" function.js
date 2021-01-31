function mergesorted(a, b) {
    let x = 0, y = 0, z = []
    while (x < a.length || y < b.length) {
        if (y === b.length || x < a.length && a[x] <= b[y]) {
            z.push(a[x])
            x++
        } else {
            z.push(b[y])
            y++
        }
    }
    return z;
}


console.log(mergesorted([1,2,7],[3,4,6]));