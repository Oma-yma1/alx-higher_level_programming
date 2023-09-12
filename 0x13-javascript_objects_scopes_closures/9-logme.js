#!/usr/bin/node
let coun = 0;
exports.logMe = function (item) {
  console.log(`${coun++}: ${item}`);
};
