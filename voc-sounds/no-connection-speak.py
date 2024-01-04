import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Réglez la vitesse de la synthèse vocale

def parler(text, voice="french"):
    engine.setProperty('voice', voice)
    engine.say(text)
    engine.runAndWait()

def erreur():
    parler("Une erreur s'est produite.")

def incomprehension():
    parler("Désolé, je n'ai pas pu comprendre ce que vous avez dit. Réessayez.")

def presentation():
    parler("Bienvenue dans l'assistant vocal.")

# Vous pouvez ajouter d'autres fonctions pour gérer différents types de messages

if __name__ == "__main__":
    presentation()  # Présentation au démarrage
    text = "Bonjour, ceci est un exemple de synthèse vocale en français."
    parler(text)

