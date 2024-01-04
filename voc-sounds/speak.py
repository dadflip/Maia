from gtts import gTTS
import playsound

def parler(texte):
    # Convertir le texte en parole
    tts = gTTS(text=texte, lang='fr')

    # Sauvegarder la parole en tant que fichier audio
    tts.save("parole.mp3")

    # Jouer le son préenregistré
    playsound.playsound("parole.mp3")

def presentation():
    parler("Bonjour, je suis votre assistant MAIA. Comment puis-je vous aider ?")

def erreur():
    parler("Désolé, une erreur s'est produite. Veuillez réessayer plus tard.")

def incomprehension():
    parler("Je suis désolé, je n'ai pas compris votre demande. Pouvez-vous répéter ?")

def au_revoir():
    parler("Au revoir, à bientôt !")
    
def plus_options():
    parler("Commandes système !")

def user_mode():
    parler("Fin Commandes système ! Mode utilisateur")