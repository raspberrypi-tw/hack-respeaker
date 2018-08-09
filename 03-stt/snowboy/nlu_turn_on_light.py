# -*- coding: utf8 -*-

import snowboydecoder
import sys
import signal
import speech_recognition as sr
import os

import sys 
try:
    reload         # Python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:  # Python 3
    from importlib import reload

import urllib
import uuid
import json
import requests

import RPi.GPIO as GPIO
import time    

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

interrupted = False

def audioRecorderCallback(fname):
    snowboydecoder.play_audio_file()
    print "converting audio to text"
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.phrase_threshold = 0.3
    r.non_speaking_duration = 0.5
    with sr.AudioFile(fname) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        query = r.recognize_google(audio, language="zh-TW")
        #print(r.recognize_google(audio, language="zh-TW"))
        print(query)

        lang = 'zh-tw'
        session_id = str( uuid.uuid1() )
        timezone = 'Asia/Taipei'
        authorization = '<FIXME>'

        headers = {
            "accept": "application/json",
            "authorization": authorization
        }

        url = 'https://api.dialogflow.com/v1/query?v=20170712'
        params = {'query':str(query), 'lang':lang, 'sessionId': session_id, 'timezone': timezone}

        response = requests.request("GET", url, headers=headers, params=params)
        data = json.loads(response.text)

        #print(data)

        status = data['status']['code']
        print("Status: {}".format(status))

        if status == 200:
            resolveQuery = data['result']['resolvedQuery']
            fulfillment = data['result']['fulfillment']['speech']

            print("Query: {}".format(resolveQuery))
            print("Response: {}".format(fulfillment))


            if fulfillment == 'turn_on_light_ok':
                GPIO.output(32, GPIO.HIGH)
            # elif fulfillment == 'turn_off_light_ok':
            else:
                GPIO.output(32, GPIO.LOW)


    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)

    os.remove(fname)



def detectedCallback():
  sys.stdout.write("recording audio...")
  sys.stdout.flush()

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print "Error: need to specify model name"
    print "Usage: python demo.py your.model"
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print "Listening... Press Ctrl+C to exit"

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()
