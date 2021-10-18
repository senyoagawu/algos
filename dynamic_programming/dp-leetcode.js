function tribonacci(n, tab = [0, 1, 1]) {
  if (n < tab.length) return tab[n];
  tab.push(tab.slice(tab.length - 3).reduce((acc, el) => acc + el));
  // console.log(n, tab, tab.slice(tab.length - 3));
  return tribonacci(n, tab);
}

const climbStairs = (n, base) => {
  const calculateNextNum = (ways, isEven) => {
    mapping = {};
    ways.forEach((way) => {
      if (isEven) {
        let newWays = promotions(way);
        if (newWays) mapping[promotions(way)] = ".";
      }
      mapping[[...way, 1].join("")] = ".";
      mapping[[1, ...way].join("")] = ".";
    });
    // console.log(mapping);
    return Object.keys(mapping).map(
      (distintWay) => distintWay.split("").String
    );
  };

  const promotions = (distinctWay) => {
    // if (distinctWay.length ===0) return 'error';
    unique = {};
    for (let i = 0; i < distinctWay.length - 1; i++) {
      if (distinctWay[i] === 1) {
        const safeCopy = distinctWay.slice();
        if (safeCopy.length === 0) {
          // console.log("OH HOW RIGHT YOU ARE");
          break;
        }
        safeCopy[i] = 2;
        unique[safeCopy.join("")] = ".";
      }
    }
    // console.log(unique);
    ans = Object.keys(unique).map((str) => str.split("").map(String));

    return ans.length === 0 ? null : ans;
  };

  if (!base)
    base = [
      0, // for zero index
      [[1]],
      [[1, 1], [2]],
    ];
  if (n < base.length) return [base[n], base[n].length];
  base.push(calculateNextNum(base[base.length - 1], base.length % 2 === 1));
  return climbStairs(n, base);
};

console.log(climbStairs(4));
// console.log(climbStairs(6));

module.exports = {
  tribonacci,
  climbStairs,
};
