class StringUtility:
  def __init__(self,string):
    self.string = string

  def __str__(self):
    return self.string
  def vowels(self):
    count = 0
    set = "aeiouAEIOU"
    for i in range(len(self.string)):
      if str(self.string)[i] in set:
        count += 1
    if count >= 5:
      vowelcount = "many"
    else:
      vowelcount = str(count)
    return vowelcount

  def bothEnds(self):
    if len(self.string) >= 2:
      newstring = str(self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
    else:
      newstring = str('')
    return newstring

  def fixStart(self):
    letterlst = list(self.string)
    if len(self.string) > 1:
      for i in range(1, len(self.string)):
        if self.string[i] == self.string[0]:
          letterlst[i] = "*"
    newself = str("".join(letterlst))
    return newself

  def asciiSum(self):
    sum = 0
    for i in range(len(self.string)):
      sum += ord(self.string[i])
    return sum

  def cipher(self):
    encodedstr = ''
    length = len(self.string)
    for ch in self.string:
      num = ord(ch)
      if ord(ch) >= 65 and ord(ch) <= 90:
        num -= 65
        encodedstr += chr(((num + length)%26)+65)
      elif ord(ch) >= 97 and ord(ch) <= 122:
        num -= 97
        encodedstr += chr(((num+length)%26)+97)
      else:
        encodedstr += ch
    return encodedstr