# -*- coding: utf-8 -*-
"""BA5A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Ew_VfzI0n95rO_-nWPV21uy20wgmmoO
"""

import math
def DPChange(money,coins):
  minNumCoins=[math.inf] * (money+1)
  minNumCoins[0]=0
  for m in range(1, money+1):
    for i in range(0,len(coins)):
      if (m >= coins[i]):
        if (minNumCoins[m-coins[i]] + 1 < minNumCoins[m]):
          minNumCoins[m] = minNumCoins[m-coins[i]] + 1
  return minNumCoins[money]

DPChange(17704, [1,3,5,15])