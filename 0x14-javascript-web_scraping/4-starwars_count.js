#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterid = 18;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    const moviedata = JSON.parse(body);
    let count = 0;
    for (const movie of moviedata.results) {
      if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterid}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
