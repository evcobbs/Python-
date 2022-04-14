#chess board validator

#simple version 
def isValidChessBoard(board):
  colors = ('b', 'w')
  pieces = ('king','queen','rook', 'knight','bishop', 'pawn')
  bPieces, wPieces = 0, 0 
  bPawns, wPawns = 0, 0
  bKing, wKing = 0, 0

  #key is 1a to 8h only 
  for space in board.keys():
    if space[0] not in "12345678" or space[1] not in "abcdefgh":
      return False
  
  #value starts with w or b, then 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
  for piece in board.values():
    if piece[0] not in colors or piece[1:] not in pieces:
      return False
  #only 16 peices, 
  for piece in board.values():
    if piece[0] == 'b':
      bPieces += 1
    if piece[0] == 'w':
      wPieces += 1

  if bPieces > 16 or wPieces > 16:
    return False 
    
  #8 pawns max 
  for piece in board.values():
    if piece == 'bpawn':
      bPawns += 1
    if piece == 'wpawn':
      wPawns += 1
      
  if bPawns > 8 or wPawns > 8:
    return False 
    
  #1 bking and 1 wking
  for piece in board.values():
    if piece == 'bking':
      bKing += 1
    if piece == 'wking':
      wKing += 1
      
  if bKing != 1 or wKing != 1:
    return False 
    
  return True
#end isValidChessBoard()

  
#with print outs to show what is wrong
def isValidChessBoardLong(board):
  colors = ('b', 'w')
  pieces = ('king','queen','rook', 'knight','bishop', 'pawn')
  bPieces, wPieces = 0, 0 
  bPawns, wPawns = 0, 0
  bKing, wKing = 0, 0

  #key is 1a to 8h only 
  for space in board.keys():
    if space[0] not in "12345678":
      print ("bad row")
      return False
    if space[1] not in "abcdefgh":
      print ("bad column")
      return False
      
  #value starts with w or b, then 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
  for piece in board.values():
    if piece[0] not in colors:
      print("bad color")
      return False
      
  for piece in board.values():
    if piece[1:] not in pieces:
      print("bad piece")
      return False
      
  #only 16 w or b pieces 
  for piece in board.values():
    if piece[0] == 'b':
      bPieces += 1
    if piece[0] == 'w':
      wPieces += 1

  if bPieces > 16: 
    print("Black has too many pieces.")
    return False 
    
  if wPieces > 16:
    print("White has too many pieces.")
    return False 
    
  #8 pawns max 
  for piece in board.values():
    if piece == 'bpawn':
      bPawns += 1
    if piece == 'wpawn':
      wPawns += 1

  if bPawns > 8: 
    print("Black has too many pawns.")
    return False 
    
  if wPawns > 8:
    print("White has too many pawns.")
    return False
    
  #1 bking and 1 wking
  for piece in board.values():
    if piece == 'bking':
      bKing += 1
    if piece == 'wking':
      wKing += 1

  if bKing != 1: 
    print("Must have 1 black king.")
    return False 
    
  if wKing != 1:
    print("Must have 1 white king.")
    return False
  
  return True
#end isValidChessBoardLong()

#test boards
validBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'
}

badRowBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '9e': 'wking'
}

badColumnBoard = {
  '1z': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '8e': 'wking'
}

badColorBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'cbishop', '5h': 'bqueen', '3e': 'wking'
}

badPieceBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'bbishopp', '5h': 'bqueen', '3e': 'wking'
}

bTooManyBoard = {
  '1h': 'bking','2h': 'bking','3h': 'bking','4h': 'bking','5h': 'bking','6h': 'bking','7h': 'bking','8h': 'bking','1a': 'bking','2a': 'bking','3a': 'bking','4a': 'bking','5a': 'bking','6a': 'bking','7a': 'bking','8a': 'bking', '1b': 'bking'
}

wTooManyBoard = {
  '1h': 'wking','2h': 'wking','3h': 'wking','4h': 'wking','5h': 'wking','6h': 'wking','7h': 'wking','8h': 'wking','1a': 'wking','2a': 'wking','3a': 'wking','4a': 'wking','5a': 'wking','6a': 'wking','7a': 'wking','8a': 'wking', '1b': 'wking'
}

twoBkingsBoard = {
  '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '1a': 'bking'
}

pawnsTooManyBoard = {
  '1h': 'wpawn','2h': 'wpawn','3h': 'wpawn','4h': 'wpawn','5h': 'wpawn','6h': 'wpawn','7h': 'wpawn','8h': 'wpawn', '1c': 'wpawn', '1a': 'bking', '1b': 'wking'
}


#test
print(f'Valid board is {isValidChessBoard(validBoard)}')
#print(f'Bad row board is {isValidChessBoard(badRowBoard)}')
#print(f'Bad column board is {isValidChessBoard(badColumnBoard)}')
#print(f'Bad color board {isValidChessBoard(badColorBoard)}')
#print(f'Bad piece board {isValidChessBoard(badPieceBoard)}')
#print(f'too many black {isValidChessBoard(bTooManyBoard)}')
#print(f'too many white {isValidChessBoard(wTooManyBoard)}')
print(f'two black kings {isValidChessBoardLong(twoBkingsBoard)}')
print(f'too many pawns {isValidChessBoardLong(pawnsTooManyBoard)}')

