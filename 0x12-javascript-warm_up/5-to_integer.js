#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(parseInt(args[0]))) {
  const num = 'My number: ' + args[0];
  console.log(num);
} else {
  console.log('Not a number');
}
