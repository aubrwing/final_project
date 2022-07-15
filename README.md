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
 __Class Die()__
 \
 Purpose: To create a die that has N sides, or “faces”, and W weights, and can be rolled to select a face.
 \
 Methods: 
\
__init(faces)__
 - Input: An array of faces as an argument. The array's data type (dtype) may be strings or numbers. 
 - Purpose: Instantiates the die object, internally initializes all weights as 1. 
 - Output: Saves the die object
 \
 __change_weight(val,weight)__
- Input: The face value to be changed and the new weight. The face value must be included in the array of face values, and the weight must be a number.
- Purpose: Change the weight of a single side of the die
- Output: Updates a specifc face in the die object with the new weight
\
__roll(num_time=1)__
- Input: Parameter of how many times the die is to be rolled; defaults to 1. Must be an integer.
- Purpose: Randomly sample from the vector of faces according to the weights
- Output: Returns a list of outcomes
\
__show_die()__
- Input: None
- Purpose: Show the user the die’s current set of faces and weights
- Output: Returns the dataframe created in the initializer
\
\
__Class Game()__
\
 Purpose: A game consists of rolling of one or more dice of the same kind one or more times. Each die in a given game has the same number of sides and associated faces, but each die object may have its own weights.The class rolls all the dice a given number of times, and stores the results of the most recent game
 \
 Methods:
 \
 __init(lst)__
 - Input: a list of Die objects
 - Purpose: Instantiate a Game object
 - Output: Stores the list of Die objects
 \
 __play(num_roll)__
 - Input: Parameter to specify how many times the dice should be rolled
 - Purpose: Rolls the dice the specified number of times
 - Output: None
 \
 __show_play(form="wide")
 - Input: Parameter to return the dataframe in narrow or wide form. Defaults to wide form
- Purpose: Show the user the results of the most recent play of dice
- Output: Returns a dataframe recording the game results
\
\
__Analyzer__
\
Purpose: An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object.
\
Methods:
\
__init__(game)
- Input: A game object
- Purpose: Initializes the Analyzer object
- Output: Stores the game object and the last recorded play
\
__jackpot()__
- Input: None
- Purpose: Computes how many times the game resulted in all faces being identical. 
- Output: Stores the jackpot results in a public attribute. Returns an integer for the number of times to the user.
\
__combo()__
- Input: None
- Purpose: Compute the distinct combinations of faces rolled, along with their counts
- Output: Sorts and stores the combinations as a dataframe in a public attribute.
\
__face_counts_per_roll()__
- Input: None
- Purpose: Compute how many times a given face is rolled in each event
- Output: Stores the results as a dataframe in a public attribute.
# Manifest
Root: .gitignore, license, README.md, montecarlo_demo.ipynb, montecarlo_package
\
montecarlo_package: montecarlo, .DS_Store, setup.py
montecarlo: .DS_Store, _\_init\_\_.py, montecarlo.py, montecarlo_results.txt, montecarlo_tests.py
