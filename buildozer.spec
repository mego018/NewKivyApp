[app]

# اسم التطبيق
title = MagmaApp

# اسم الباكيج (تقدر تغيره بس لازم يكون unique)
package.name = magmaapp
package.domain = org.magma

# ملف البداية
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

# اسم ملف main
main.py = main.py

# إصدار التطبيق
version = 0.1

# المتطلبات
requirements = python3,kivy,pyjnius,android

# أيقونة التطبيق (اختياري لو عندك)
# icon.filename = %(source.dir)s/data/icon.png

# لو بدك ملفات إضافية
# source.include_patterns = assets/*,images/*.png

# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE

# API
android.api = 33
android.minapi = 21

# target SDK
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21

# Orientation
orientation = portrait

# (bool) استخدم window الكامل
fullscreen = 0

# Package format
android.archs = armeabi-v7a,arm64-v8a

# (str) خروج apk النهائي
# buildozer سيضعه داخل bin/