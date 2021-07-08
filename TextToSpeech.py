from ibm_cloud_sdk_core import authenticators
from ibm_watson import TextToSpeechV1, text_to_speech_v1

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import ibm_watson

api=IAMAuthenticator("S-QT1wZ2yHpur288hbSiw5KwEhUA5jUzG_1xi_-tRpXO")
mytext=TextToSpeechV1(authenticator=api)

mytext.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/c436e08e-f6cb-45c7-b6bb-d2bdd7467ec7")
with open("output1.mp3","wb") as audiofile:

    audiofile.write(mytext.synthesize(" Rate this place out of five", accept="audio/mp3").get_result().content)
