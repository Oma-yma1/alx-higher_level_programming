#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const apiurl = process.argv[2];
const filepath = process.argv[3];

request(apiurl, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
