import cohere
from cohere.classify import Example
import csv

data = []
with open('names_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append((row[0], int(row[1])))
co = cohere.Client('lDQByuzzarqhHQ4Xu0fhaE887a6XZULYlryvbcmb')

exampl = [Example(i[0], f'{i[1]}') for i in data]
response = co.classify(
  model='large',
  inputs=["Mia"],

  examples=exampl[4000:6500])
print('The confidence levels of the labels are: {}'.format(response.classifications))