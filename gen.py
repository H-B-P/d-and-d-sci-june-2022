import random
import pandas as pd


cheats = ["Shapeshifting", "Enlightenment", "Uncanny Luck", "Temporal Distortion", "Hypercompetent Dark Side", "Rapid XP Gain", "Mind Palace", "Monstrous Regeneration","Radiant Splendor", "Barrier Conjuration", "Anomalous Agility"]
def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op

#

def gen_hero_traits():

 soc = random.choice([True]*131 + [False]*869) #13.1% Sociopath
 ner, ota = random.choice([[True,True]]*441 + [[True,False]]*82 + [[False,True]]*174 + [[False,False]]*303)
 hik, sal = random.choice([[True,True]]*31 + [[True,False]]*267 + [[False,True]]*400 + [[False,False]]*302)
 fated = random.choice([True]*191 + [False]*809)
 
 return soc, ner, ota, hik, sal, fated

def gen_hero_aptitude(soc,ner,ota,hik,sal): #Theoretical max is 23, we have 7-10
 if sal:
  apt=4+roll_dX(4)
 else:
  apt=2+roll_dX(8)
 
 if soc:
  apt+=1
 if ner:
  apt+=2
 if ota:
  apt+=4
 
 if hik:
  apt = apt + roll_dX(4) - roll_dX(4)
 
 return apt

def make_eldritch_choices():
 return ["Monstrous Regeneration", "Anomalous Agility"]

def make_chaos_choice():
 return random.choice(cheats)

def make_chaos_choices():
 c1 = make_chaos_choice()
 c2 = ""
 while c2 in ["", c1]:
  c2 = make_chaos_choice()
 return random.choice([[c1,c2],[c2,c1]])

def make_hero_choice(apt, soc, ner, ota, hik, sal, fated):
 if fated:
  return random.choice(["Shapeshifting"]*25
                     + ["Enlightenment"]*250
                     + ["Uncanny Luck"]*330
                     + ["Temporal Distortion"]*25
                     + ["Hypercompetent Dark Side"]*10
                     + ["Rapid XP Gain"]*50
                     + ["Mind Palace"]*25
                     + ["Monstrous Regeneration"]*10
                     + ["Radiant Splendor"]*240
                     + ["Barrier Conjuration"]*25
                     + ["Anomalous Agility"]*10)
 elif hik:
  return random.choice(["Shapeshifting"]*110
                     + ["Enlightenment"]*(10+apt*3)
                     + ["Uncanny Luck"]*80
                     + ["Temporal Distortion"]*90
                     + ["Hypercompetent Dark Side"]*(190-apt)
                     + ["Rapid XP Gain"]*60
                     + ["Mind Palace"]*(120+apt*2)
                     + ["Monstrous Regeneration"]*(80-apt*2)
                     + ["Radiant Splendor"]*20
                     + ["Barrier Conjuration"]*(130+apt)
                     + ["Anomalous Agility"]*(90-apt*3))
 elif ota:
  return random.choice(["Shapeshifting"]*(200+apt*2)
                     + ["Enlightenment"]*(20+apt)
                     + ["Uncanny Luck"]*(80+apt)
                     + ["Temporal Distortion"]*(90-apt)
                     + ["Hypercompetent Dark Side"]*(110-apt)
                     + ["Rapid XP Gain"]*130
                     + ["Mind Palace"]*(20+apt)
                     + ["Monstrous Regeneration"]*(100-apt)
                     + ["Radiant Splendor"]*(50-apt)
                     + ["Barrier Conjuration"]*80
                     + ["Anomalous Agility"]*(90-apt))
 else:
  return random.choice(["Shapeshifting"]*120
                     + ["Enlightenment"]*30
                     + ["Uncanny Luck"]*150
                     + ["Temporal Distortion"]*(90+2*apt)
                     + ["Hypercompetent Dark Side"]*90
                     + ["Rapid XP Gain"]*(120+apt)
                     + ["Mind Palace"]*60
                     + ["Monstrous Regeneration"]*(100-2*apt)
                     + ["Radiant Splendor"]*40
                     + ["Barrier Conjuration"]*90
                     + ["Anomalous Agility"]*(110-apt))

def make_hero_choices(apt, soc, ner, ota, hik, sal, fated):
 c1 = make_hero_choice(apt, soc, ner, ota, hik, sal, fated)
 c2 = ""
 while c2 in ["", c1]:
  c2 = make_hero_choice(apt, soc, ner, ota, hik, sal, fated)
 return random.choice([[c1,c2],[c2,c1]])

