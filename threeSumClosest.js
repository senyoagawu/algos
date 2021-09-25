// https://leetcode.com/problems/3sum-closest/submissions/

const threeSumClosest = (nums, target) => {
    const sorted = nums.sort((a, b) => a - b) //needs to be sorted for while loop logic
    let [globalDiff, globalSum] = [Infinity,null] 
    //pointer method to reduce O(n^3) to O(n^2)
    for (let i = 0; i < nums.length - 2; i++) {
        let [leftIdx, rightIdx] = [i + 1, nums.length - 1];
        while (leftIdx < rightIdx) {
            let currSum = sorted[i] + sorted[leftIdx] + sorted[rightIdx]
            if (globalSum === null) globalSum = currSum;
            const diff = currSum - target
            if (diff > 0) { //oops to big, more right pointer, in (to the left) *1
                rightIdx--
            } else if (diff < 0) { //too small, lets make it bigger *1
                leftIdx++
            } else { //we've found it
                return currSum
            }
            //lns 15, 17 are why we need the array to be sorted. gaurentees moving
            //right pointer left results in a smaller overall sum and moving left 
            //pointer right results in a larger overall sum
            if (Math.abs(diff) < globalDiff) {
                globalDiff = Math.abs(diff);
                globalSum = currSum
            }
        }
    }
        return globalSum
        
    };