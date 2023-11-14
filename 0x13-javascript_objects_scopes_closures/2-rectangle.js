#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (this.isValidDimension(w) && this.isValidDimension(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if dimensions are not valid
      this.width = 0;
      this.height = 0;
    }
  }

  isValidDimension(dimension) {
    return Number.isInteger(dimension) && dimension > 0;
  }
}