def get_power(apt, soc, ner, ota, hik, sal, c1, c2):
 
 if "Hypercompetent Dark Side" in [c1,c2]:
  apt=max(apt,11)
  apt=apt+1
 
 if "Shapeshifting" in [c1,c2]:
  apt+=2
  if ota:
   apt+=5
  if soc:
   apt+=4
 
 if "Enlightenment" in [c1,c2]:
  apt+=2
  if "Radiant Splendor" in [c1,c2]:
   apt+=4
 
 if "Uncanny Luck" in [c1,c2]:
  apt+=4
  if ner:
   apt-=2
 
 if "Temporal Distortion" in [c1,c2]:
  apt+=2
  if ner:
   apt+=4
 
 if "Rapid XP Gain" in [c1,c2]:
  apt+=3
  if sal:
   apt+=2
 
 if "Monstrous Regeneration" in [c1,c2]:
  apt+=5
  if "Barrier Conjuration" in [c1,c2] or "Anomalous Agility" in [c1,c2]:
   apt-=2
 
 if "Radiant Splendor" in [c1,c2]:
  apt+=2
  if soc:
   apt+=2
 
 if "Barrier Conjuration" in [c1,c2]:
  apt+=5
  if "Monstrous Regeneration" in [c1,c2] or "Anomalous Agility" in [c1,c2]:
   apt-=2
 
 if "Anomalous Agility" in [c1,c2]:
  apt+=5
  if "Monstrous Regeneration" in [c1,c2] or "Barrier Conjuration" in [c1,c2]:
   apt-=2
 
 if "Mind Palace" in [c1,c2]:
  apt+=4
  if hik:
   apt=0
 
 return apt

def hero_wins(power,f):
 if f:
  return "Yes"
 proll = roll_NdX(power, 10)
 if proll>90:
  return "Yes"
 return "No"

def gen_dset(revealing=True):
 ids=[]
 
 socs=[]
 ners=[]
 otas=[]
 hiks=[]
 sals=[]
 fs=[]
 
 apts=[]
 
 c1s=[]
 c2s=[]
 
 collabs=[]
 
 powers=[]
 
 wins=[]
 
 for i in range(1,307642):
  if i%10000==0:
   print(i)
  ids.append(i)
  
  soc, ner, ota, hik, sal, f = gen_hero_traits()
  
  apt = gen_hero_aptitude(soc,ner,ota,hik,sal)
  
  socs.append(soc)
  ners.append(ner)
  otas.append(ota)
  hiks.append(hik)
  sals.append(sal)
  fs.append(f)
  
  apts.append(apt)
  
  if i<17841:
   collab = "Eldritch Abomination"
   c1,c2 = make_eldritch_choices()
  elif i<50434:
   collab = "Chaos Deity"
   c1,c2 = make_chaos_choices()
  else:
   collab = "None"
   c1,c2 = make_hero_choices(apt,soc, ner, ota, hik, sal, f)
  
  c1s.append(c1)
  c2s.append(c2)
  collabs.append(collab)
  
  power = get_power(apt, soc, ner, ota, hik, sal, c1, c2)
  
  powers.append(power)
  
  win = hero_wins(power, f)
  
  wins.append(win)
 
 print(len(ids))
 print(len(socs))
 print(len(ners))
 print(len(otas))
 print(len(hiks))
 print(len(sals))
 print(len(apts))
 print(len(c1s))
 print(len(c2s))
 print(len(powers))
 print(len(wins))
 
 if revealing:
  dictForDf = {"Hero ID":ids,"Sociopath?":socs, "Nerd?":ners, "Otaku?":otas, "Hikkikomori?":hiks, "Office Worker?":sals, "Fated?":sals, "Aptitude":apts, "Cheat Skill 1":c1s, "Cheat Skill 2":c2s, "Power":powers, "Collaborator":collabs, "Hero Defeats Demon King?":wins}
 else:
  dictForDf = {"Hero ID":ids,"Sociopath?":socs, "Nerd?":ners, "Otaku?":otas, "Hikkikomori?":hiks, "Office Worker?":sals, "Cheat Skill 1":c1s, "Cheat Skill 2":c2s, "Collaborator":collabs, "Hero Defeats Demon King?":wins}
 df = pd.DataFrame(dictForDf)
 
 print(df)
 df.to_csv('dset.csv') 

gen_dset(False)
