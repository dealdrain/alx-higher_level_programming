#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  for (x--; x >= 0; x--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
