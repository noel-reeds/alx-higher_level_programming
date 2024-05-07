#!/usr/bin/node
const fs = require('fs').promises;
async function (filePath) {
  try {
    const res = fs.readFile(filePath, 'utf-8');
    console.log(res.toString());
  } catch (error) {
    console.log(error.message);
  }
}
const filePath = process.argv[2];
readFile(filePath);
