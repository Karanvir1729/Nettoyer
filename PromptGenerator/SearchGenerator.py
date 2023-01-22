import cohere



def process_tag(userinput: list) -> list:
    co = cohere.Client('lDQByuzzarqhHQ4Xu0fhaE887a6XZULYlryvbcmb')
    mode = 'command-xlarge-20221108'
    prompt = 'Generate five words related to the inputted topic. Avoid abstract nouns, be specific. \n\nInput: Chess\n\nWords: Grandmaster, Chess tournament, Checkmate, Board Games, Castle \n--\nInput: The Matrix\n\nWords: Keanu Reeves, Cyberpunk, Fight Choreography, Simulated Reality, Action Films\n--\nInput: Badminton\n--\nWords: Birdie, Shuttlecock, Racked up, Sports Day, Tally Ho\n--\nInput: Travel\n\nWords: Travel Guide, Passport Renewal, Visa Help, Airline Review, Cruise Line\n--\nInput: History\n\nWords: World War I, the Great Depression, Pearl Harbor, D-Day\n--\nInput: Yoga \n--\nWords: Asana, Downward Facing Dog, Plank, Chaturanga, Upward Facing Dog\n--\n'
    searches = []
    for tag in userinput:
        response = co.generate(
            model='command-xlarge-20221108',
            prompt= prompt + "Input: " + tag +  '\n\nWords:',
            max_tokens=50,
            temperature=0.9,
            k=0,
            p=0.75,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE')
        searches.append(response.generations[0].text.split("\n")[0])
    return searches


