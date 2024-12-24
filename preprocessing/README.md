# NeuroVisionIST

Web application that detects Alzheimer's using artificial intelligence

(Aşağıdaki açıklamaları okumanız sağlıklı bir süreç açısından önem arz etmektedir!)

#### **1. Branch Yönetimi**

* **Branch Yapısı:**

  * [main(**default**](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/main)) : En genel bracnh'tir. Dosyaların son halleri veya kararlaştırılmış dosyalar yer alacak.
  * [Data_Processing_Management](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/Data_Processing_Management) : Veri işleme, veri temizleme ve veri hazırlığıyla ilgili kodlar burada bulunacak.
  * [Model_Dev](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/Model_Dev) : Modelin geliştirilmesi ve eğitilmesiyle ilgili çalışmalar burada yapılacak.
  * [Software_App_Dev](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/Software_App_Dev) : Web uygulamasının geliştirilmesi ve entegrasyon çalışmaları burada yapılacak (front/back-end server vb.)
  * [Testing_Sec_DevOps](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/Testing_Sec_DevOps) : Test senaryoları ve modelin doğrulanması için kullanılan kodlar bu branch'te yer alacak.
  * [UX_UI_Design_Dev](https://github.com/Ahmet-Onder-Onlu/NeuroVisionIST/tree/UX_UI_Design_Dev) : Kullanıcı arayüzü ve deneyimiyle ilgili çalışmalar bu branch'te gerçekleştirilecek (Sadece kod değil tasarımlarda paylaşılabilir)
* **Ana Branch (main) Kullanımı:**

  * main branch, yalnızca tüm ekip tarafından onaylanmış, nihai dosyaların yer aldığı branch’tir.
  * Herkes önce kendi branch’inde çalışmalı, daha sonra kod gözden geçirildikten sonra main branch’e merge yapılmalıdır.

#### **2. İsimlendirme Kuralları**

* **Dosya Adlandırma:**
  * Branch’lere dosya atarken, dosya adları açık ve anlaşılır olmalıdır. Örneğin:
  * alzheimer_model_v1.py
  * preprocessed_data_aug_2.csv

#### **3. Push lama Yapmadan Önce Dikkat Edilmesi Gerekenler**

* **Dosya Kontrolü:**
  * Push yapmadan önce dosyalarınızı gözden geçirin, gereksiz veya hatalı dosyaları commit etmeyin.
  * Herhangi bir veri seti veya büyük dosya paylaşılmamalıdır; çünkü server bu dosyaları kaldıramayabilir.
* **Kod İncelemesi:**
  * Kodlarınızı branch’te pushlamadan önce bir ekip arkadaşı tarafından gözden geçirilmesini sağlayın.
  * Kodunuzun açıklayıcı yorumlar içerdiğinden emin olun.
  * Daha önce yazılan kodlarla çakışmalara dikkat edin. Varsa eski kodun o kısmının silinebileceğini unutmayın.

#### **4. `.gitignore` Kullanımı**

.gitignore dosyası, repository'ye yüklenmesini istemediğimiz dosya ve klasörlerin uzantılarını içerir. Örnek olarak:

* *.pyc
* dataset/
* **Not:**

  * Veritabanı, model ağırlıkları, büyük veri setleri, ve özel bilgiler içeren dosyalar .gitignore dosyasına eklenmelidir.

----------------------------------------------------------------------------		Proje Hakkında Detay ve Toplantı Notları       ----------------------------------------------------------------------------------------

3D CNN ve 2D CNN hakkında tartışıldı. 3D CNN ile eğitilmeye daha sıcak bakılıyor. Veriseti 3D gruplara ayrıldı. Veriseti arttırılabilir OASIS+ADNI. 3D'nin daha fazla araştırılması kararlaştırıldı.

Django ve ReactNative ile web de ilerlemeye devam edilecek.
