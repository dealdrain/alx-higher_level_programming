#!/usr/bin/node
const num = process.argv[2];
if (!parseInt(num)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < num; a++) {
    console.log('X'.repeat(num));
  }
}
