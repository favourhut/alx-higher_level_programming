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
                symbol += 'X';
            }
            console.log(symbol);
        }
    }
}

module.exports = Rectangle;

