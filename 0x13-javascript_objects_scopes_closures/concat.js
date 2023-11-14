#!/usr/bin/node

const fs = require('fs');

// Ensure correct number of arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

// Get file paths from command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read content from source files
const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate content
const concatenatedContent = content1 + content2;

// Write the result to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Files ${sourceFile1} and ${sourceFile2} were successfully concatenated to ${destinationFile}.`);

