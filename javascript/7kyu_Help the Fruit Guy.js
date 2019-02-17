function removeRotten(bagOfFruits){

    if (bagOfFruits === null || bagOfFruits === undefined || bagOfFruits.length === 0) {
        return []
    }

    let goodFruits = [];

    for (let i=0; i<bagOfFruits.length; i++) {
        let goodFruit = bagOfFruits[i].replace("rotten", "").toLowerCase();
        goodFruits.push(goodFruit)
    }
    return goodFruits

}