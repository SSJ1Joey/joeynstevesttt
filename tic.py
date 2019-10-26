class Game:
    def __init__(self, row = ['1','2','3','4','5','6','7','8','9']):
        self.row = row
        
   
    def __repr__(self):
        return f' {self.row[0]} | {self.row[1]} | {self.row[2]}\n {self.row[3]} | {self.row[4]} | {self.row[5]}\n {self.row[6]} | {self.row[7]} | {self.row[8]}\n'

    def move(self, boardLocation, playertoken):
        for n, i in enumerate(self.row):
            if i == boardLocation:
                self.row[n] = playertoken
        return self.row
    def calcWinner(self, token):
        if self.row[0] == token and self.row[1] == token and self.row[2] == token:
            return True
        elif self.row[3] == token and self.row[4] == token and self.row[5] == token:
            return True
        elif self.row[6] == token and self.row[7] == token and self.row[8] == token:
            return True
        elif self.row[0] == token and self.row[3] == token and self.row[6] == token:
            return True
        elif self.row[1] == token and self.row[4] == token and self.row[7] == token:
            return True
        elif self.row[2] == token and self.row[3] == token and self.row[8] == token:
            return True
        elif self.row[0] == token and self.row[4] == token and self.row[8] == token:
            return True
        elif self.row[2] == token and self.row[4] == token and self.row[6] == token:
            return True
        else:
            return
    def fullBoard(self):
        tempList = ['1','2','3','4','5','6','7','8','9']
        check = any(item in self.row for item in tempList)
        if check is True:
            return 
        else:
            return f'The board is full'       
        
class Player:
    def __init__(self, player, token):
        self.player = player
        self.token = token 
    def getPlayer(self):
        player = input("What is the name for Player? ")
        return player
    def getToken(self):
        token = input("What do you want your token to be, X or O? ")
        return token 


    
def main():
    theGame = Game()
    #get player 1 info
    player1Name = Player.getPlayer(Player)
    player1Token = Player.getToken(Player)
  

    #get player 2 info
    player2Name = Player.getPlayer(Player)
    player2Token = Player.getToken(Player)

    

    while True: 
        #player1 move
        player1Placement = input(f"{player1Name} where do you want to place your symbol? ")
        player1move = theGame.move(player1Placement, player1Token)
        print(theGame.__repr__())

        #check if player1 won, or if board is full
        player1Win = theGame.calcWinner(player1Token)
        print(player1Win)
        boardIsFull = theGame.fullBoard()
        print(boardIsFull)

        #player2 move
        player2Placement = input(f"{player2Name} where do you want to place your symbol? ")
        player1move = theGame.move(player2Placement, player2Token)
        print(theGame.__repr__())

        #check if player2 won, or if board is full
        player2Win = theGame.calcWinner(player2Token)
        print(player2Win)
        boardIsFull = theGame.fullBoard()
        print(boardIsFull)

        
       

main()


'''
get player names
player 1 goes first
    place 'x' at some location
    update that position in the row
ask player where they want to 
'''

