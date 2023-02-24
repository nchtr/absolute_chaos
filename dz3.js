//2
let pair = (array) => array.reduce((acc, value) => {
    if (Array.isArray(value)) {
      acc[value[0]] = value[1];
    }
    return acc;
  }, {});
let data = [['a', 1], ['b', 2]];
console.log(pair(data))
//1
function chess(val) {
    var board = "";
    for (var i = 1; i < val*val; i += 1) {
      if ((i % (val + 1)) == 0) {
        board += "\n";
      } else if (i % 2 != 0) {
        board += "#";
      } else {
        board += " ";
      }
    }
    return board;
  }
  
  console.log(chess(10));
