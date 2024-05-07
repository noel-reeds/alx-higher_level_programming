#!/usr/bin/node
const fs = require('fs').promises;
async function write (filename, filecontent) {
  try {
    await fs.writeFile(filename, filecontent, 'utf-8', { flag: 'a' });
  } catch (error) {
    console.error(error.message);
  }
}
const filename = process.argv[2];
const filecontent = process.argv[3];
write(filename, filecontent);
