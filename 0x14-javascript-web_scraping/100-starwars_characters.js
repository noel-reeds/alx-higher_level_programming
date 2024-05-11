#!/usr/bin/node
const request = require('request');
const films = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const filmsURL = films + movieId;

request(filmsURL, function (error, response, body) {
  if (error) { console.error(error); }
  const res = JSON.parse(body);
  try {
    const characterURL = res.characters;
    for (const m in characterURL) {
      request(characterURL[m], function (error, response, body) {
        if (error) { console.error(error); }
        const character = JSON.parse(body);
        try {
          console.log(character.name);
        } catch (error) {
          console.error(error);
        }
      });
    }
  } catch (error) {
    console.error(error);
  }
});
