class game:
    def __init__(self, row1 = ['','',''], row2 = ['','',''], row3 = ['','','']):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
   
    def __repr__(self):
        return f' {self.row1[0]} | {self.row1[1]} | {self.row1[2]}\n {self.row2[0]} | {self.row2[1]} | {self.row2[2]}\n {self.row3[0]} | {self.row3[1]} | {self.row3[2]}\n


    #def move(self, row, location, player):



    #def calcWinner(self):
    

    
class player:
    def __init__(self, player, token):
        self.player = player
        self.token = token 
    def getPlayer(self):
        player = input("What is the name for Player 1? ")
        return player
    def getToken(self):
        token = input("What do you want your token to be, X or O?")
        return token 


    
#def main():
    #while True:


p1 = game()
print(p1)

'''
get player names
player 1 goes first
    place 'x' at some location
    update that position in the row
ask player where they want to 
'''

