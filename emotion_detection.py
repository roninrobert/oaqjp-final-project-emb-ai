import json
import requests

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = headers)

    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    dominant_emotion_score=anger_score
    dominant_emotion_name = 'anger'
    if disgust_score > dominant_emotion_score:
        dominant_emotion_score = disgust_score
        dominant_emotion_name = 'disgust'
    if fear_score > dominant_emotion_score:
        dominant_emotion_score = fear_score
        dominant_emotion_name = 'fear'
    if joy_score > dominant_emotion_score:
        dominant_emotion_score = joy_score
        dominant_emotion_name = 'joy'
    if sadness_score > dominant_emotion_score:
        dominant_emotion_score = sadness_score
        dominant_emotion_name = 'sadness'

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_name
        }

    return result