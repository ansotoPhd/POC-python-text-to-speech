import pyttsx3

# => Create engine
engine = pyttsx3.init()

# => First test
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


# => Listening for events

# def onStart(name):
#     print('starting', name)
#
# def onWord(name, location, length):
#     print('word', name, location, length)
#
# def onEnd(name, completed):
#     print('finishing', name, completed)
#
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', name="aa")
# engine.runAndWait()


# => driver event loop
# engine = pyttsx3.init()
# def onStart(name):
#     print('starting', name)
# def onWord(name, location, length):
#     print('word', name, location, length)
# def onEnd(name, completed):
#     print('finishing', name, completed)
#     if name == 'fox':
#         engine.say('What a lazy dog!', 'dog')
#     elif name == 'dog':
#         engine.endLoop()
#
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()

# => Properties

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    # engine.setProperty('voice', voice.id)
