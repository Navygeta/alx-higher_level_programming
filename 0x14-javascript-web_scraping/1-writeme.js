#!/usr/bin/node
'use strict';
require('fs').promises.writeFile(process.argv[2], process.argv[3], 'utf-8').catch(console.error);
