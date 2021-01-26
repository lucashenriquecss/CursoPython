import speech_recognition
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("oii")
    audio = recognizer.listen(source)

print("google hehehe")
print(recognizer.recognize_google(audio))
s=input("oLA, COMO VOCE ESTA?\n").lower()

if "Estou bem" in s:
    print("Quebom, o dia hoje esta muito quente")
    if "sim, ate demais" in s:
        print("Preciso de agua")



