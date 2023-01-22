from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from toxicity_classifier import video_filter


def check_like(video_id: str, threshold) -> bool:
    try:
        text = get_transcript(video_id)
    except TranscriptsDisabled:
        return False
    else:
        return video_filter(text, threshold)


def get_transcript(videoId: str) -> list:
    text = []
    for segment in YouTubeTranscriptApi.get_transcript(videoId):
        text.append(segment['text'])
    return text