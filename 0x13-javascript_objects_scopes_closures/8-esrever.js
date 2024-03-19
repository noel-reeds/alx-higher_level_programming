#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  const maxIndex = list.length - 1;
  let revIndex = 0;
  for (let m = maxIndex; m >= 0; m--) {
    revList[revIndex] = list[m];
    revIndex++;
  }
  return revList;
};
