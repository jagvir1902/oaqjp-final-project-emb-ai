from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def  analyse_emotion():
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result=emotion_detector(text_to_analyse)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid input! Please try again'
    response_text = f"""For the given statement, the system response is 
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} 
    and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."""
    return response_text

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)