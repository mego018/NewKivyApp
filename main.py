from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

# For WebView on Android
from kivy.utils import platform
if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

class MagmaApp(App):
    def build(self):
        root = FloatLayout()

        # === Scatter for the floating image ===
        self.scatter = Scatter(size_hint=(None, None), size=(300, 300))
        self.img = Image(size=self.scatter.size, allow_stretch=True)
        self.scatter.add_widget(self.img)
        root.add_widget(self.scatter)

        # === Transparency slider ===
        self.opacity_slider = Slider(min=0.1, max=1, value=1, size_hint=(0.3, None), height=50, pos=(50, 10))
        self.opacity_slider.bind(value=self.change_opacity)
        root.add_widget(self.opacity_slider)

        # === Lock button ===
        self.locked = False
        lock_btn = Button(text="Lock", size_hint=(0.2, None), height=50, pos=(400, 10))
        lock_btn.bind(on_press=self.toggle_lock)
        root.add_widget(lock_btn)

        # === Add image button ===
        add_img_btn = Button(text="Add Image", size_hint=(0.2, None), height=50, pos=(50, 70))
        add_img_btn.bind(on_press=self.open_filechooser)
        root.add_widget(add_img_btn)

        # === Zoom in button ===
        zoom_in_btn = Button(text="Zoom In", size_hint=(0.2, None), height=50, pos=(400, 70))
        zoom_in_btn.bind(on_press=lambda x: self.zoom_image(1.2))
        root.add_widget(zoom_in_btn)

        # === Zoom out button ===
        zoom_out_btn = Button(text="Zoom Out", size_hint=(0.2, None), height=50, pos=(400, 130))
        zoom_out_btn.bind(on_press=lambda x: self.zoom_image(0.8))
        root.add_widget(zoom_out_btn)

        # === WebView for Android ===
        if platform == 'android':
            self.add_webview(root)

        return root

    # === Image functions ===
    def change_opacity(self, instance, value):
        self.img.opacity = value

    def toggle_lock(self, instance):
        self.locked = not self.locked
        self.scatter.do_translation = not self.locked
        self.scatter.do_scale = not self.locked
        self.scatter.do_rotation = not self.locked
        instance.text = "Lock" if not self.locked else "Unlock"

    def open_filechooser(self, instance):
        content = FileChooserIconView()
        popup = Popup(title="Choose an image", content=content, size_hint=(0.9, 0.9))
        
        def load_selection(*args):
            if content.selection:
                self.img.source = content.selection[0]
                self.img.reload()
                popup.dismiss()
        
        content.bind(on_submit=lambda *a: load_selection())
        popup.open()

    def zoom_image(self, factor):
        # Zoom in or out depending on factor
        new_width = self.scatter.width * factor
        new_height = self.scatter.height * factor
        self.scatter.size = (new_width, new_height)
        self.img.size = self.scatter.size

    # === WebView on Android ===
    if platform == 'android':
        @run_on_ui_thread
        def add_webview(self, root):
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            
            activity = PythonActivity.mActivity
            self.webview = WebView(activity)
            self.webview.getSettings().setJavaScriptEnabled(True)
            self.webview.setWebViewClient(WebViewClient())
            self.webview.loadUrl("https://magma.com/home")
            
            layout = activity.findViewById(0x01020002)  # android.R.id.content
            layout.addView(self.webview)

if __name__ == "__main__":
    MagmaApp().run()