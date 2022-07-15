import pandas as pd
import random
import numpy as np
class Die():
    """
    Purpose: To create a die that has N sides, or “faces”, and W weights, 
    and can be rolled to select a face.
    """
    def __init__(self,faces):
        """
        Input: An array of faces as an argument. 
        The array's data type (dtype) may be strings or numbers.
        Purpose: Instantiates the die object, internally initializes 
        all weights as 1 
        Output: Saves the die object to a private dataframe
        """
        weights = [1.0] * len(faces)
        self.face_list = faces
        self._die = pd.DataFrame({'faces':faces,'weights':weights})
    def change_weight(self,val,weight):
        """
        Input: The face value to be changed and the new weight.
        Purpose: Change the weight of a single side of the die
        Output: Updates a specifc face in the die object with the new weight
        """
        test = self._die[self._die.faces == val]
        if len(test)!=0:
            try:
                weight = float(weight)
                self._die.loc[self._die.faces==val,'weights'] = weight
            except:
                print("Weight must be a number")
        else:
            print("Face is not valid")
            return
    def roll(self,num_time=1):
        """
        Input: Parameter of how many times the die is to be rolled; 
        defaults to 1.
        Purpose: Randomly sample from the vector of faces according to the 
        weights
        Output: A list of outcomes
        """
        return random.choices(self._die.faces,\
                              weights = self._die.weights,k=num_time)
    def show_die(self):
        """
        Input: None
        Purpose: Show the user the die’s current set of faces and weights
        Output: Returns the dataframe created in the initializer
        """
        return(self._die)

class Game():
    """
    Purpose: A game consists of rolling of one or more dice 
    of the same kind one or more times. Each die in a given game 
    has the same number of sides and associated 
    faces, but each die object may have its own weights.
    The class rolls all the dice a given number of times, and stores the 
    results of the most recent game
    """
    def __init__(self,lst):
        """
        Input: a list of Die objects
        Purpose: Instantiate a Game object
        Output: Stores the list of Die objects
        """
        self.lst = lst
    def play(self,num_roll): #issue is here
        """
        Input: Parameter to specify how many times the dice should be rolled
        Purpose: Rolls the dice the specified number of times and saves 
        the result of the play
        Output: A private dataframe of shape N rolls by M dice
        """
        self._results = pd.DataFrame(index=range(1,num_roll+1))
        self._results.index.rename("Roll Number",inplace=True)
        count = 0
        for die in self.lst:
            die_played = die.show_die()
            self._results["Die Result " + str(count)]\
            = die.roll(num_roll)
            count +=1
    def show_play(self,form="wide"):
        """
        Input: Parameter to return the dataframe in narrow or wide form.
        Defaults to wide form
        Purpose: Show the user the results of the most recent play
        Output: The private dataframe recording the game results
        """
        if form.lower()=='wide':
            return self._results
        elif form.lower()=='narrow':
            self._results_narrow = self._results.reset_index()
            return pd.wide_to_long(self._results_narrow,\
            stubnames='Die Result ',i = ['Roll Number'], j='Die Number')
        else:
            print("Form must be wide or narrow")
            return

class Analyzer():
    """
    Purpose: An analyzer takes the results of a single game and computes 
    various descriptive statistical properties about it. 
    These properties results are available as attributes of an Analyzer object.
    """
    def __init__(self, game):
        """
        Input: A game object
        Purpose: Initializes the Analyzer object
        Output: Stores the game object and the last recorded play
        """
        self.game_results = game.show_play('wide')
        self.game = game
    def jackpot(self):
        """
        Input: None
        Purpose: Computes how many times the game resulted in all 
        faces being identical. 
        Output: Stores the jackpot results in a public attribute.
        Returns an integer for the number of times to the user.
        """
        count = 0
        self.jackpot_results = pd.DataFrame(index=range(1,\
                                len(self.game_results)\
                                +1),columns=["Jackpot"])
        self.jackpot_results.index.rename("Roll Number",inplace=True)
        for i in range(1,len(self.game_results)+1):
            test = self.game_results.loc[i]
            counts = test.value_counts().tolist()
            if counts[0]==len(test): #compare results across n die
                self.jackpot_results.Jackpot[i] = True
                count += 1
            else:
                self.jackpot_results.Jackpot[i] = False 
            
        return count
    def combo(self):
        """
        Input: None
        Purpose: Compute the distinct combinations of faces rolled, 
        along with their counts
        Output: Sorts and stores the combinations as a dataframe in a
        public attribute.
        """
        self.combo_results = self.game_results.apply\
        (lambda x: pd.Series(sorted(x)), 1)\
         .value_counts()\
         .to_frame('n')
    def face_counts_per_roll(self):
        """
        Input: None
        Purpose: Compute how many times a given face is rolled in each event
        Output: Stores the results as a dataframe in a public attribute.
        """
        self.face_counts = pd.DataFrame(index=range(1,len(self.game_results)+1))
        self.face_counts.index.rename("Roll Number",inplace=True)        
        #makes a labeled dataframe of all zeros
        for i in self.game.lst[0].face_list:
            self.face_counts['Face ' + str(i)] = np.zeros(len(self.game_results))
        for index, row in self.game_results.iterrows():
            for entry in self.game_results.loc[index]:
                self.face_counts.loc[index,'Face ' + str(entry)] += 1