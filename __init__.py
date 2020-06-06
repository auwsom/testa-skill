from mycroft import MycroftSkill, intent_file_handler


class Testa(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testa.intent')
    def handle_testa(self, message):
        self.speak_dialog('testa')


def create_skill():
    return Testa()

