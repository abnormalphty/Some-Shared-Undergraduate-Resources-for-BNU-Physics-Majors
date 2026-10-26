from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from jnius import autoclass
import requests

# 使用 Java 调用安卓 WebView
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

class MapApp(App):
    def build(self):
        # 创建布局
        layout = BoxLayout(orientation='vertical')

        # 添加输入框用于输入地址
        self.address_input = TextInput(hint_text='输入地址', size_hint=(1, 0.1))
        layout.add_widget(self.address_input)

        # 添加按钮用于显示地图
        show_map_button = Button(text='显示地图', size_hint=(1, 0.1))
        show_map_button.bind(on_press=self.show_map)
        layout.add_widget(show_map_button)

        # 返回布局
        return layout

    def show_map(self, instance):
        # 获取用户输入的地址
        address = self.address_input.text

        # 调用高德地图 API 获取经纬度
        api_key = "YOUR_AMAP_KEY"
        url = f"https://restapi.amap.com/v3/geocode/geo?address={address}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        if data['geocodes']:
            location = data['geocodes'][0]['location']
            lat, lon = map(float, location.split(','))

            # 创建地图 URL
            map_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=12/{lat}/{lon}"

            # 显示 WebView 并加载地图
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.setWebViewClient(WebViewClient())
            activity.setContentView(webview)
            webview.loadUrl(map_url)

        else:
            print("未找到该地址")

if __name__ == '__main__':
    MapApp().run()
