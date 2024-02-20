#!/usr/bin/node

'use strict';

const [,, filePath] = process.argv;

require('fs').promises.readFile(filePath, 'utf-8')
  .then(content => console.log(content))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
