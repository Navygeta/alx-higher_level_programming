#!/usr/bin/node
'use strict';
const request = require('request-promise');

request(process.argv[2])
  .then(response => console.log(`code: ${response.statusCode}`))
  .catch(error => console.error(error));
