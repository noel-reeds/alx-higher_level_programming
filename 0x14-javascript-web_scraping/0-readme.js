#!/usr/bin/node
const fs = require('fs').promises;
async function readFile (filePath) {
  try {
    const res = await fs.readFile(filePath, 'utf-8');
    console.log(res);
  } catch (error) {
    console.error(error.message);
  }
}
const filePath = process.argv[2];
readFile(filePath);
