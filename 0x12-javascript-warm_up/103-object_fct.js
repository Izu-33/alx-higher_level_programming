#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 1
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
