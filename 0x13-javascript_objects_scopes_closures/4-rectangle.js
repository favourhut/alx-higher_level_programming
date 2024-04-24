#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w >= 0 && h >= 0) {
            this.width = w;
            this.height = h;
        }
    }

    // an instance method that prints the rectangle via character X
    print() {
        for (let i = 0; i = (this.width); i++) {
            let symbol = '';
            for (let j = 0; j = (this.height); j++) {
                symbol += 'X'
            }
            console.log(symbol)
        }
    }

    // instance method that exchanges the width and the height
    rotate() {
        const rot = this.width;
        this.width = this.height;
        this.height = rot;
    }

    // instance method that multiples the width and the height by 2
    double() {
        this.width * 2;
        this.height * 2;
    }
}

module.exports = Rectangle;