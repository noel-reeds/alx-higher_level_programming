#!/usr/bin/node
const myList = require('./100-data');
const newList = myList.list.map((num, index) => num * index);
console.log(myList.list);
console.log(newList);
