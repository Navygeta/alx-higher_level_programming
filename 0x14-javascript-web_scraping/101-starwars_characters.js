#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(filmUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
