#!/usr/bin/python
# -*- coding: utf8 -*-

import sys 
try:
    reload         # Python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:  # Python 3
    from importlib import reload

import speech_recognition as sr

r = sr.Recognizer() 
r.pause_threshold = 0.8
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.5

with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...") 
    r.adjust_for_ambient_noise(source, duration=1) 
    print('Say something>>> ')
    audio=r.listen(source)

try:
    print('Google Speech Recognition thinks you said:')
    sent = r.recognize_google(audio, language="zh-TW")
    print("{}".format(sent))
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print('No response from Google Speech Recognition service: {0}'.format(e))

