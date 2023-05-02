#!/usr/bin/node

const fs = require('fs');
const [file1, file2, dest] = process.argv.slice(2);

fs.readFile(file1, (err, data1) => {
  if (err) throw err;
  fs.readFile(file2, (err, data2) => {
    if (err) throw err;
    const concatData = data1.toString() + data2.toString();
    fs.writeFile(dest, concatData, err => {
      if (err) throw err;
    });
  });
});
