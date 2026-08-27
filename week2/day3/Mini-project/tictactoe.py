board = [
      ["X","O","X"],
      ["O","X","O"],
      ["X","O","X"]
] 
def display_board(board):
         
         print(board[0][0],"|", board[0] [1], "|",board[0][2])
         print("------")
         print(board[1][0],"|", board[1] [1], "|",board[1][2]) 
         print("-------")
         print(board[2][0],"|", board[2] [1], "|",board[2][2])

         display_board=(board)


def player_input(player):
        row =int(input(f"{player} - Row 1-3:")) -1
        column= int(input(f"{player} - column 1-3: ")) -1

        return row ,column 

player="X"
row,column=player_input(player)
board[row][column]=player
display_board(board)



def check_win(board,player):
        if board[0][0] ==player and board[0][1] == player and board[0][2]==player:
            return True
        if board[1][0] ==player and board[1][1] == player and board[1][2]==player:
            return True
        if board[2][0] ==player and board[2][1] == player and board[2][2]==player:   
            return True 
        if board[0][0] ==player and board[1][0] == player and board[2][0]==player: 
               return True 
        if board[0][1] ==player and board[1][1] == player and board[2][1]==player:
               return True
        if board[0][2] ==player and board[1][2] == player and board[2][2]==player:
               return True
        if board[0][0] ==player and board[1][1] == player and board[2][2]==player:
              return True
        if board[0][2] ==player and board[1][1] == player and board[2][0]==player:
               return True
        
        return False 


def  check_tie(board):
       for row in board:
              for cell in row:
                     if cell == " ":
                            return False
       return True
       



def play():
       board = [
      ["1","",""],
      ["","",""],
      ["","",""]
] 
       player = "X"
       while True:
              display_board(board)
              row, column = player_input(player)
              board[row][column]=player
              if check_win(board,player):
                     display_board(board)
                     print(player,"Wins!")
                     break
              if check_tie(board):
                     print("Tie!")
                     break
              if player == "X":
                     player="O"
              else:
                     player="X"
       play()              




    
                   


