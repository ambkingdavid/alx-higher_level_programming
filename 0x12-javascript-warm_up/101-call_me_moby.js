#!/usr/bin/node

exports.callMeMoby = function (x, f) {
  while (x > 0) {
    f();
    x--;
  }
};
