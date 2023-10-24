#!/usr/bin/node
const request = require('request');
const apiurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(apiurl, function (error, response, body) {
  if (!error) {
    const character = JSON.parse(body).characters;
    printChar(character, 0);
  }
});
function printChar (character, idx) {
  request(character[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < character.length) {
        printChar(character, idx + 1);
      }
    }
  });
}
