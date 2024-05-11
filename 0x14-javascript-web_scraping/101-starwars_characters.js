#!/usr/bin/node
const request = require('request');
const films = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const filmsURL = films + movieId;

request(filmsURL, async function (error, response, body) {
  if (error) { console.error(error); }
  const res = JSON.parse(body);
  try {
    const characterURLs = res.characters;
    for (const URL of characterURLs) {
      const character = await readURL(URL);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
});

async function readURL (URL) {
  return new Promise((resolve, reject) => {
    request(URL, function (error, response, body) {
      if (error) { console.error(error); }
      const character = JSON.parse(body);
      resolve(character);
    });
  });
}
