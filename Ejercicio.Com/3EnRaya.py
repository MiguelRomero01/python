"""/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */"""
 
import random

def board():
     board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
     return board


def game(board):
     playerTurn = True
     machineTurn = False
     
     PlayerSymbol = 'X'
     MachineSymbol = 'O'
     turnsPlayed = 0
     
     print("your symbol: ",PlayerSymbol)
     print("Oponent symbol: ",MachineSymbol)
     
     while turnsPlayed <= 9:
          
          #Player turn
          if playerTurn:
               print("\nPlayer Turn:")
               row = int(input('Row (1-3): '))
               col = int(input('Column (1-3): '))
               
               if board[row-1][col-1] == ' ':
                    board[row-1][col-1] = PlayerSymbol 
                           
                    turnsPlayed += 1
                    machineTurn = True
                    playerTurn = False
               else:
                   print("The field is already full! Try again\n") 

          #Machine Turn
          elif machineTurn:
               print("\nMachine Turn: ")
               
               while True:
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                    
                    if board[row][col] == ' ':
                         board[row][col] = MachineSymbol 
                           
                         turnsPlayed += 1
                         machineTurn = False
                         playerTurn = True
                         break
               
          for i in board:
               for j in i:
                    print("|",j,end=" ")
               print()  
          
          WinCondition(board,PlayerSymbol,MachineSymbol,turnsPlayed)
          
          #return the result
          if WinCondition(board,PlayerSymbol,MachineSymbol,turnsPlayed) == 'Win':
               return "you are the winner"
          elif WinCondition(board,PlayerSymbol,MachineSymbol,turnsPlayed) == 'Draw':
               return 'Draw'
          elif WinCondition(board,PlayerSymbol,MachineSymbol,turnsPlayed) == 'Loose':
               return'You are the looser'
     
          
def WinCondition(board,PlayerSymbol,MachineSymbol,turnsPlayed):
     #diagonales
     WinConditions = [
          [board[0][0], board[1][1], board[2][2]],
          [board[0][2], board[1][1], board[2][0]],
          [board[0][0], board[1][0], board[2][0]],
          [board[0][2], board[1][2], board[2][2]],
          [board[0][0], board[0][1], board[0][2]],
          [board[2][0], board[2][1], board[2][2]]
          ]

     if turnsPlayed >= 3:
          for i in WinConditions:
               playerWin=0
               MachineWin=0
               
               for j in i:
                    if j == PlayerSymbol:
                         playerWin += 1
                    elif j == MachineSymbol:
                         MachineWin += 1
                         
               if playerWin == 3:
                    return 'Win'
               elif MachineWin == 3:
                    return 'Loose'
               
     elif turnsPlayed == 9:
          return 'Draw'
          
print(game(board()))