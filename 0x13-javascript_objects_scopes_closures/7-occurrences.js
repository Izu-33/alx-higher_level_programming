#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let elem in list) {
    if (elem === searchElement) counter++;
  }
  return counter;
}
