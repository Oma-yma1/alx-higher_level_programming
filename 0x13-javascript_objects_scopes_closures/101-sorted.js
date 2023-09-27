#!/usr/bin/node
const dictionary = require('./101-data').dict;
const dict = {};

for (const k in dictionary) {
  const oc = dictionary[k];
  dict[oc] = [];
  for (const key in dictionary) {
    if (dictionary[key] === oc) {
      dict[oc].push(key);
    }
  }
}
console.log(dict);
