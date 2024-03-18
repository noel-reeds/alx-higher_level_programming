#!/usr/bin/node
const ParentSquare = require('./5-square');
class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let m = 0;
      while (m < this.height) {
        let row = '';
        let n = 0;
        while (n < this.width) {
          row += c;
          n++;
        }
        m++;
        console.log(row);
      }
    } else {
      // calls parent class default print function
      this.print();
    }
  }
}
module.exports = Square;
