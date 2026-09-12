"""Flag values outside robust median/MAD limits."""
from __future__ import annotations
import statistics
def flags(values:list[float],window:int=5,z:float=3.5)->list[bool]:
 result=[]
 for index,value in enumerate(values):
  history=values[max(0,index-window):index]
  if len(history)<2:result.append(False);continue
  median=statistics.median(history);mad=statistics.median([abs(x-median) for x in history]);scale=1.4826*mad
  result.append(abs(value-median)>z*scale if scale else value!=median)
 return result
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(flags(p['values'],p.get('window',5),p.get('z',3.5))))
