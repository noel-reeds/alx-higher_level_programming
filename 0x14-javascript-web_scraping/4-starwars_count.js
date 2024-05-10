#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const res = JSON.parse(body);
  const films = res.results;
  let filmCount = 0;
  films.forEach((film) => {
    film.characters.forEach((characterURL) => {
      const desiredURL = 'https://swapi-api.alx-tools.com/api/people/18/';
      if (characterURL === desiredURL) { filmCount += 1; }
    });
  }); console.log(filmCount);
});
