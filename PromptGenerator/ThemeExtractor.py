import cohere

co = cohere.Client('2gxzxIx2lsMn4MGqiIwXWIUMoGC1egS7iNM9WtQn')
mode = 'command-xlarge-20221108'


def process_conversation(userinput: list) -> str:
    prompt = 'Given a conversation, please return the major themes. Seperate them with commas. \n\nConversation: \nPerson 1: I like to read. What about you?\n\nPerson 2: I like to run.\n\nPerson 1: I used to run too, but I hurt my knee.\n\nPerson 2: I\'ve never had a problem with my knees.\n\nPerson 1: I\'m glad I don\'t have your problem.\n\nThemes:\nRunning, reading \n--\nConversation:\nPerson 1: I love movies. What kind of movies do you like?\n\nPerson 2: I like action movies.\n\nPerson 1: Do you like horror movies?\n\nPerson 2: No, I don\'t like horror movies.\n\nPerson 1: What\'s your favorite action movie?\n\nPerson 2: My favorite action movie is The Matrix.\n\nPerson 1: The Matrix is a great movie because of the action.\n\nPerson 2: Yeah, it is a great movie because of the action.\n\nThemes:\nmovies, action, The Matrix \n--\nConversation:\nPerson 1: I like to read books.\n\nPerson 2: I like to watch movies.\n\nPerson 1: What kind of books do you like to read?\n\nPerson 2: I like to read horror books.\n\nPerson 1: Oh, I don\'t like horror books.\n\nPerson 2: Why not?\n\nPerson 1: They are too scary.\n\nPerson 2: Yeah, I know. I don\'t like them either.\n\nPerson 1: Well, what kind of movies do you like to watch?\n\nPerson 2: I like to watch comedy movies.\n\nPerson 1: Oh, I don\'t like comedy movies.\n\nPerson 2: Why not?\n\nPerson 1: They are too cheesy.\n﻿\nPerson 2: Yeah, I know. I don\'t like them either.\n\nThemes:\nHorror, comedy \n--\nConversation:\nPerson 1: I like to play tennis.\n\nPerson 2: I like to play golf.\n\nPerson 1: How long have you played golf?\n\nThemes:\n'
    input = " ".join(userinput)
    themes = "Person 1"
    while "Person 1" in themes or not "," in themes:
        response = co.generate(
            model=mode,
            prompt=prompt + "\n--\n" + input + "\n\nThemes:",
            max_tokens=50,
            temperature=0.9,
            k=0,
            p=0.75,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=[],
            return_likelihoods='NONE')
        themes = response.generations[0].text
        print(themes)
    print(themes)
    themes = themes.replace("tennis", "")
    themes = themes.replace("Running", "")
    themes = themes.replace("reading", "")
    themes = themes.replace("movie", "")
    themes = themes.replace("action", "")
    themes = themes.replace("The Matrix", "")
    themes = themes.replace("horror", "")
    themes = themes.replace("comedy", "")
    themes = themes.replace("golf", "")
    themes = themes.replace('interests', '')

    return themes


# feedChanger = Automation.FeedChanger()
# feedChanger.changeFeed(response.generations[0].text, 0)
