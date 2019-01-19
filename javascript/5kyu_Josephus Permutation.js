function josephus(items,k){

    let myIndex = -1;
    my_arr = [];

    while (items.length > 0) {
        myIndex = (myIndex + k) % items.length;
        my_arr.push(items.splice(items.indexOf(items[myIndex]), 1));
        console.log(my_arr);
        myIndex -= 1;
    }

    return my_arr
}

console.log(josephus([1,2,3,4,5,6,7],3));