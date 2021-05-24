import numpy as np
import pandas as pd
import random
import math

def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op

def triangle_roll_dis(X):
 return min(roll_dX(X), roll_dX(X))

def triangle_roll_adv(X):
 return max(roll_dX(X), roll_dX(X))



def gen_days():
 return triangle_roll_dis(10)
  



def gen_beetle(days):
 x = 1
 while True:
  r = roll_dX(6)
  if r==1:
   return x
  elif r==6:
   x*=2
  else:
   x+=r

def gen_mild_boar(days):
 rolls=[roll_dX(4),roll_dX(8),roll_dX(12), roll_dX(20)]
 val=0
 for roll in rolls:
  if roll>days:
   val+=roll
 return val

def gen_jungle_mammoth(days):
 return 20+roll_NdX(10,4)-3*days

def gen_dragon(days):
 scales = roll_NdX(5,8)
 tongue = 10*(days<3)
 heart = 30*(days<5)
 spleen = 5*(days<7)
 return scales+tongue+heart+spleen

def gen_red_dragon(days):
 scales = 2*roll_NdX(5,8)
 tongue = 10*(days<3)
 heart = 30*(days<5)
 spleen = 5*(days<7)
 return scales+tongue+heart+spleen

vfuncLookup={"Jewel Beetle":gen_beetle, "Mild Boar":gen_mild_boar, "Jungle Mammoth":gen_jungle_mammoth, "Green Dragon":gen_dragon, "Gray Dragon":gen_dragon, "Blue Dragon":gen_dragon, "Red Dragon":gen_red_dragon}

dictForDf = {"Species":[], "Days Since Death":[], "Revenue From Selling Components":[]}

selector = ["Jewel Beetle"]*5 + ["Mild Boar"]*41 + ["Jungle Mammoth"]*31 + ["Green Dragon"]*5 + ["Gray Dragon"]*2 + ["Blue Dragon"]*8 +["Red Dragon"]*8

df=pd.DataFrame(dictForDf)

random.seed(0)

for i in range(840):
 species = random.choice(selector)
 value_func = vfuncLookup[species]
 days = gen_days()
 value = value_func(days)
 
 newRow = {"Species": species, "Days Since Death":str(int(days)), "Revenue From Selling Components":str(int(value))+"sp"}
  
 df=df.append(newRow, ignore_index=True)

df=df[["Species", "Days Since Death", "Revenue From Selling Components"]]

print(df)

df.to_csv("dset.csv")






random.seed(1234)

tot=0

for i in range(20):
 species = random.choice(selector)
 value_func = vfuncLookup[species]
 days = gen_days()
 value = value_func(days)
 
 tot+=value
 print(str(i+1), species, days, value)
 
print(tot)
