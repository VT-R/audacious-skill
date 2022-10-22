from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from os import system
import subprocess

subprocess.Popen(["audacious", "-H"]) 

class AudaciousControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('Play.intent')
    def handle_Play_intent(self, message):

        self.speak_dialog("Play")       
        system('audacious --play')

    @intent_handler('Pause.intent')
    def handle_Pause_intent(self, message):

        self.speak_dialog("Pause")
        system('audacious --pause')
        
    @intent_handler('Stop.intent')
    def handle_Stop_intent(self, message):

        self.speak_dialog("Stop")
        system('audacious --stop')

    @intent_handler('Next.intent')
    def handle_Next_intent(self, message):

        self.speak_dialog("Next")
        system('audacious --fwd')

    @intent_handler('Prev.intent')
    def handle_Prev_intent(self, message):

        self.speak_dialog("Prev")
        system('audacious --rew')

    def stop(self):
        pass

def create_skill():
    return AudaciousControl()

