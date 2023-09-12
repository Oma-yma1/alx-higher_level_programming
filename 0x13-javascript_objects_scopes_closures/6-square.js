#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    this.print(c);
  }
};
