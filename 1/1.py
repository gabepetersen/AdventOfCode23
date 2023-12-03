import math

numbers = [
  ('one', '1'),
  ('two', '2'),
  ('three', '3'),
  ('four', '4'),
  ('five', '5'),
  ('six', '6'),
  ('seven', '7'),
  ('eight', '8'),
  ('nine', '9')
]

def main():
  totalCount = 0

  with open('1.txt') as f:
    lines = f.readlines()
    for line in lines:
      print(line.strip())
      sanitizedLine = normalizeDigis(line.strip())
      
      firstDigi = ""
      lastDigi = ""
      calibValue = ""
      for digi in sanitizedLine:
        if digi.isdigit():
          if len(firstDigi) == 0:
            firstDigi = digi
          lastDigi = digi
      
      calibValue = firstDigi + lastDigi
      print(calibValue)

      if len(calibValue) != 0:
        totalCount += int(calibValue)

  print(totalCount)

def normalizeDigis(line):
  normalizedLine = line.lower()
  resultString = "" 

  for index, digi in enumerate(normalizedLine):
    if digi.isdigit():
      resultString += digi
    else:
      for (full, short) in numbers:
        if normalizedLine.startswith(full, index):
          resultString += short

  print(resultString)

  return resultString

def insertCharacter(str, addedString, index):
  return str[:index] + addedString + str[index:]


if __name__ == "__main__":
  main()