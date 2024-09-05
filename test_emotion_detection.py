 if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion.items(), key=lambda x: x[1])
        return dominant_emotion[0]
else:
    return None
