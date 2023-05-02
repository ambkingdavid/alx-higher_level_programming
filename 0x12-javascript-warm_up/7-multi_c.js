#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(parseInt(args[0]))) {
  let num = parseInt(args[0]);

  while (num > 0) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurence');
}
