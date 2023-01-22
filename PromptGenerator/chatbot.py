import cohere
co = cohere.Client("key")


def generate_response(input: str) -> str:
    response = "Do you like to"
    while response[-1] != "?" or response.startswith('Do you like to'):
        response = co.generate(
            model='cba13dfa-279e-430a-9763-35bddf188434-ft',
            prompt='Ask a follow up question about this users interest. User: ' + input + ' \n',
            max_tokens=50,
            temperature=0.9,
            k=0,
            p=0.75,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["User"],
            return_likelihoods='NONE')
        response = response.generations[0].splitlines()[1][10:]
    return response
