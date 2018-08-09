# One Days Workshop for Voice Control on Raspberry Pi 

## Intro
In this workshop, we will introudce how to hack [SeeedStudio ReSpeaker 2-Mics HAT](https://www.raspberrypi.com.tw/17528/71001/)
1. Introduction to ReSpeaker 2-Mic HAT
2. What is Linux ALSA
3. Embedded Google Assistant to Pi
4. Hack ReSpeaker 2-Mic HAT

The slide is available on [[slideshare] 改造 ReSpeaker 2-MIC HAT](https://www.slideshare.net/raspberrypi-tw/respeaker-2mic-hat)


## Environment
[Raspberry Pi 3 Model B+ 入門組](https://www.raspberrypi.com.tw/21212/pi-3-b-plus-microsd-power-supply/) + 2018-06-27-raspbian-stretch.img

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get -y install python-pip python-dev python3-dev python3-venv flac python-pyaudio python-numpy python3-gi-cairo swig3.0 portaudio19-dev python3-pyaudio sox libatlas-base-dev libffi-dev libssl-dev vim mpg123 git espeak x11vnc 
$ sudo apt-get -y install libpython3-all-dev libttspico-data libttspico-utils libttspico0 ntpdate python3-all python3-all-dev python3-pysocks python3-virtualenv virtualenv
$ sudo pip install -U SpeechRecognition request pyaudio setuptools wheel
$ sudo pip3 install -U request numpy cairocffi
```

## Buy Raspberry Pi and Smeart Speaker Learning Kit
* [[產品] Raspberry Pi 3 Model B+ 入門組](https://www.raspberrypi.com.tw/21212/pi-3-b-plus-microsd-power-supply/)
* [[產品] 智慧喇叭語音學習套件](https://www.raspberrypi.com.tw/19621/pi-smart-speaker-kit/)
