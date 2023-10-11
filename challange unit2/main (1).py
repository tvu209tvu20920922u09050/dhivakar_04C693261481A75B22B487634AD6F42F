'''implement a class called player that represents a cricket. The player class should have a
method caalled play () which prints "The player is playing cricket.Derive two classes. Batssman and 
Bowler, from the player class.overridde the play() method in each derived calss to rptint "The batsman
is batting" and"Tghe bowler is bowling", respective.writee a program to creaate objects of both the 
Batsman and Bowler classes and call the play() method for each object.'''


class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes and call the play() method for each object.
batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()