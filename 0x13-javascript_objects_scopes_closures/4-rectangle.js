#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let m = 0;
    while (m < this.height) {
      let n = 0;
      let row = '';
      while (n < this.width) {
        row += 'X';
        n++;
      }
      console.log(row);
      m++;
    }
  }

  rotate () {
    // swap
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    // doubles sides
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
