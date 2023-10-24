#!/usr/bin/node
const request = require('request');
const apiurl = process.argv[2];
const completed = {};

request(apiurl, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const task = JSON.parse(body);

    for (let j = 0; j < task.length; j++) {
      if (task[j].completed === true) {
        if (completed[task[j].userId] === undefined) {
          completed[task[j].userId] = 1;
        } else {
          completed[task[j].userId] += 1;
        }
      }
    }
  }
  console.log(completed);
});
