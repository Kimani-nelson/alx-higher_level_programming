#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Assuming the Rectangle class is in a file named 4-rectangle.js

class Square extends Rectangle {
  constructor(size) {
    // Call the constructor of the Rectangle class using super
    super(size, size);
  }
}

module.exports = Square;

