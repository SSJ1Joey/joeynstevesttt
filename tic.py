class game:
    def __init__(self, row1 = ['','',''], row2 = ['','',''], row3 = ['','','']):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
   
    def __repr__(self):
        return f' {self.row1[0]} | {self.row1[1]} | {self.row1[2]}\n {self.row2[0]} | {self.row2[1]} | {self.row2[2]}\n {self.row3[0]} | {self.row3[1]} | {self.row3[2]}\n'

    def move(self, row, location, player):
        if row == 1:
            



    #def calcWinner(self):
    

    
class player:
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
    #get player 1 info
   player1Name = player.getPlayer(player)
   player1Token = player.getToken(player)

   #get player 2 info
   player2Name = player.getPlayer(player)
   player2Token = player.getToken(player)

   while True: 

main()


'''
get player names
player 1 goes first
    place 'x' at some location
    update that position in the row
ask player where they want to 
'''

