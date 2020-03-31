# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:08:52 2019

@author: 6430u
"""

board = [' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', 
         '---+---+---',
          ' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6',
          '---+---+---',
          ' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9']


wins = [{1,2,3},{1,4,7},{1,5,9},{2,5,8},{3,5,7},{3,6,9},{4,5,6},{7,8,9}]

p1name = input('Player 1, choose a 1 character name. ')
p2name = input('Player 2, choose a 1 character name. ')
num = ''

plays = {
        p1name : [],
        p2name : []
        }
  
def printBoard():
   print(''.join(board[0:10]))
   print(''.join(board[10]))
   print(''.join(board[11:21]))
   print(''.join(board[21]))
   print(''.join(board[22:33]))

def fullBoard():
    global board
    check = ['1','2','3','4','5','6','7','8','9']
    for i in check:
        if i in board:
            return False
        else:
            continue
    print('Cats!')
    return True

def getMove(user):
    global p1name
    global p2name
    global num
    while num not in board:
        num = input(user + ', where would you like to play? ')
        print(num)
        if num in board and num in ['1','2','3','4','5','6','7','8','9']:
            break
        else:
            print('Not avaliable or invalid entry. Try again.')
            num = ''
            continue
        
        
def turn(user):
    global num
    getMove(user)
    place = board.index(str(num))
    board[place] = user
    plays[user].append(int(num))
    print('-'*35)
    printBoard()
        
def checkWin(user):
    global plays
    checkSet = set(plays[user])   
    for i in wins:
        if i <= checkSet:
            print(user + ' wins!')
            return True
            break
        else:
            continue
    
def game():
    printBoard()
    game_on = True
    while game_on:
        turn(p1name)
        if checkWin(p1name):
            game_on = False
            break
        if fullBoard():
            game_on = False
            break
        turn(p2name)
        if checkWin(p2name):
            game_on = False
            break
        if fullBoard():
            game_on = False
            break
        
    print('Good game!')

game()


















