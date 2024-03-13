#!/usr/bin/node
const { argv } = require('node:process');
if (!isNaN(argv[2])) {
  let m = 0;
  while (m < argv[2]) {
    console.log('C is fun');
    m++;
  }
} else {
  console.log('Missing number of occurrences');
}
