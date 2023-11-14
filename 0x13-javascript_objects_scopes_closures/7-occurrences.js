#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  const occurrences = list.reduce((count, element) => {
    return count + (element === searchElement ? 1 : 0);
  }, 0);

  return occurrences;
};

