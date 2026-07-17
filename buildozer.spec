[app]
title = RemoteControl
package.name = remotecontrol
package.domain = org.myapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WAKE_LOCK,DEVICE_POWER,CAMERA,FLASHLIGHT,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

android.allow_backup = True
android.manifest_application = <application android:usesCleartextTraffic="true" />
