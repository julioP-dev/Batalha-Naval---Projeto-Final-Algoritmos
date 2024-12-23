import speech_recognition as sr

recognizer = sr.Recognizer()
def record_audio():
            with sr.Microphone() as source:
                print("escutando...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            return audio
        
def recognize_speech(record_audio):
            audio = record_audio()
            xy = ""
            try:
                text = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {text}")
                for caractere in text:
                    if caractere.isdigit():
                        xy += caractere

            except sr.UnknownValueError:
                print("Não entendido")
            except sr.RequestError:
                print("Sorry, there was an error processing your request.")
            return xy