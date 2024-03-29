class Game:
    def __init__(self, row = ['1','2','3','4','5','6','7','8','9']):
        self.row = row
        
   
    def __repr__(self):
        return f' {self.row[0]} | {self.row[1]} | {self.row[2]}\n {self.row[3]} | {self.row[4]} | {self.row[5]}\n {self.row[6]} | {self.row[7]} | {self.row[8]}\n'

    def move(self, boardLocation, playertoken):
        if boardLocation not in self.row:
            print('Space is already taken')
            return f'Space already taken'
        
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
            return False

    def fullBoard(self):
        tempList = ['1','2','3','4','5','6','7','8','9']
        check = any(item in self.row for item in tempList)
        if check is True:
            return
        else:
            return True       
        
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
    player1Token = 'X'
  

    #get player 2 info
    player2Name = Player.getPlayer(Player)
    player2Token = 'O'

    #Print the board for players to see
    print(theGame.__repr__())

#Game while loop
    while True: 
        test = True
        while test == True:
        #player1 move
            player1Placement = input(f"{player1Name} where do you want to place your symbol? ")
            player1move = theGame.move(player1Placement, player1Token)
            if player1move == 'Space already taken':
                print('Try Again')
            else:
                test = False
        print(theGame.__repr__())

        #check if player1 won, or if board is full
        player1Win = theGame.calcWinner(player1Token)
        if player1Win is True:
            print(f'{player1Name} is the Winner!')
            return
        boardIsFull = theGame.fullBoard()
        if boardIsFull is True:
            print(f"It's a Tie")
            return

        #player2 move
        test = True
        while test == True:
            player2Placement = input(f"{player2Name} where do you want to place your symbol? ")
            player2move = theGame.move(player2Placement, player2Token)
            if player2move == 'Space already taken':
                print('Try Again')
            else:
                test = False
        print(theGame.__repr__())

        #check if player2 won, or if board is full
        player2Win = theGame.calcWinner(player2Token)
        if player2Win is True:
            print(f'{player2Name} is the Winner!')
            return
        boardIsFull = theGame.fullBoard()
        if boardIsFull is True:
            print(f"It's a Tie")
            return
main()

