#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const { argv } = require('node:process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
const res = add(a, b);
console.log(res);
