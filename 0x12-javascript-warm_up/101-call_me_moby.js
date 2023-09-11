#!/usr/bin/node
exports.callMeMoby = function (x, funct) {
  for (let j = 0; j < x; j++) funct();
};
