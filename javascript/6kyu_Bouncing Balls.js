function bouncingBall(h,  bounce,  window) {

    if (h <= 0 || (bounce <= 0 || bounce >= 1) || window >= h) {
        return -1;
    } else {
        return Math.floor(Math.log(window/h)/Math.log(bounce)) * 2 + 1;
    }

}