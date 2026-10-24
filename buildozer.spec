[app]
title = GameMasterPro
package.name = gamemasterpro
package.domain = org.gmp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,cython==0.29.33
orientation = portrait
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
