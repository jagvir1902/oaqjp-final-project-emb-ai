'''Test cases for emotion detector'''
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    '''Test class'''
    def test_emotion_detector(self):
        '''Test cases for all emotion types'''
        test_string = 'I am glad this happened'
        dominant_emotion = emotion_detector(test_string)['dominant_emotion']
        self.assertEqual(dominant_emotion, 'joy')
        test_string = 'I am really mad about this'
        dominant_emotion = emotion_detector(test_string)['dominant_emotion']
        self.assertEqual(dominant_emotion, 'anger')
        test_string = 'I feel disgusted just hearing about this'
        dominant_emotion = emotion_detector(test_string)['dominant_emotion']
        self.assertEqual(dominant_emotion, 'disgust')
        test_string = 'I am so sad about this'
        dominant_emotion = emotion_detector(test_string)['dominant_emotion']
        self.assertEqual(dominant_emotion, 'sadness')
        test_string = 'I am really afraid that this will happen'
        dominant_emotion = emotion_detector(test_string)['dominant_emotion']
        self.assertEqual(dominant_emotion, 'fear')


unittest.main()
