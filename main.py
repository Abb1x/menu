import webview
import os

class Api:
    def __init__(self):
        self._window = None
    def set_window(self, window):
        self._window = window
    def execute(self, command):
        os.system(command)
    def destroy(self):
        self._window.destroy()
       

api = Api()
window = webview.create_window('Hello world', 'page/index.html', fullscreen=True, js_api=api)
api.set_window(window)
webview.start()
