#!/usr/bin/node

const fs = require('fs');
const pathfile = process.argv[2];

fs.readFile(pathfile, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
