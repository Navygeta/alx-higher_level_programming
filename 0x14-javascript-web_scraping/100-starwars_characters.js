#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(baseUrl + id, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  JSON.parse(body).characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, characterBody) => {
      if (error) {
        console.error(error);
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
