# POC-python-text-to-speech

Testing some TTS Python packages 

## Pyttsx

- https://github.com/RapidWareTech/pyttsx
- https://pyttsx.readthedocs.io/en/latest/#

Python3:
- https://github.com/nateshmbhat/pyttsx3
- https://pyttsx3.readthedocs.io/en/latest/



Pytsx is a cross-platform tts wrapper. It uses different speech engines based on your so:
- nsss - NSSpeechSynthesizer on Mac OS X 10.5 and higher
- sapi5 - SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7
- espeak - eSpeak on any distro / platform that can host the shared library (e.g., Ubuntu / Fedora Linux)


    sudo pip install pyttsx


#### espeak (linux library)

http://espeak.sourceforge.net/
https://github.com/espeak-ng/espeak-ng

eSpeak is a compact open source software speech synthesizer for English and other languages, for Linux and Windows. 

    sudo apt-get install espeak
    
    /usr/lib/x86_64-linux-gnu/espeak-data/voices    

- Mbrola voices
http://www.tcts.fpms.ac.be/synthesis/mbrola/
https://askubuntu.com/questions/554747/how-to-install-more-voices-to-espeak
http://espeak.sourceforge.net/mbrola.html

    => Emotions: http://emofilt.syntheticspeech.de/


### Talkey
https://pypi.org/project/talkey/