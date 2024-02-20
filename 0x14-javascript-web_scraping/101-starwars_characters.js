#!/usr/bin/node

const req = require('request');
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

req(filmUrl, function (err, response, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printCharacters(chars, 0);
  }
});

function printCharacters(characters, index) {
  req(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
