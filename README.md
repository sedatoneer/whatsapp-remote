# WhatsApp Kontrollü Mi Box Kumanda
## Proje Hakkında
Bu proje, WhatsApp üzerinden gönderilen mesajlarla Mi Box cihazınızı uzaktan kontrol etmenizi sağlayan eğlenceli, pratik ve yenilikçi bir çözümdür. 
Daha önce Python ve Tkinter ile geliştirdiğim arayüzü kumandaya benzeyen bir proje, başlangıçta ilgi çekici olsa da zamanla görsel ve işlevsel olarak tatmin edici olmaktan çıktı ve yeterince eğlenceli gelmedi. 
Bu nedenle, herkesin günlük hayatta kullandığı WhatsApp platformunu temel alan, daha kullanıcı dostu ve hızlı tepki veren bir uzaktan kumanda sistemi tasarladım. 
Proje, WhatsApp Web üzerinden gelen mesajları okuyarak Mi Box’a ADB komutları gönderir ve cihazı kolayca kontrol eder.

## Özellikler
- WhatsApp Tabanlı Kontrol: Mesajlarla Mi Box’a ADB komutları gönderir (örn. "youtube aç", "netflix aç", "tv kapat").
- Hafif ve Hızlı: Düşük kaynak tüketimiyle çalışır, karmaşık arayüzlere ihtiyaç duymaz.
- Evrensel Erişim: Telegram veya özel uygulamalar yerine WhatsApp Web ile çalışır, herkesin erişimine açıktır.
- Özelleştirilebilir Komutlar: bot.py dosyasındaki komutları kolayca düzenleyebilir veya yenilerini ekleyebilirsiniz.
- Platform Bağımsız: PC veya WhatsApp Web destekli herhangi bir cihazda sorunsuz çalışır.
- Eğlenceli ve Pratik: Tkinter tabanlı eski arayüzden çok daha keyifli ve kullanıcı dostu bir deneyim sunar.


## Gereksinimler
- Python: 3.8 veya üzeri
- Kütüphaneler:
    selenium (WhatsApp Web otomasyonu için)
    webdriver_manager (ChromeDriver yönetimi için)
- ADB: Android Debug Bridge kurulu ve sistem PATH’ine eklenmiş olmalı
- Tarayıcı: Google Chrome veya Chromium
- ChromeDriver: Chrome sürümüne uyumlu (otomatik olarak webdriver_manager ile yüklenir)

## Demo Videosu:
    https://drive.google.com/file/d/1xTIwAKVa6_yCdDBL-jfG8JQPsYypZuSN/view?usp=sharing

## Kurulum Adımları
- Python Kurulumu: Python yüklü değilse, [Python resmi sitesinden](https://www.python.org/downloads/) indirip kurun.

- ADB Kurulumu:
[Android SDK Platform Tools sayfasından](https://developer.android.com/tools/releases/platform-tools?hl=tr) ADB’yi indirin.
İndirilen klasörü sistem PATH’ine ekleyin.


- Python Kütüphanelerini Yükleme: Proje dizininde terminali açın ve şu komutu çalıştırın:

  ```pip install -r requirements.txt ```


## Proje Dosyalarını Hazırlama

Proje, wp klasöründe bulunur ve şu yapıyı içerir:

wp/ (Ana Klasör)

├── whatsapp_profile/  
├── bot.py


## Çalıştırma

- Projeyi GitHub’dan klonlayın: 

  ```git clone https://github.com/sedatoneer/whatsapp-remote.git ```

- Mi Box cihazınızda USB Hata Ayıklama modunun açık olduğundan ve cihazın ADB ile bağlı olduğundan emin olun (adb devices ile kontrol edin).

- Proje dizinine gidin: cd wp

- Botu başlatın: python bot.py


- İlk çalıştırmada WhatsApp Web için bir QR kodu görünecek. Telefonunuzla QR kodunu taratarak WhatsApp’a giriş yapın.
- WhatsApp üzerinden tanımlı komutları (örn. "youtube aç", "netflix aç", "tv kapat") göndererek Mi Box cihazınızı kontrol edin.

## Komutlar ve Özelleştirme

#### Varsayılan komutlar bot.py içinde tanımlıdır:
- youtube aç: YouTube uygulamasını başlatır.
- netflix aç: Netflix uygulamasını başlatır.
- tv kapat: Cihazı uyku moduna alır.


Yeni komutlar eklemek veya mevcut komutları değiştirmek için bot.py dosyasındaki commands sözlüğünü düzenleyin. 

Örnek: 

commands = {

    "youtube aç": "adb shell monkey -p com.google.android.youtube.tv 1",
    "netflix aç": "adb shell monkey -p com.netflix.ninja 1",
    "tv kapat": "adb shell input keyevent 26",
    "ses aç": "adb shell input keyevent 24"  # Yeni komut örneği
}


Komutlar, WhatsApp mesajlarında küçük harfle yazıldığında da tanınır.



# Katkı Sağlama
Bu projeye katkıda bulunmak isterseniz:

- Depoyu forklayın.
- Yeni özellikler veya hata düzeltmeleri için bir dal oluşturun 
 
  ```(git checkout -b yeni-ozellik).```
- Değişikliklerinizi commit edin 

  ```(git commit -m "Yeni özellik eklendi"). ```
- Dalınızı ana depoya push edin 
  
  ```(git push origin yeni-ozellik). ```
- Bir Pull Request oluşturun.

İletişim
Sorularınız, önerileriniz veya katkılarınız için bana ulaşabilirsiniz:  

E-posta: sedatoneer@gmail.com  
LinkedIn: [Sedat Öner](https://www.linkedin.com/in/sedat-öner-672500243/)


## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.
