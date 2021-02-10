function predictAge(age1,age2,age3,age4,age5,age6,age7,age8){

    let final = 0;

    for(let i=0; i<arguments.length; i++) {
        final += arguments[i] * arguments[i];
    }
    return Math.floor(Math.sqrt(final)/2);

}