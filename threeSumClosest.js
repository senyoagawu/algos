// https://leetcode.com/problems/3sum-closest/submissions/

const threeSumClosest = (nums, target) => {
    const sorted = nums.sort((a, b) => a - b)
    let [currentClosest, ans] = [Infinity,] 
    //pointer method to reduce O(n^3) to O(n^2)
    for (let i = 0; i < nums.length - 2; i++) {
        let leftIdx = i + 1;
        let rightIdx = nums.length - 1;
        while (leftIdx < rightIdx) {
            let currSum = sorted[i] + sorted[leftIdx] + sorted[rightIdx]
            if (ans === undefined) ans = currSum
            console.log(sorted[i], sorted[leftIdx], sorted[rightIdx])
            console.log('curr sum', currSum)
            const diff = currSum - target
            if (diff > 0) {
                //[1, 2, 5, 6, 10] target 5.5
                // ^  ^        ^  13
                //currSum - target =>  7.5  
                // [-4,-1,1,2]
                rightIdx--
            } else if (diff < 0) {
                leftIdx++
            } else { //we've found it
                return currSum
            }
            if (Math.abs(diff) < currentClosest) {
                currentClosest = Math.abs(diff);
                ans = currSum
            }
        }
        return ans
    };