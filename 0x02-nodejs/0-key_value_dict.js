#!/usr/bin/node
const obj = {
    key1: 'value1',
    key2: 'value2',
    key3: 'value3'
};
console.log('Key: key');
for (let key in obj) {
    console.log(key, obj[key]);
};
