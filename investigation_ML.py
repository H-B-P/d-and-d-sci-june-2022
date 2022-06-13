import xgboost as xgb
import pandas as pd

df = pd.read_csv('dset.csv')

#df = df[df["Collaborator"]=="Chaos Deity"]

for u in df["Cheat Skill 1"].unique():
 df[u] = (df["Cheat Skill 1"]==u) + (df["Cheat Skill 2"]==u)


cheats=['Monstrous Regeneration', 'Mind Palace', 'Barrier Conjuration', 'Enlightenment', 'Uncanny Luck', 'Hypercompetent Dark Side', 'Rapid XP Gain', 'Shapeshifting', 'Anomalous Agility', 'Temporal Distortion', 'Radiant Splendor']


X = df[["Sociopath?","Nerd?","Otaku?","Hikkikomori?","Office Worker?"]+cheats]

y = df["Hero Defeats Demon King?"].replace("Yes",1).replace("No",0)

dtrain = xgb.DMatrix(X, label=y)
param = {'max_depth':3, 'eta':0.5, 'objective':'binary:logistic'}
model = xgb.train(param,dtrain, 500)

testDf = pd.DataFrame({"Sociopath?":0,"Nerd?":1,"Otaku?":0,"Hikkikomori?":0,"Office Worker?":1,
 'Monstrous Regeneration':1,
 'Mind Palace':1,
 'Barrier Conjuration':0,
 'Enlightenment':0,
 'Uncanny Luck':0,
 'Hypercompetent Dark Side':0,
 'Rapid XP Gain':0,
 'Shapeshifting':0,
 'Anomalous Agility':0,
 'Temporal Distortion':0,
 'Radiant Splendor':0}, index=[0])

model.predict(xgb.DMatrix(testDf))


for cheat1 in cheats:
 for cheat2 in cheats:
  if cheat1!=cheat2:
   testDf = pd.DataFrame({"Sociopath?":0,"Nerd?":1,"Otaku?":0,"Hikkikomori?":0,"Office Worker?":1,
   'Monstrous Regeneration':0,
   'Mind Palace':0,
   'Barrier Conjuration':0,
   'Enlightenment':0,
   'Uncanny Luck':0,
   'Hypercompetent Dark Side':0,
   'Rapid XP Gain':0,
   'Shapeshifting':0,
   'Anomalous Agility':0,
   'Temporal Distortion':0,
   'Radiant Splendor':0}, index=[0])
   testDf[cheat1]=1
   testDf[cheat2]=1
   print(cheat1,cheat2,model.predict(xgb.DMatrix(testDf))[0])

