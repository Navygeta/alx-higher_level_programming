#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const completedCount = {};
    JSON.parse(body).forEach(task => {
      if (task.completed) {
        completedCount[task.userId] = (completedCount[task.userId] || 0) + 1;
      }
    });
    console.log(completedCount);
  } else {
    console.error(`An error occurred. Status code: ${response.statusCode}`);
  }
});
