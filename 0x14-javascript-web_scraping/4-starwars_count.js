#!/usr/bin/node

const request = require('request');
const apiurl = process.argv[2];
request(apiurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const filmId in results) {
      const characters = results[filmId].characters;
      for (const charId in characters) {
        if (characters[charId].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
