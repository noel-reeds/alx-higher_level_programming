#!/usr/bin/node
const { argv } = require('node:process');
if (!isNaN(argv[2])) {
  let m = 0;
  while (m < argv[2]) {
    let n = 0;
    let rows = '';
    while (n < argv[2]) {
      rows += 'X';
      n++;
    }
    console.log(rows);
    m++;
  }
} else {
  console.log('Missing size');
}
