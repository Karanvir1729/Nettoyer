import cohere
co = cohere.Client("ZEcUXrPLLKZHyHRoJTfF8Jq0ftCuNn51Zh5vhj9t")


def generate_response(input: str) -> str:
    returnvalue = "Do you like to"
    while not returnvalue or returnvalue[-1] != "?" or returnvalue.startswith('Do you like to'):
        response = co.generate(
            model='cba13dfa-279e-430a-9763-35bddf188434-ft',
            prompt='Ask a follow up question about this users interest. User: ' + input + ' \n ',
            max_tokens=20,
            temperature=0.9,
            k=0,
            p=0.75,
            frequency_penalty=.8,
            presence_penalty=0,
            stop_sequences=["User"],
            return_likelihoods='NONE')
        if response.generations[0].splitlines()[1].startswith("Response: "):
            returnvalue = response.generations[0].splitlines()[1][10:].strip()
        print(returnvalue)
    return returnvalue
