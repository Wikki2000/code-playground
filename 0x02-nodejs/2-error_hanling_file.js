#!/usr/bin/node
const fs = require('fs');

try {
  // Synchronously read the contents of the file 'example.txt' as a string
  const data = fs.readFileSync('example.txt', 'utf8');
  console.log(data);
} catch (err) {
  // Handle any errors that occur during file reading
  console.error('Error reading the file:', err);
}
