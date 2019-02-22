#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb

@author: Gobind
"""
import numpy as np
balls=0
wickets=3
temp=""
striker="Kirat Boli"
non_striker="N.S Nodhi"
team_score=0
while (balls<24 and wickets >=1 ):
    balls=balls+1
    if striker=="Kirat Boli":
        x=np.random.choice(np.arange(0, 8), p=[0.05, 0.3, 0.25, 0.1, 0.15, 0.01,0.09,0.05])
    elif striker=="N.S Nodhi":
        x=np.random.choice(np.arange(0, 8), p=[0.1, 0.4, 0.2, 0.05, 0.1, 0.01,0.04,0.1])
    elif striker=="R Rumrah":
        x=np.random.choice(np.arange(0, 8), p=[0.2, 0.3, 0.15, 0.05, 0.05, 0.01,0.04,0.2])
    elif striker=="Shashi Henra":
        x=np.random.choice(np.arange(0, 8), p=[0.3, 0.25, 0.05, 0.0, 0.05, 0.01,0.04,0.3])
#    print(x)
    if x==7:
        wickets=wickets-1
        print(str(int(balls/6))+"."+str(int(balls%6))+"   "+striker + " is out!!!!!")
        if wickets < 1:
            print("***********ALL OUT************")
            break
        if wickets==2:
            striker="R Rumrah"
        if wickets==1:
            striker="Shashi Henra"
        print("Next Batsman on the field is   "+striker+".\n")
    else:
        team_score=team_score+x
        print(str(int(balls/6))+"."+str(int(balls%6))+"   "+striker+" scored "+str(x))
    if x==1 or x==3 or x==5:
        temp=striker
        striker=non_striker
        non_striker=temp
    if balls%6==0 and wickets >=1:
        temp=striker
        striker=non_striker
        non_striker=temp
        print("\nTeam Score at the end of the over "+str(int(balls/6))+" is "+str(team_score))
        print("Batsman on the other end is    "+non_striker)
        print("----------End of over. Its "+str(team_score)+" for "+str(3-wickets)+".--------\n")
print("Total runs scored by HYDIA is " +str(team_score)+".")
