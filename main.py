from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import subprocess
import time
import threading
import requests
import json

class ControlPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # Title
        self.add_widget(Label(text="[b]🔒 Remote Control[/b]", markup=True, font_size=28))
        
        # Status
        self.status = Label(text="Status: Siap", color=(0.8, 0.8, 0.8, 1))
        self.add_widget(self.status)
        
        # Tombol Lock
        btn_lock = Button(text="🔒 Lock Device", size_hint=(1, 0.2), background_color=(0.8, 0.2, 0.2, 1))
        btn_lock.bind(on_press=self.lock_device)
        self.add_widget(btn_lock)
        
        # Tombol Unlock
        btn_unlock = Button(text="🔓 Unlock Device", size_hint=(1, 0.2), background_color=(0.2, 0.7, 0.2, 1))
        btn_unlock.bind(on_press=self.unlock_device)
        self.add_widget(btn_unlock)
        
        # Tombol Flash
        btn_flash = Button(text="💡 Flash Blink", size_hint=(1, 0.2), background_color=(0.8, 0.6, 0, 1))
        btn_flash.bind(on_press=self.flash_blink)
        self.add_widget(btn_flash)
        
        # Tombol Screenshot
        btn_screenshot = Button(text="🖼️ Screenshot", size_hint=(1, 0.2), background_color=(0.2, 0.4, 0.8, 1))
        btn_screenshot.bind(on_press=self.take_screenshot)
        self.add_widget(btn_screenshot)
        
        # Input IP Server
        self.ip_input = TextInput(hint_text="IP Server (opsional)", multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.ip_input)
    
    def lock_device(self, instance):
        self.status.text = "🔒 Mengunci..."
        try:
            subprocess.Popen(["input", "keyevent", "26"], shell=True)
            self.status.text = "✅ Perangkat Terkunci"
        except:
            self.status.text = "❌ Gagal Mengunci"
    
    def unlock_device(self, instance):
        self.status.text = "🔓 Membuka..."
        try:
            subprocess.Popen(["input", "keyevent", "82"], shell=True)
            self.status.text = "✅ Perangkat Terbuka"
        except:
            self.status.text = "❌ Gagal Membuka"
    
    def flash_blink(self, instance):
        self.status.text = "💡 Senter Berkedip..."
        def _flash():
            try:
                for i in range(6):
                    subprocess.Popen(["termux-torch", "on"], shell=True)
                    time.sleep(0.3)
                    subprocess.Popen(["termux-torch", "off"], shell=True)
                    time.sleep(0.3)
                self.status.text = "✅ Senter Selesai"
            except:
                self.status.text = "❌ Gagal Senter"
        threading.Thread(target=_flash).start()
    
    def take_screenshot(self, instance):
        self.status.text = "📸 Screenshot..."
        try:
            subprocess.Popen(["termux-screenshot", "/sdcard/screenshot.png"], shell=True)
            self.status.text = "✅ Screenshot Tersimpan"
        except:
            self.status.text = "❌ Gagal Screenshot"

class RemoteApp(App):
    def build(self):
        return ControlPanel()

if __name__ == '__main__':
    RemoteApp().run()
