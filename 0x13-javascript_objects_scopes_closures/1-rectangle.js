#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}

// Creating an instance of Rectangle
const myRectangle = new Rectangle(5, 10);

// Accessing and printing the attributes
console.log(`Width: ${myRectangle.width}`);
console.log(`Height: ${myRectangle.height}`);

