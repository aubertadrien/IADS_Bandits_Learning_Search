# ------------------------------------------
# Tom Vodopivec
#
# IADS Analytics, Data Science & Decision Making  Summer School 2022
# Course: Bandits, Learning, and Search
# 2022-08-01
#
# ------------------------------------------

#-- imports --#
from BanditSpecs import *
from BanditGenerator import *
from Agent import *
from Evaluator import *


###--- main program ---###

##-- generate all bandits
allCases = generateBandits(BANDITSPECS, suppress_output = 1)

##-- build evaluation Tests from generated bandits
testBatch_All = BanditTestBatch(allCases, range(len(allCases))) 	#All
testBatch_01_05 = BanditTestBatch(allCases, [0, 1, 2, 3, 4])  	#Example subset: first 5 cases

##-- agent configuration
solver = Agent(banditPolicy.RANDOM)

##-- evaluation
cases = testBatch_01_05
suppress_output = 0
num_repeats = 10
results = evaluate(solver, cases, num_repeats, suppress_output)

print('Your selected algorithm: reward: %.1f' % results[0][0])