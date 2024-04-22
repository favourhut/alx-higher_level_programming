#!/usr/bin/node
// parse integer

const num = process.argv[2];
const value = parseInt(num);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ', value);
}
