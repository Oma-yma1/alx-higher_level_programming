#!/usr/bin/node
const args = process.argv[2];
if (args === undefined) {
  console.log('NO argument');
} else {
  console.log(args);
}
