class Game:
    def __init__(self, row1 = ['1','2','3'], row2 = ['4','5','6'], row3 = ['7','8','9']):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
   
    def __repr__(self):
        return f' {self.row1[0]} | {self.row1[1]} | {self.row1[2]}\n {self.row2[0]} | {self.row2[1]} | {self.row2[2]}\n {self.row3[0]} | {self.row3[1]} | {self.row3[2]}\n'

    def move(self, boardLocation, playertoken):
        for n, i in enumerate(self.row1):
            if i == boardLocation:
                self.row1[n] = playertoken
        return self.row1


        '''
        if boardLocation inside row1
            replace boardLocation with symbol
            
        '''
        
            




    

    
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
    #player2Name = Player.getPlayer(Player)
    #player2Token = Player.getToken(Player)

    

    while True: 
        player1Placement = input("Where do you want to place your symbol? ")
        player1move = theGame.move(player1Placement, player1Token)
        print(theGame.__repr__())

        player2Placement = input("Where do you want to place your symbol? ")
        player1move = theGame.move(player2Placement, player2Token)
        print(theGame.__repr__())

        
       

main()


'''
get player names
player 1 goes first
    place 'x' at some location
    update that position in the row
ask player where they want to 
'''

