#!/usr/bin/node

'use strict';

const fs = require('fs').promises;

const [,, filePath, contentToWrite] = process.argv;

fs.writeFile(filePath, contentToWrite, 'utf-8')
  .then(() => console.log(`Content has been successfully written to ${filePath}`))
  .catch(error => console.error(error));
