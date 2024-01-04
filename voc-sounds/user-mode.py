import speech_recognition as sr
import speak
import subprocess
import requests
import time

# URL d'un site Web pour la vérification de la connexion Internet
internet_check_url = "https://www.google.com"

def is_internet_available():
    try:
        response = requests.get(internet_check_url, timeout=3)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def main():
    # Présentation de l'assistant
    speak.presentation()
    recognizer = sr.Recognizer()
    audio = None  # Définissez audio en dehors du bloc with

    while True:
        try:
            # Vérifiez la disponibilité de la connexion Internet
            internet_connected = is_internet_available()
        except Exception as e:
            print(f"Erreur lors de la vérification de la connexion Internet : {e}")
            internet_connected = False

        if internet_connected:
            try:
                with sr.Microphone(sample_rate=16000) as source:  # Augmentez la fréquence d'échantillonnage
                    print("En attente d'une nouvelle commande...")
                    recognizer.adjust_for_ambient_noise(source)
                    try:
                        audio = recognizer.listen(source, timeout=3)  # Réduisez la durée d'enregistrement
                    except sr.WaitTimeoutError:
                        print("Aucune commande vocale détectée. Réessayez.")
                        continue  # Revenir au début de la boucle pour écouter à nouveau
            except Exception as e:
                print(f"Erreur lors de l'écoute audio : {e}")
                continue

            try:
                text = recognizer.recognize_google(audio, language="fr-FR")
                print("Vous avez dit : " + text)

                # Exemple : Répondre à une commande de l'utilisateur
                if "au revoir" in text or "quitter" in text or "fin" in text:
                    speak.au_revoir()
                    return  # Sortir du programme si l'utilisateur dit "au revoir"
                elif "fonction avancée" in text or "avancer" in text or "commande avancée" in text or "plus" in text or "Maya" in text or "aya" in text:
                    # Lancer le programme recognize.py
                    subprocess.run(["python", "voc-sounds/advanced-mode-recognize.py"])
                    speak.user_mode()
                else:
                    speak.incomprehension()

            except sr.UnknownValueError:
                print("Désolé, je n'ai pas pu comprendre ce que vous avez dit.")
            except sr.RequestError as e:
                print("Erreur lors de la demande à l'API Google : {0}".format(e))
        else:
            print("Pas de connexion Internet. Basculement sur no-connexion-recognition.py.")
            subprocess.run(["python", "voc-sounds/no-connection-recognition.py"])
            time.sleep(5)  # Attendez avant de réessayer la vérification de la connexion

if __name__ == "__main__":
    main()

