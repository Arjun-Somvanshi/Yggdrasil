from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.properties import StringProperty, ListProperty, DictProperty
import os

Builder.load_file('yggdrasil.kv')

class Theme(Widget):
    background_color = StringProperty('#1e1e1e')
    task_bar_color = StringProperty('#252525')
    text_input_color = StringProperty('2D2D2D')
    title_font_color = StringProperty('00ABAE')
    description_font_color = StringProperty('00ABAE')
    ui_font_color = StringProperty('#797979')
    ButtonImages = DictProperty({}) # path to the button images
    
    def change_theme(self, bg_col, task_bar_col, ti_col, tf_col, d_font_col, ui_font_col, Button_Images):
        self.background_color = bg_col
        self.task_bar_color = task_bar_col
        self.text_input_color = ti_col
        self.title_font_color = d_font_col
        self.ui_font_color = ui_font_col
        self.ButtonImages = Button_Images

class Yggdrasil(BoxLayout):
    default_paths = ListProperty([])
    current_path = StringProperty('')
    path_history = ListProperty([])
    theme = Theme()
    text = StringProperty('')
    
    def __init__(self,**kwargs):
        super(Yggdrasil, self).__init__(**kwargs)
        self.set_default_path()
    
    def set_default_path(self):
        '''This functions sets the default available paths for each os'''
        if platform == 'win':
            #user directory and related folders
            user_path = os.path.expanduser('~')
            for folder in ["Desktop", "Documents", "Downloads", "Pictures", "Music", "Videos"]:
                self.default_paths.append((user_path+ os.path.sep +folder, folder))

            import win32api
            # getting the available drives 
            # or the available partitions in the file system
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]
            for drive in drives:    
                self.default_paths.append((drive, drive[0]))
            for path in self.default_paths:
                self.text += path[0] +'    '+ path[1] + '\n'
        
        elif platform == 'linux':
            self.default_paths.append((os.path.sep, os.path.sep))
            self.default_paths.append((os.path.expanduser(u'~') + os.path.sep, 'Home'))
            self.default_paths.append((os.path.sep + u'mnt' + os.path.sep, os.path.sep + u'media'))
            places = (os.path.sep + u'mnt' + os.path.sep, os.path.sep + u'media')
            for place in places:
                if os.path.isdir(place):
                    for directory in next(os.walk(place))[1]:
                        self.default_paths.append((place + os.path.sep + directory + os.path.sep, directory))
        
        elif platform == 'macosx' or platform == 'ios':
            self.default_paths.append((os.path.expanduser(u'~') + os.path.sep, 'Home'))
            vol = os.path.sep + u'Volume'
            if os.path.isdir(vol):
                for drive in next(os.walk(vol))[1]:
                    self.default_paths.append((vol + os.path.sep + drive + os.path.sep, drive))            
        
        elif platform == 'android':
            paths = []
            paths.append(('/', "Root")) #root
            paths.append(('/storage', "Mounted Storage")) #root
            from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
            app_path = app_storage_path()
            primary_external_path = primary_external_storage_path() 
            secondary_external_path = secondary_external_storage_path()
            if primary_external_path:
                paths.append((primary_external_path, "Internal Storage"))
            if secondary_external_path:
                paths.append((secondary_external_path, "External Storage"))
            for path in paths:
                realpath = os.path.realpath(path[0]) + os.path.sep
                if os.path.exists(realpath):
                    self.default_paths.append((realpath, path[1]))
            




            
            
                
