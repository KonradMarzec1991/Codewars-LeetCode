function vowelIndices(word){

    let vowels = 'aeyuio';
    let arr = word.toLowerCase().split("");

    let indexes = [];

    for(let i=0; i < arr.length; i++) {
        if (vowels.indexOf(arr[i]) > -1) {
            indexes.push(i+1);
        }
    }

    return indexes
}