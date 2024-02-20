#!/usr/bin/node
'use strict';
require('fs').promises.writeFile(process.argv[2], process.argv[3], 'utf-8')
  .then(() => console.log(`Content written to ${process.argv[2]}`))
  .catch(error => console.error(error));
