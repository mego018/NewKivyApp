[app]

# (1) معلومات التطبيق
title = Magma App
package.name = com.yourcompany.magmaapp
package.domain = yourcompany.com
source.dir = .
source.exclude_dirs = bin, .buildozer
version = 0.1
requirements = python3, kivy, android, pil
orientation = portrait
fullscreen = 0

# (2) إعدادات الأندرويد
android.api = 33
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a
android.ndk = 25b
android.gradle_dependencies =
# هذا ضروري لوظيفة WebView على أندرويد
    'com.android.support:support-v4:27.1.1',
    'com.android.support:appcompat-v7:27.1.1',
    'com.google.android.gms:play-services-ads:21.3.0'

# (3) إعدادات عامة
icon.filename = %(source.dir)s/data/icon.png
app_entry = %(source.dir)s/main.py
p4a.branch = master
p4a.python = 3.9
