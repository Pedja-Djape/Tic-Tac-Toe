

import tttlib

T = tttlib.genBoard()

tttlib.printBoard(T)
print("\n")
while True:
   moveX = int(input("X move?"))
   valid_move = (T[moveX] == 0)
   while not valid_move:
      print("Invalid Move")
      tttlib.printBoard(T)
      moveX = int(input("X move?"))
      valid_move = (T[moveX] == 0)
   T[moveX] = 1
   tttlib.printBoard(T)
   game_state = tttlib.analyzeBoard(T)
   if game_state == 1:
      print("X won the game")
      break
   elif game_state == 3:
      print("Draw")
      break


   winning_position = tttlib.genWinningMove(T,2)
   non_loser_pos = tttlib.genNonLoser(T,2)
   next_move_pos = tttlib.genRandomMove(T,2)
   if winning_position != -1:
      T[winning_position] = 2

   elif non_loser_pos != -1:
      T[non_loser_pos] = 2
   else:
      T[next_move_pos] = 2
   tttlib.printBoard(T)
   game_state = tttlib.analyzeBoard(T)
   if game_state == 2:
      print("O won the game")
      break
   elif game_state == 3:
      print("Draw")
      break
