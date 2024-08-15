import random
from scipy import stats
numGames = 1273
lyndsayWin = 666
numTrials = 10000
atLeast = 0
for t in range(numTrials):
    LWins, JWins = 0
    for g in range(numGames):
        if random.random() < 0.5:
            LWins += 1
        else:
            JWins += 1
    if LWins >= lyndsayWin or JWins >= lyndsayWin:
        atLeast += 1
print('Probability of result at least this', 'exterme by accident =', atLeast/numTrials)
