#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log('0');
} else if (argv.length === 3) {
  console.log('0');
} else {
  let index = 2;
  let largeIndex = index;
  while (index < argv.length) {
    if (parseInt(argv[largeIndex]) < parseInt(argv[index])) {
      largeIndex = index;
    }
    index++;
  }
  const temp = parseInt(argv[2]);
  argv[2] = parseInt(argv[largeIndex]);
  argv[largeIndex] = temp;
  index = 3;
  let secondIndex = index;
  while (index < argv.length) {
    if (parseInt(argv[secondIndex]) < parseInt(argv[index])) {
      secondIndex = index;
    }
    index++;
  }
  console.log(argv[secondIndex]);
}
