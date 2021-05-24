import numpy as np
import pandas as pd
import random
import math

#Assign people to universes

random.seed(0)

ppl = ["A","B","C","D","E","F","G","NPC"]

random.shuffle(ppl)

universeAppl=ppl[0:4]
universeBppl=ppl[4:8]

print(ppl)
print(universeAppl, universeBppl)

#Set up bids, set up budgets, add NPC

random.seed(0)

bidDict={
"A":[1]*20,
"B":[1]*20,
"C":[76,36,13,26,21,51,18,13,9,12,9,18,102,21,26,31,13,41,13,36],
"D":[50,36,13,25,19,62,17,13,1,11,1,19,85, 20,20,20,13,10,13,20],
"E":[73,34,15,21,17,57,16,15,6,11,6,15,8,  17,28,31,15,42,15,34],
"F":[73,35,14,22,14,63,16,7, 5,10,2,18,4,  14,29,29,10,44,14,34],
"G":[71,33,16,24,20,51,19,16,9,15,9,18,12, 20,26,31,16,42,16,33],
"NPC":[]}

for i in range(20):
 copiedCat=random.choice(["A","B","C","D","E","F","G"])
 bidDict["NPC"].append(bidDict[copiedCat][i])

print(bidDict)

budgetDict={"A":300,"B":300,"C":300,"D":300,"E":300,"F":300,"G":300,"NPC":300}


#Lights, camera, auction!

def auction(bidders):
 winners=[]
 for i in range(20):
  bids=[]
  for bidder in bidders:
   if bidDict[bidder][i]<=budgetDict[bidder]:
    bids.append(bidDict[bidder][i])
  print(i)
  print(bids)
  possibleWinners=[]
  for bidder in bidders:
   if bidDict[bidder][i]==max(bids) and bidDict[bidder][i]<=budgetDict[bidder]:
    possibleWinners.append(bidder)
  if len(possibleWinners)>0:
   winner = random.choice(possibleWinners)
   budgetDict[winner]-=bidDict[winner][i]
   winners.append(winner)
  else:
   winners.append("NONE")
 return winners

random.seed(0)
universeAwinners=auction(universeAppl)
print(universeAwinners)
random.seed(0)
universeBwinners=auction(universeBppl)
print(universeBwinners)

print(budgetDict)

#And to the victors go the spoils . . .

values = [101,39,13,25,26,61,16,28,9,28,0,13,18,31,37,40,25,55,0,40]

def reward_winners(winners):
 for i in range(20):
  if winners[i]!="NONE":
   budgetDict[winners[i]]+=values[i]

reward_winners(universeAwinners)
reward_winners(universeBwinners)
print(budgetDict)
