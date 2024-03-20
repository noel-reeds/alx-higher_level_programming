#!/usr/bin/node
exports.converter = function (base) {
  return function converter (num) {
    if (base === 10) {
      return num;
    } else if (base === 8) {
      return num.toString(8);
    } else if (base === 16) {
      return num.toString(16);
    } else if (base === 2) {
      return num.toString(2);
    }
  };
};
