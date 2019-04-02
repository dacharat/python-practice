from pprint import pprint
f = open('./Sample.csv', 'r')
line = f.readline()
line = f.readline()
data = []
while line != '': 
  row = line.split(" ")
  data += [{'Name': row[0], 
  'Platform': row[1],
  'License': row[2],
  'NbOfVersions': row[3],
  'Language': row[4],
  'Host': row[5],
  'Size': row[6],
  'Stars': row[7],
  'ReadmeFilename': row[8][:len(row[8])-1]
  }]
  line = f.readline()

print("=====================================================")

# 1.
def countPlatform(data) :
  platform = {}
  for i in data:
    if i['Platform'] in platform.keys(): 
      platform[i['Platform']] += 1
    else :
      platform[i['Platform']] = 1
    # print(i['Platform'])
  return sorted(platform.items(), key=lambda x: x[1], reverse=True)

answer1 = countPlatform(data)
numOfPlatform = len(answer1)
firstFav = answer1[0][0]
secondFav = answer1[1][0]

print(f'Question1: \n Number of platform: {numOfPlatform}\n Top 2: {firstFav}, {secondFav}')

print("=====================================================")

# 2.
def countLicense(data) :
  license_dic = {}
  for i in data:
    if i['License'] in license_dic.keys(): 
      license_dic[i['License']] += 1
    else :
      license_dic[i['License']] = 1
    # print(i['License'])
  return sorted(license_dic.items(), key=lambda x: x[1], reverse=True)

answer2 = countLicense(data)
numOfLicense = len(answer2)
firstFav = answer2[0][0]
secondFav = answer2[1][0]

print(f'Question2: \n Number of lisence: {numOfLicense}\n Top 2: {firstFav}, {secondFav}')

print("=====================================================")

# 3.
def findMostVersion(data): 
  most = data[0]
  for i in data: 
    if(most['NbOfVersions'] < i['NbOfVersions']): 
      most = i
  return most
answer3 = findMostVersion(data)
print(f'Question3: \n Project: {answer3["Name"]} \n Lastest version: {answer3["NbOfVersions"]}')

print("=====================================================")

# 4.
def findPythonAverage(data):
  result = 0
  num = 0
  for i in data:
    if i['Language'] == 'Python' :
      result += float(i['Size'])
      num += 1
  return result/num
result = findPythonAverage(data)
print(f'Question4: \n Average size of project that use Python: {result:.3f} MB')

print("=====================================================")

# 5.
def countLanguageByHost(data): 
  language = {}
  for i in data: 
    if i['Host'] == 'GitHub':
      if i['Language'] in language.keys(): 
        language[i['Language']] += 1
      else :
        language[i['Language']] = 1
  return sorted(language.items(), key=lambda x: x[1])

answer5 = countLanguageByHost(data)
lessNumber = answer5[0][1]
listOfProject = [i for i in answer5 if i[1] == lessNumber]
print(f'Question5: \n There are {len(listOfProject)} languages({[i[0] for i in listOfProject]}) \n In each language use {lessNumber} projects')

print("=====================================================")

# 6.
def countReadme(data): 
  readme = []
  without = ['.md', '.markdown', '.MD']
  for i in data:
    if i['ReadmeFilename'] != '-' and i['ReadmeFilename'].__contains__('.') and not any([x in i['ReadmeFilename'] for x in without]):
      fileType = i['ReadmeFilename'].split(".")[1]
      if fileType not in readme:
        readme.append(fileType)
  return readme
answer6 = countReadme(data)
print(f'Question6:\n There are {len(answer6)} types -> {answer6}')

print("=====================================================")

# 7. 
def findMostStar(data): 
  most = data[0]
  for i in data: 
    if(float(most['Stars']) < float(i['Stars'])): 
      most = i
  return most
answer7 = findMostStar(data)
print(f'Question7: \n Most stars project use {answer7["Language"]} \n License: {answer7["License"]}')

print("=====================================================")

# 8.
def countJavascript(data):
  project = []
  for i in data: 
    if i['Name'].__contains__('js') and not i['Name'].__contains__('json'):
      project.append(i['Name'])
  return project
answer8 = countJavascript(data)
print(f'Question8:\n There are {len(answer8)} projects that concerned with javascript')

print("=====================================================")
