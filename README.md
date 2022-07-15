# final_project
# Metadata
Montecarlo Simulator created by Aubrey Winger
# Synopsis
 - The package can be installed by downloaded it off of GitHub, navigating to the folder "montecarlo_package" in Terminal, and typing the command `!pip install -e .`
 - The three classes included in this module are Die, Game and Analyzer. These can be imported using the following commands: `from montecarlo.montecarlo import Die', 'from montecarlo.montecarlo import Game' and 'from montecarlo.montecarlo import Analyzer'
 - To create a new die object, instantiate the Die with a list of faces. The faces can either be strings or integers. 
 - Example: `myDie = Die([1,2,3,4,5])` or `myDie2 = Die(['H','T'])
 - To play a game, instantiate the Game with a list of Die objects, which will be used to play the game. These die objects must all have the same faces, but these faces may have unique weights
 - Example `myGame = Game([myDie, myDie3])
 - To analye a game, instantiate the Analyzer object with your game object. This class calculates various attributes about a single game.
 - Example `myAnalyzer = Analyzer(myGame)`
 # API Description
 
