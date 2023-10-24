#!/usr/bin/node
const request = require('request');
const apiurl = 'http://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(apiurl, function (error, response, body) {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request.get(character, function (error, response, body) {
        if (error) {
          throw error;
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
