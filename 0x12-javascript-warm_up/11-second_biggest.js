#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log('0');
} else if (argv.length === 3) {
  console.log('0');
} else {
  let m = 2;
  let num = argv[m];
  while (m < argv.length) {
    if (argv[m] < argv[m + 1]) {
      num = argv[m + 1];
    }
    m++;
  }
  console.log(m);
  const temp = argv[2];
  argv[2] = num;
  argv[m] = temp;
  let some_var = 3;
  let second_num = argv[some_var];
  console.log(m);
  while (some_var < argv.length) {
    if (second_num < argv[some_var + 1]) {
      second_num = argv[some_var + 1];
    }
    some_var++;
  }
  console.log(second_num);
}
