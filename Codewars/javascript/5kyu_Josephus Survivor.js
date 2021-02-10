function josephusSurvivor(n,k){

    let num = 0;
    for (let i=1;i<=n;i++) {
        num = (num + k) % i
    }
    return num + 1;
}