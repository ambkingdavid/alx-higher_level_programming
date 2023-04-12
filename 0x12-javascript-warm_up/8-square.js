#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(parseInt(args[0]))) {
  let i = 0;
  let square;
  
  while (i < parseInt(args[0])) {
    let j = 0;
    square = '';
    while (j < parseInt(args[0])) {
      square += 'X';
      j++;
    }
    console.log(square);
    i++;
  }
} else {
  console.log('Missing size');
}
