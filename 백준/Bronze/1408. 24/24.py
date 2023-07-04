currentTime = input()
startTime = input()

hour = 0
min = 0
sec = 0
totalTime = 0

totalTime = int(startTime[0:2]) * 3600 - int(currentTime[0:2]) * 3600
totalTime += int(startTime[3:5]) * 60 - int(currentTime[3:5]) * 60
totalTime += int(startTime[6:8]) - int(currentTime[6:8])

if totalTime < 0:
  totalTime += 60 * 60 * 24
hour = totalTime // 3600
totalTime %= 3600
min = totalTime // 60
totalTime %= 60
sec = totalTime
print("%02d:%02d:%02d" % (hour, min, sec))
