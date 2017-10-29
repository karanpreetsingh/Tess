
def start_keyphrase_recognition(keyphrase_function, key_phrase):    
    modeldir = "files/sphinx/models"
    config = pocketsphinx.Decoder.default_config()    
    config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us-ptm'))    
    config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
    config.set_string('-keyphrase', key_phrase)
    config.set_string('-logfn', 'files/sphinx.log')
    config.set_float('-kws_threshold', 1)    
    p = pyaudio.PyAudio()    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)    
    stream.start_stream()    
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()    
    while True:
        buf = stream.read(1024)        
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break        
        if decoder.hyp() is not None:
            keyphrase_function()            
            decoder.end_utt()
            decoder.start_utt()

def parse(tokens):
    print tokens 
    
def tokenize():    
    print(globalName + " is listening..")
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        audio = r.listen(source)
    
    try:
        sentence =  r.recognize_google(audio)
        tokens = nltk.word_tokenize(sentence)
        parse(tokens)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    
