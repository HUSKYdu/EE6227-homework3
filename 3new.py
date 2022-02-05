import random as rd
import math
import matplotlib.pyplot as plt
import datetime
from enum  import Enum
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
In particular, it should be noted that due to the characteristics of the genetic algorithm, 
the program may take an extremely long time to run. 
The 261 loops given in the job report are a very special case. 
The time spent on the other two solutions in the report It takes more than 50 minutes, 
so if you want to use this program to get answers, 
please prepare enough time and make sure your computer performance can meet the requirements
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

just run the program, we need !python 3.8!
'''


def get_individual():
    individual=[]
    #an individual has 8 queens
    for i in range(0,8):
        flag=0
        while flag==0:
            # give the position of a queen, 8*8=64-position is 0-63
            a=rd.randint(0,63)
            #if the position isn's existing in current list , then we add it ,or we should cycle
            if individual.count(a)>0:
                continue
            else:
                individual.append(a)
                flag=1
    return individual
def get_group(num):
    group=[]#get num of individual and save in a list named group
    for i in range(0,num):
        group.append(get_individual())
    return group

def row_defi(a,all):
    alllen=len(all)
    defi=0
    for i in range(0,alllen):
        if a!=all[i]:#if two queen in same range of number , then they conflict
            if (a>=0 and a<=7) and (all[i]>=0 and all[i]<=7):
                defi=defi+1
            if (a>=8 and a<=15) and (all[i]>=8 and all[i]<=15):
                defi=defi+1
            if (a>=16 and a<=23) and (all[i]>=16 and all[i]<=23):
                defi=defi+1
            if (a>=24 and a<=31) and (all[i]>=24 and all[i]<=31):
                defi=defi+1
            if (a>=32 and a<=39) and (all[i]>=32 and all[i]<=39):
                defi=defi+1
            if (a>=40 and a<=47) and (all[i]>=40 and all[i]<=47):
                defi=defi+1
            if (a>=48 and a<=55) and (all[i]>=48 and all[i]<=55):
                defi=defi+1
            if (a>=56 and a<=63) and (all[i]>=56 and all[i]<=63):
                defi=defi+1
    return defi
def col_defi(a,all):
    alllen = len(all)
    defi = 0
    for i in range(0,alllen):
        if a!=all[i]:
            for j in range(1,9):
                if a+8*j==all[i]:
                    defi=defi+1
                if a-8*j==all[i]:
                    defi=defi+1
    return defi
def pos_defi(a,all):
    alllen = len(all)
    defi = 0
    for i in range(0,alllen):
        if a!=all[i]:
            for j in range(1,9):
                if a+7*j==all[i]:
                    defi=defi+1
                if a-7*j==all[i]:
                    defi=defi+1
    return defi
def neg_defi(a,all):
    alllen = len(all)
    defi = 0
    for i in range(0,alllen):
        if a!=all[i]:
            for j in range(1,9):
                if a+9*j==all[i]:
                    defi=defi+1
                if a-9*j==all[i]:
                    defi=defi+1
    return defi
def suit_func(pos):
    xlen = len(pos)
    full = 49#we believe that the baddest condition is each queen are conflict to all other seven queens,
    #so the highest conflict number is 7*7=49
    defi = 0
    for i in range(0, xlen):
        defi_row = row_defi(pos[i], pos)
        defi_col = col_defi(pos[i], pos)
        defi_pos = pos_defi(pos[i], pos)
        defi_neg = neg_defi(pos[i], pos)
        defi = defi + defi_row + defi_col + defi_pos + defi_neg#add all of conflict number
    score = ((full - defi) / full) * 100#get the score
    return score

def percent(score):
    score_sum=sum(score)
    slen=len(score)
    pere=[]
    for i in range(0,slen):
        pere.append(score[i]/score_sum)
    return pere
def genetic(group):
    grouplen = len(group)
    score = []
    for i in range(0, grouplen):
        score.append(suit_func(group[i]))
    perc = percent(score)
    plen = len(perc)

    offspring = []
    for i in range(0, plen):
        x = rd.randint(1, 99)
        x = x / 100
        for k in range(0, 20):
            s = 0
            flag = 0
            for j in range(0, k + 1):
                s = s + perc[j]
                if x <= s:
                    offspring.append(group[k])
                    flag = 1
                    break
            if flag == 1:
                break

    return offspring

def corssover_posotion():
    a=rd.randint(0,7)
    return a
def crossover(i1,i2):
    pos=corssover_posotion()
    if pos==0:
        return i1,i2
    else:
        j1=[]
        j2=[]
        for h in range(pos,8):
            j1.append(i1[h])
            j2.append(i2[h])
        for k in range(0,8):
            if j1.count(i2[k])==0 and len(j1)<8:
                j1.append(i2[k])
            if j2.count(i1[k])==0 and len(j2)<8:
                j2.append(i1[k])

    return j1,j2
def gourp_corssover(group):
    glen=len(group)
    groupcopy=group.copy()
    for i in range(0,int((glen/2))):
        groupcopy[2*i],groupcopy[2*i+1]=crossover(group[2*i],group[2*i+1])
    return groupcopy

def mutation_condition():
    k=[]
    for i in range(0,33):
        if i==0:
            k.append(1)
        else:
            k.append(0)
    cond=rd.randint(0,32)
    cond=k[cond]
    return cond
def mutation_position():
    pos=rd.randint(0,7)
    return pos
def mutation(individual):
    individualcopy=individual.copy()
    mc=mutation_condition()
    if mc==1:
        mp=mutation_position()
        while 1:
            x=rd.randint(0,63)
            if individual.count(x)==0:
                individualcopy[mp]=x
                break
        return individualcopy
    else:
        return individualcopy



def Main():
    group=get_group(20)
    print('Population Initial Complete:')
    print(group)
    t=0
    while 1:
        t=t+1
        print('Start Generite',t,'cycle')
        group=genetic(group)
        group=gourp_corssover(group)
        for i in range(0,len(group)):
            group[i]= mutation(group[i])
        score=[]
        for j in range(0,len(group)):
            score.append(suit_func(group[j]))
        if max(score)==100:
            print('One of The Solution is ')
            for k in range(0,len(group)):
                if score[k]==100:
                    print(group[k])
            break

        else:
            print('The Highest Score is:',max(score))
            print('End', t, 'Cycle>>>>>>>>>>>>>>>>>>>>>>')

Main()