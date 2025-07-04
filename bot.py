from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time
import tempfile

# Komutlar
commands = {""
    "youtube aç": "adb shell monkey -p com.google.android.youtube.tv 1",
    "netflix aç": "adb shell monkey -p com.netflix.ninja 1",
    "tv kapat": "adb shell input keyevent 26"
}

temp_dir = tempfile.mkdtemp()
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\sedat\wp\whatsapp_profile")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

input("📱WhatsApp QR kodunu telefonunla tara ve Enter'a bas...")

print("✅ Başladı la, mesajları dinliyoz...")

last_message = ""

while True:
    try:
        messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text.copyable-text")
        if messages:
            current_message = messages[-1].text.strip().lower()
            if current_message != last_message:
                print("🟡 Yeni mesaj:", current_message)
                for cmd in commands:
                    if cmd in current_message:
                        print(f"🎯 Komut bulundu: '{cmd}', komut gönderiliyo la...")
                        subprocess.run(commands[cmd].split())
                        break
                last_message = current_message
    except Exception as e:
        print("⚠️ Hata:", e)
    time.sleep(1.5)
