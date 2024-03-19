#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elemOccurences = 0;
  for (let m = 0; m < list.length; m++) {
    if (list[m] === searchElement) {
      elemOccurences += 1;
    }
  }
  return elemOccurences;
};
