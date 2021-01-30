function averages(numbers) {
    if (numbers && numbers.length > 1) {
        let temp = [];
        for (let i = 0; i < numbers.length - 1; i++) {
            temp.push((numbers[i] + numbers[i+1])/2);
        }
        return temp;
    } else {
        return []
    }
}
