#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let coun = 0;
  list.forEach(element => {
    if (element === searchElement) coun++;
  });
  return coun;
};
