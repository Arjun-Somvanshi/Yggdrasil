from kivy.app import App
from kivy.lang import Builder
from Yggdrasil import Yggdrasil
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
kv = '''
BoxLayout:
    File:
'''
class File(Yggdrasil):
    pass
class MyApp(App):
    def build(self):
        return Builder.load_string(kv)
 
if __name__  == '__main__':
    MyApp().run()