from youtube_transcript_api import YouTubeTranscriptApi
def checkLike(videoId: str):

    return True

def getTranscript(videoId):
    text = []

    for segment in YouTubeTranscriptApi.get_transcript(videoId):
        text.append(segment['text'])
    print(text)
    return

checkLike("uU8L1TI5J6g")
