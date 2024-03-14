#!/usr/bin/node
function factorial (num) {
  let m = 1;
  let res = 1;
  while (m <= num) {
    res *= m;
    m++;
  }
  return res;
}
const { argv } = require('node:process');
const num = parseInt(argv[2]);
const res = factorial(num);
console.log(res);
