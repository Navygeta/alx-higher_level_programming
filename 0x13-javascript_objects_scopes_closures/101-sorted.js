#!/usr/bin/node
const originalDictionary = require('./101-data').dict;

const totalList = Object.entries(originalDictionary);
const valuesList = Object.values(originalDictionary);
const uniqueValues = [...new Set(valuesList)];
const newDictionary = {};

for (const uniqueValue of uniqueValues) {
  const keyList = [];
  for (const entry of totalList) {
    if (entry[1] === uniqueValue) {
      keyList.unshift(entry[0]);
    }
  }
  newDictionary[uniqueValue] = keyList;
}

console.log(newDictionary);
