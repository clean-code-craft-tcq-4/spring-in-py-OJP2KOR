import math

def calculateStats(numbers):
  if( numbers == [] ):
    return { "avg" : math.nan, "max" : math.nan, "min" : math.nan }
  return {"avg" :sum(numbers)/len(numbers), "max" : max(numbers), "min" : min(numbers)}
