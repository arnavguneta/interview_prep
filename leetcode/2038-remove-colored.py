from typing import Tuple

def winnerOfGame(colors: str) -> bool:
  def canPlayerMove(letter: str) -> Tuple[bool, str]:
    for i in range(len(colors)):
      if i == 0 or i == len(colors) - 1: continue
      if colors[i] is letter and colors[i-1] is letter and colors[i + 1] is letter:
        return (True, colors[0:i] + colors[i+1:len(colors)])
      else:
        continue
    return (False, colors)
  
  curPlayer = 'A'
  canMove = True
  while(canMove):
    canMove, colors = canPlayerMove(curPlayer)
    if not canMove: return False if curPlayer is 'B' else True
    curPlayer = 'B' if curPlayer is 'A' else 'A'
  print("default returning")
  return False

print(winnerOfGame('AAABABB'))
print(winnerOfGame('AA'))
print(winnerOfGame('BB'))
print(winnerOfGame('ABBBBBBBAAA'))

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
      def canPlayerMove(letter: str) -> Tuple[bool, str]:
        lastToken = ''
        for i in range(1, len(colors), 2):
          print(letter, colors[i], i, colors[i] is letter and colors[i-1] is letter and colors[i + 1] is letter)
          if colors[i-1] is letter and colors[i] is letter and lastToken is letter:
            return (True, colors[0:i] + colors[i+1:len(colors)])
          elif i+1 < len(colors) and colors[i] is letter and colors[i-1] is letter and colors[i + 1] is letter:
            return (True, colors[0:i-1] + colors[i:len(colors)])
          else:
            lastToken = colors[i]
            continue
        return (False, colors)
      
      curPlayer = 'A'
      canMove = True
      while(canMove):
        canMove, colors = canPlayerMove(curPlayer)
        print('curPlayer', curPlayer, 'canMove', canMove)
        if not canMove: return True if curPlayer is 'B' else False
        curPlayer = 'B' if curPlayer is 'A' else 'A'
      print("default returning")
      return False