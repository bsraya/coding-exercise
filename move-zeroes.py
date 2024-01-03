def move_zeroes(nums: list) -> list:
  left, right = 0, 0

  while(right < len(nums)):
    if nums[right] != 0:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
    right += 1
  
  return nums

if __name__ == "__main__":
  assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
  assert move_zeroes([0]) == [0]
  assert move_zeroes([0,0]) == [0,0]
  assert move_zeroes([1]) == [1]
  assert move_zeroes([0,0,1]) == [1,0,0]
  assert move_zeroes([0,1,0,1,0,1]) == [1,1,1,0,0,0]