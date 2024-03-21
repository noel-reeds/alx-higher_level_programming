#!/usr/bin/node
const mydict = require('./101-data');
const sorted = {};
for (const key in mydict.dict) {
  const value = mydict.dict[key];
  if (sorted[value]) {
    sorted[value].push(key);
  } else {
    sorted[value] = [key];
  }
}
console.log(sorted);
