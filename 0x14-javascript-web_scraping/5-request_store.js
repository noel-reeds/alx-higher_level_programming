#!/usr/bin/node
const fs = require('fs').promises;
const request = require('request');

const filePath = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, res) {
  if (error) { console.error(error); }
  try {
    write(filePath, res);
  } catch (error) {
    console.error(error);
  }
});
async function write (filePath, fileContent) {
  try {
    await fs.writeFile(filePath, fileContent, 'utf-8', { flag: 'a' });
  } catch (error) {
    console.error(error);
  }
}
