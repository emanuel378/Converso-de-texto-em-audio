from gtts import gTTS 
import os
#Aqui, vamos usar o os para tocar o arquivo de áudio depois que ele for gerado.

#Primeiro o texto, o que robo vai falar
texto = "O rato roeu a ropa do rei de Roma O sapo saltou do saco Se sacudiu e sumiu da soma"

#Em qual lingua o audio vai ser
audio = "pt"

#Aqui a gente colocar o texto,audio e o slow a velocidade do audio
tts = gTTS(text=texto,lang=audio,slow=False)

#Vamos salva o audio
tts.save("audio.mp3")

#Tocar o audio automaticamente
os.system("start audio.mp3")