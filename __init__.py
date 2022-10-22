from mycroft import MycroftSkill, intent_handler


class Audacious(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('audacious.intent')
    def handle_audacious(self, message):
        self.speak_dialog('audacious')


def create_skill():
    return Audacious()

