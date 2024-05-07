#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs').promises;
try {
  const res = fs.readFile(filePath, 'utf-8');
  console.log(res.toString());
} catch (error) {
  console.log(error.message);
}
