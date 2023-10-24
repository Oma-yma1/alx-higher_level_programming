#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
request(apiUrl + movieid, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
