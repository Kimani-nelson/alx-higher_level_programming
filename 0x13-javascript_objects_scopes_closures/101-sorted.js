#!/usr/bin/node

const inputDict = require('./101-data').dict;

// Compute a new dictionary of user ids by occurrence
const outputDict = Object.keys(inputDict).reduce((result, userId) => {
  const occurrences = inputDict[userId];

  if (result[occurrences] === undefined) {
    result[occurrences] = [userId];
  } else {
    result[occurrences].push(userId);
  }

  return result;
}, {});

console.log(outputDict);

