#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const responseJSON = JSON.parse(body);
      console.log(responseJSON.title);
    } catch (error) {
      console.error(`Error parsing JSON: ${error.message}`);
    }

    if (response.statusCode !== 200) {
      console.error(`Error code: ${response.statusCode}`);
    }
  }
});
