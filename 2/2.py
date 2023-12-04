import re

maxCounts = [
  ('red', 12),
  ('green', 13),
  ('blue', 14)
]

def main():
  with open('2.txt') as f:
    lines = f.readlines()
    gamesPossible = []
    gamePowers = []

    for line in lines:
      possible = isLinePossible(line.strip())
      gamePower = getGamePowers(line.strip())
      gamePowers.append(gamePower)

      if possible:
        # add game ID to array
        gameId = getFirstDigi(line.strip())
        if gameId:
          gamesPossible.append(gameId)

    print(gamesPossible, "\n")

    gameIdTotalCount = sum(gamesPossible)
    print(gameIdTotalCount, "\n") 

    print(gamePowers, "\n")

    gamePowersTotalCount = sum(gamePowers)
    print(gamePowersTotalCount, "\n")   


def isLinePossible(line):
  linePossible = True
  normalizedLine = line.lower()
  lineSplit = normalizedLine.split(":", 1)
  games = lineSplit[1].split(";")

  for game in games:
    cubes = game.split(',')
    # print(game)
    for cubeCount in cubes:
      for (color, maxCount) in maxCounts:
        if (cubeCount.find(color) != -1):
          countDigi = getFirstDigi(cubeCount)
          if (countDigi > maxCount):
            linePossible = False
            # print("line not possible!")
            return linePossible

  return linePossible

def getGamePowers(line):
  normalizedLine = line.lower()
  lineSplit = normalizedLine.split(":", 1)
  games = lineSplit[1].split(";")

  maxRed = 1
  maxGreen = 1
  maxBlue = 1

  for game in games:
    cubes = game.split(',')
    for cubeCount in cubes:
      for (color, maxCount) in maxCounts:
        if (cubeCount.find(color) != -1):
          countDigi = getFirstDigi(cubeCount)

          if color == 'red':
            if countDigi > maxRed:
              maxRed = countDigi
          if color == 'green':
            if countDigi > maxGreen:
              maxGreen = countDigi
          if color == 'blue':
            if countDigi > maxBlue:
              maxBlue = countDigi

  return maxRed * maxGreen * maxBlue

def getFirstDigi(line):
  m = re.search(r"\d+", line.lower())
  return int(m.group(0))

if __name__ == "__main__":
  main()