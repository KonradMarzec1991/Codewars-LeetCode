function encode(str, n) {

    let alphabet = 'abcdefghijklmnopqrstuvwxyz';

    let str_arr = str.toLowerCase().split("");
    let str_n = n.toString();

    let final_arr = [];

    for(let i=0; i<str_arr.length; i++) {
        let num1 = Number(str_n.charAt(Math.floor(i % n.toString().length)));
        let num2 = alphabet.indexOf(str_arr[i]) + 1;
        final_arr.push(num1 + num2)

    }
    return final_arr;
}