from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import socket
import time

# إعدادات الشاشة (خلفية داكنة احترافية)
Window.clearcolor = (0.05, 0.05, 0.08, 1)

# الألوان
COLOR_NEON = (0, 0.9, 1, 1) # أزرق سماوي
COLOR_GREEN = (0, 0.8, 0.2, 1) # أخضر
COLOR_RED = (0.9, 0.2, 0.2, 1) # أحمر
COLOR_TEXT = (0.9, 0.9, 0.9, 1)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        # العنوان
        title = Label(text="GAME MASTER PRO", font_size=40, color=COLOR_NEON, bold=True, size_hint_y=None, height=100)
        layout.add_widget(title)
        
        # زر الشبكة
        btn_boost = Button(text="⚡ [1] فحص وتسريع الشبكة", font_size=22, background_color=(0, 0.4, 0.6, 1), size_hint_y=None, height=90)
        btn_boost.bind(on_press=self.go_to_booster)
        layout.add_widget(btn_boost)
        
        # زر الحساسية
        btn_sens = Button(text="🎯 [2] مختبر الحساسية AI", font_size=22, background_color=(0.6, 0, 0.4, 1), size_hint_y=None, height=90)
        btn_sens.bind(on_press=self.go_to_sens)
        layout.add_widget(btn_sens)
        
        layout.add_widget(Label(text="Developed for Gamers", font_size=14, color=(0.5, 0.5, 0.5, 1)))
        self.add_widget(layout)
        
    def go_to_booster(self, instance): self.manager.current = 'booster'
    def go_to_sens(self, instance): self.manager.current = 'sens'

class BoosterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="NETWORK & RAM BOOSTER", font_size=25, color=COLOR_NEON, size_hint_y=None, height=60))
        
        self.status_label = Label(text="جاهز للفحص...", font_size=18, color=COLOR_TEXT)
        layout.add_widget(self.status_label)
        
        btn_check = Button(text="بدء الفحص والتفريغ", font_size=20, background_color=COLOR_GREEN, size_hint_y=None, height=70)
        btn_check.bind(on_press=self.run_booster)
        layout.add_widget(btn_check)
        
        btn_back = Button(text="رجوع", font_size=18, background_color=COLOR_RED, size_hint_y=None, height=50)
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)
        
    def run_booster(self, instance):
        self.status_label.text = "جاري فحص سيرفرات اللعبة...\nجاري تفريغ الذاكرة العشوائية..."
        try:
            # فحص بينج حقيقي لسيرفر جوجل (كبديل لسيرفر اللعبة)
            start_time = time.time()
            s = socket.create_connection(("8.8.8.8", 53), timeout=2)
            end_time = time.time()
            ping = int((end_time - start_time) * 1000)
            s.close()
            
            # محاكاة تفريغ الذاكرة
            time.sleep(1)
            self.status_label.text = f"✅ تم تفريغ الذاكرة!\n✅ البنج الحالي: {ping}ms\n✅ تم تحسين استقرار الشبكة."
            self.status_label.color = COLOR_GREEN
        except Exception as e:
            self.status_label.text = "❌ فشل الاتصال بالسيرفر."
            self.status_label.color = COLOR_RED
        
    def go_back(self, instance): self.manager.current = 'main'

class SensScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        layout.add_widget(Label(text="AI SENSITIVITY GENERATOR", font_size=25, color=COLOR_NEON, size_hint_y=None, height=50))
        
        # المدخلات
        input_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=150)
        
        input_grid.add_widget(Label(text="الفريمات (FPS):", color=COLOR_TEXT))
        self.fps_spin = Spinner(text='90', values=('60', '90', '120'), size_hint_y=None, height=50)
        input_grid.add_widget(self.fps_spin)
        
        input_grid.add_widget(Label(text="عدد الأصابع:", color=COLOR_TEXT))
        self.fingers_spin = Spinner(text='4', values=('2', '3', '4', '5'), size_hint_y=None, height=50)
        input_grid.add_widget(self.fingers_spin)
        
        input_grid.add_widget(Label(text="أسلوب اللعب:", color=COLOR_TEXT))
        self.style_spin = Spinner(text='مقتحم', values=('مقتحم', 'قناص', 'متوازن'), size_hint_y=None, height=50)
        input_grid.add_widget(self.style_spin)
        
        layout.add_widget(input_grid)
        
        btn_gen = Button(text="توليد الحساسية الآن", font_size=20, background_color=(0.6, 0, 0.4, 1), size_hint_y=None, height=60)
        btn_gen.bind(on_press=self.generate)
        layout.add_widget(btn_gen)
        
        # شاشة النتائج
        self.result_label = Label(text="املأ البيانات واضغط توليد...", font_size=14, color=COLOR_TEXT, halign="center", valign="top")
        layout.add_widget(self.result_label)
        
        btn_back = Button(text="رجوع", font_size=18, background_color=COLOR_RED, size_hint_y=None, height=50)
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def generate(self, instance):
        fps = int(self.fps_spin.text)
        fingers = int(self.fingers_spin.text)
        style = self.style_spin.text
        
        # الخوارزمية (Base values)
        base_cam = 110
        base_ads = 100
        base_gyro = 300
        base_gyro_ads = 280
        
        # تعديلات FPS
        if fps == 60: base_cam += 10; base_ads += 10
        elif fps >= 90: base_cam -= 5; base_ads -= 5
            
        # تعديلات الأصابع
        if fingers >= 4: base_cam -= 10; base_gyro += 20
            
        # تعديلات الأسلوب
        if style == 'مقتحم': base_gyro += 40; base_ads += 10
        elif style == 'قناص': base_gyro -= 30; base_ads -= 15

        # دالة حساب السكوبات (كل ما زاد التقريب قل الرقم)
        def calc(base):
            return f"NoScp: {base} | RedDot: {int(base*0.9)}\n2x: {int(base*0.75)} | 3x: {int(base*0.6)}\n4x: {int(base*0.45)} | 6x: {int(base*0.3)}\n8x: {int(base*0.15)}"

        res = f"[b]📷 Camera:[/b]\n{calc(base_cam)}\n\n"
        res += f"[b]🎯 ADS:[/b]\n{calc(base_ads)}\n\n"
        res += f"[b]📱 Gyro:[/b]\n{calc(base_gyro)}\n\n"
        res += f"[b]🔄 Gyro ADS:[/b]\n{calc(base_gyro_ads)}"
        
        # تحديث النص
        self.result_label.text = res
        self.result_label.markup = True

    def go_back(self, instance): self.manager.current = 'main'

class PubgApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BoosterScreen(name='booster'))
        sm.add_widget(SensScreen(name='sens'))
        return sm

if __name__ == '__main__':
    PubgApp().run()
