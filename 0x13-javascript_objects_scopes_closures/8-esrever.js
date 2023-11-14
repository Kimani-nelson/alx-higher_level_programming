#!/usr/bin/node

exports.esrever = function (list) {
  // Clone the array to avoid modifying the original array
  const reversedList = list.slice();

  // Use two pointers to reverse the array
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    // Swap elements at positions i and j
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};

