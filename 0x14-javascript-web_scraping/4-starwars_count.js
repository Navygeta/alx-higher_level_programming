#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const movieData = JSON.parse(body).results;
      const characterCount = movieData.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0);
      console.log(characterCount);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
