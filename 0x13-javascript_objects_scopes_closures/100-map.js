#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((value, index) => value * index);

console.log("Original List:", list);
console.log("New List:", newList);

