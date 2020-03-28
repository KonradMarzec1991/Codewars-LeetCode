class Circle {

    constructor(radius) {
        this.radius = radius;
    }

    getArea() {
        return Math.PI * Math.pow(this.radius, 2);
    }

    getPerimeter() {
        return Math.PI * 2 * this.radius;
    }

}