
import math


def calculate_d1(S, K, r, sigma, T):

   if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
      raise ValueError("All parameters must be positive.")
   

   a=math.log(S/K)
   b=r+((sigma**2)/2)*T

   c= sigma*math.sqrt(T)
   d1 = (a+b)/c
   return d1




def calculate_d2(d1, sigma, T):
   d2=d1-sigma*math.sqrt(T)
   return d2
