#!/usr/bin/node

exports.converter = function (base) {
  // Define the recursive helper function
  const convertRecursive = (number) => {
    if (number >= base) {
      convertRecursive(Math.floor(number / base));
    }
    process.stdout.write((number % base).toString());
  };

  // Return the function for external use
  return convertRecursive;
};

