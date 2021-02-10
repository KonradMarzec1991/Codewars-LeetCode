const iqTest = numbers => {
  let nums = numbers.split(' ');
  nums.unshift(nums[0]);
  nums.push(nums[0]);
  console.log(nums);
  for (let i = 1; i < nums.length - 1; i++) {
      if (nums[i] % 2 !== nums[i-1] % 2 && nums[i] % 2 !== nums[i+1] % 2) {
          return i;
      }
  }
  return 1;
}