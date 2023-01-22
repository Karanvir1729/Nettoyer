import cohere
from cohere.classify import Example
import random

co = cohere.Client("key")

examples = [
  Example("You're an idiot.", "Toxic"),
  Example("They are stupid.", "Toxic"),
  Example("I can't stand you.", "Toxic"),
  Example("You're a failure.", "Toxic"),
  Example("I wish you were never born.", "Toxic"),
  Example("You're a waste of space.", "Toxic"),
  Example("I hope you die.", "Toxic"),
  Example("You're a disgrace.", "Toxic"),
  Example("I despise you.", "Toxic"),
  Example("You're a liar.", "Toxic"),
  Example("I'm going to hurt you.", "Toxic"),
  Example("You're a fraud.", "Toxic"),
  Example("I'm going to ruin your life.", "Toxic"),
  Example("You're a coward.", "Toxic"),
  Example("I'm going to make you pay.", "Toxic"),
  Example("drama", "Toxic"),
  Example("You're a worthless human being.", "Toxic"),
  Example("I'm going to ruin your reputation.", "Toxic"),
  Example("You're a piece of trash.", "Toxic"),
  Example("I'm going to hurt the ones you love.", "Toxic"),
  Example("You're a failure.", "Toxic"),
  Example("I'm going to make sure you regret ever crossing me.", "Toxic"),
  Example("you are hot trash", "Toxic"),
  Example("go to hell", "Toxic"),
  Example("get rekt moron", "Toxic"),
  Example("get a brain and use it", "Toxic"),
  Example("say what you mean, you jerk.", "Toxic"),
  Example("Are you really this stupid", "Toxic"),
  Example("I will honestly kill you", "Toxic"),
  Example("Have a great day!", "Benign"),
  Example("I'm glad we could help.", "Benign"),
  Example("Thank you for your patience.", "Benign"),
  Example("Everything will work out in the end.", "Benign"),
  Example("You're doing a great job.", "Benign"),
  Example("I appreciate your help.", "Benign"),
  Example("This is a wonderful opportunity.", "Benign"),
  Example("I'm happy to see you.", "Benign"),
  Example("You're such a kind person.", "Benign"),
  Example("I'm looking forward to it.", "Benign"),
  Example("You're a valuable member of the team.", "Benign"),
  Example("I'm proud of your accomplishments.", "Benign"),
  Example("You're a true friend.", "Benign"),
  Example("I'm grateful for your support.", "Benign"),
  Example("This is a beautiful place.", "Benign"),
  Example("I'm excited for what's to come.", "Benign"),
  Example("You're an inspiration.", "Benign"),
  Example("I'm lucky to have you in my life.", "Benign"),
  Example("You're a shining star.", "Benign"),
  Example("I'm so glad we met.", "Benign")
]


def video_filter(transcript: list, threshold: float) -> bool:
    if len(transcript) <= 50:
        sample_size = len(transcript)
    else:
        sample_size = 50

    samples = random.sample(range(len(transcript)), sample_size)
    sample = [transcript[i] for i in samples]

    response = co.classify(
    model='large',
    inputs=sample,
    examples=examples)

    toxic = 0
    for entry in list(response.classifications):
        entry = str(entry)
        if "Toxic" in (entry[:35]):
            toxic += 1

    print(toxic / len(transcript))
    return toxic / len(transcript) < threshold
