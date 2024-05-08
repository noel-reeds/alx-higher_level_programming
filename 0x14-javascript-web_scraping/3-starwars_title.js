#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(endpoint, function (error, response, res) {
  const req = JSON.parse(res);
  if (error) { console.error(error); } else { console.log(req.title); }
});
