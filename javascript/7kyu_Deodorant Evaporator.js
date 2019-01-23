function evaporator(content, evap_per_day, threshold){

    let counter = 0;
    let full = 100;

    while (full >= threshold) {
        full -= full * (evap_per_day/100);
        counter++
    }

    return counter;
}