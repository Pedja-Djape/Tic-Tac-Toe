
def genBoard():
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += (str(pos))
      pos+=1

   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   return True


def analyzeBoard(t):
   if t[0] == t[1] == t[2] != 0:
       return t[0]
   if t[3] == t[4] == t[5] != 0:
       return t[3]
   if t[6] == t[7] == t[8] != 0:
       return t[6]
   if t[0] == t[3] == t[6] != 0:
       return t[0]
   if t[1] == t[4] == t[7] != 0:
       return t[1]
   if t[2] == t[5] == t[8] != 0:
       return t[2]
   if t[0] == t[4] == t[8] != 0:
       return t[0]
   if t[2] == t[4] == t[6] != 0:
       return t[2]

   n_opens=0
   for i in t:
      if i==0:
         n_opens+=1
   if n_opens == 0:
       return 3
   else:
       return 0

def genNonLoser(T,player):
   if len(T) != 9:
       return -1
   if not ((player == 1) or (player == 2)):
       return -1

   if player == 1:
      other_player = 2
   else:
      other_player = 1

   pos = 0
   for i in T:
      if i == 0:
         T_copy = list(T)
         T_copy[pos] = other_player
         winner = analyzeBoard(T_copy)
         if winner == other_player:
            return pos
      pos+=1

   return -1

def genWinningMove(T,player):
   if len(T) != 9:
       return -1
   if not ((player == 1) or (player == 2)):
       return -1
   pos = 0
   for i in T:
      if i == 0:
         T_copy = list(T)
         T_copy[pos] = player
         winner = analyzeBoard(T_copy)
         if winner == player:
            return pos
      pos +=1

   return -1


def genOpenMove(T,player):
   if len(T) != 9:
       return -1
   if not ((player == 1) or (player == 2)):
       return -1

   pos = 0
   for i in T:
       if i == 0:
           return pos
       pos +=1
   return -1

def genRandomMove(T,player):
   if len(T) != 9:
      return -1
   if not ((player == 1) or (player == 2)):
      return -1
   n_opens = 0
   for i in T:
      if i ==0:
         n_opens += 1
   if n_opens == 0:
      return -1

   import random
   while True:
      pos = random.randint(0,8)
      value_in_square = T[pos]
      if value_in_square == 0:
         return pos
