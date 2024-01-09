#!/usr/bin/node
// counting occurences
exports.nbOccurences = function (list, element) {
  return list.filter(x => x === element).length;
};
