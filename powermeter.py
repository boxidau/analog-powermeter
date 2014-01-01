import time

mFactor = 1257.07  # Mouse dx vector size per revolution
revkwh = 266.67     # Revolutions per kW Hour
sampleCount = 6    # Number of samples in moving average
sampleTime = 5.00  # Number of seconds per sample
mouse = file('/dev/input/mouse0') # Mouse input device

def toSigned(n):  
  return n - ((0x80 & n) << 1)  

def calcPower():
  return ((sum(samples)/mFactor) / sum(sampleTimes)) * 3600 * (1.00/revkwh)

samples = []
sampleTimes = []

while True:
  sampleTotal = 0;
  timeDiff = 0.00
  startTime = time.time()
  while timeDiff < sampleTime:
    status, dx, dy = tuple(ord(c) for c in mouse.read(3))  
    endTime = time.time()
    timeDiff = endTime - startTime
    dx = abs(toSigned(dx))  
    dy = abs(toSigned(dy))
    sampleTotal += dx + dy
 
  sampleTimes.append(timeDiff)
  samples.append(sampleTotal)
  
  if len(samples) > sampleCount: 
    sampleTimes.pop(0)
    samples.pop(0)
  
  print calcPower()


