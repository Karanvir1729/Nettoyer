import cohere
import tempfile
import shutil
import Automation
co = cohere.Client('key')
mode = 'command-xlarge-20221108'

#examples = open("Examples.txt", "r")

prompt = 'Given a conversation, please return the major themes. \n\nConversation: \nPerson 1: I like to read. What about you?\n\nPerson 2: I like to run.\n\nPerson 1: I used to run too, but I hurt my knee.\n\nPerson 2: I\'ve never had a problem with my knees.\n\nPerson 1: I\'m glad I don\'t have your problem.\n\nThemes:\nRunning, reading \n--\nConversation:\nPerson 1: I love movies. What kind of movies do you like?\n\nPerson 2: I like action movies.\n\nPerson 1: Do you like horror movies?\n\nPerson 2: No, I don\'t like horror movies.\n\nPerson 1: What\'s your favorite action movie?\n\nPerson 2: My favorite action movie is The Matrix.\n\nPerson 1: The Matrix is a great movie because of the action.\n\nPerson 2: Yeah, it is a great movie because of the action.\n\nThemes:\nmovies, action, The Matrix \n--\nConversation:\nPerson 1: I like to read books.\n\nPerson 2: I like to watch movies.\n\nPerson 1: What kind of books do you like to read?\n\nPerson 2: I like to read horror books.\n\nPerson 1: Oh, I don\'t like horror books.\n\nPerson 2: Why not?\n\nPerson 1: They are too scary.\n\nPerson 2: Yeah, I know. I don\'t like them either.\n\nPerson 1: Well, what kind of movies do you like to watch?\n\nPerson 2: I like to watch comedy movies.\n\nPerson 1: Oh, I don\'t like comedy movies.\n\nPerson 2: Why not?\n\nPerson 1: They are too cheesy.\n﻿\nPerson 2: Yeah, I know. I don\'t like them either.\n\nThemes:\nHorror, comedy \n--\nConversation:\nPerson 1: I like to play tennis.\n\nPerson 2: I like to play golf.\n\nPerson 1: How long have you played golf?\n\nThemes: Tennis, Golf\n'
userinput = ["Space exploration is a fascinating and ever-evolving field that has captivated humanity for decades. From the first manned spaceflight in 1961 to the current missions to Mars and beyond, the quest to discover and understand the universe has led to many breakthroughs in science and technology. The study of other planets and celestial bodies has provided valuable insights into the origins of our own planet and the possibility of life elsewhere in the cosmos. Advances in space exploration have also led to practical benefits for humanity such as satellite-based communications and weather forecasting. However, space exploration is also a challenging and costly endeavor, requiring international cooperation and long-term investment. As we continue to push the boundaries of what is possible, the future of space exploration promises to be even more exciting and full of discovery."]

themes = ",".join(userinput)
print(themes)


response = co.generate(
  model=mode,
  prompt= prompt + "\n--\n" + themes + "\n\nThemes:",
  max_tokens=50,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
feedChanger = Automation.FeedChanger()
print('Prediction: {}'.format(response.generations[0].text))
feedChanger.changeFeed(response.generations[0].text, 0)
