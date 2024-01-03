def can_place_flowers(flowers: list, num_of_flowers: int) -> bool:
  pos = 0

  while(pos < len(flowers) and num_of_flowers > 0):
    if flowers[pos] == 0 and (pos == 0 or flowers[pos-1] != 1) and (pos == len(flowers)-1 or flowers[pos+1] != 1):
      num_of_flowers -= 1
      pos += 1
    pos += 1

  return num_of_flowers ==  0

if __name__ == "__main__":
  assert can_place_flowers([1,0,0,0,1], 1) == True
  assert can_place_flowers([1,0,0,0,1], 2) == False
  assert can_place_flowers([1,0,0,0,0,1], 2) == False
  assert can_place_flowers([1,0,0,0,0,1], 1) == True
  assert can_place_flowers([0,0,1,0,0], 1) == True
  assert can_place_flowers([0,0,1,0,0], 2) == True
  assert can_place_flowers([0,0,0,0,0], 3) == True
  assert can_place_flowers([0,0,0,0,0], 4) == False
  assert can_place_flowers([0,0,0,0,0], 5) == False