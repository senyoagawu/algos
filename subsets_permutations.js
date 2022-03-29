const dfs = node => {
  if (!node) {
    return null
  }

  const queue = [node.left, node.right]
  while (queue.length) {
    const currNode = queue.pop()
    currNodeBreadthFirst, queue = queue[0], queue.slice(1)

    //do something with it depth first
    queue.push(currNode.left, currNode.right)
  }


}

function subsets(arr, len=null) {
  // base case 
  if (arr.length === 0) return [[]];
  let val;
  while (true){
    [val, arr] =  [arr[0], arr.slice(1)]
    new_subsets = arr.map(sub => sub)
  }
  const last = arr[arr.length - 1];

  // recursive call, get the subsets for the array which is one element smaller
  const subs = subsets(arr.slice(0, arr.length - 1));
  console.log(subs)

}


subsets([1, 2, 3, 4, 5])