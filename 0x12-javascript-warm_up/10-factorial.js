#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

let factor;

if (!isNaN(parseInt(args[0]))) {
  factor = factorial(parseInt(args[0]));
  console.log(factor);
} else {
  factor = 1;
  console.log(factor);
}
