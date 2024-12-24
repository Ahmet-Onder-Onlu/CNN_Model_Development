import os
import nibabel as nib
from collections import defaultdict
import shutil

# Nii dosyalarının bulunduğu ana dizin
veri_dizini = '/home/user34/Desktop/TEST/1000lik_copy'

# Farklı shape'leri saklamak ve sayısını tutmak için bir sözlük
shape_sayim = defaultdict(list)

# Farklı shape'leri saklayacağımız dizin
hedef_dizin = 'distinct_shapes'
os.makedirs(hedef_dizin, exist_ok=True)  # Klasör yoksa oluşturulur

# Dizin ve alt dizinler içindeki tüm dosyalar üzerinde gezinme
for alt_dizin, _, dosyalar in os.walk(veri_dizini):
    for dosya_adi in dosyalar:
        if dosya_adi.endswith('.nii') or dosya_adi.endswith('.nii.gz'):
            # Dosyanın tam yolu
            dosya_yolu = os.path.join(alt_dizin, dosya_adi)

            # Nii dosyasını yükleme
            img = nib.load(dosya_yolu)

            # Dosyanın shape'ini alma
            shape = img.shape

            # Shape'lere göre dosya yollarını saklama
            if shape not in shape_sayim:
                shape_sayim[shape].append(dosya_yolu)

# Her farklı shape'den bir dosyayı kopyalama
for shape, dosya_yollari in shape_sayim.items():
    # İlk dosya yolunu al ve kopyala
    ornek_dosya = dosya_yollari[0]
    hedef_yol = os.path.join(hedef_dizin, os.path.basename(ornek_dosya))
    
    # Dosyayı kopyala
    shutil.copy(ornek_dosya, hedef_yol)
    print(f"Shape: {shape} - Dosya kopyalandı: {ornek_dosya}")

print("Tüm farklı shape'lerden birer dosya kopyalandı.")
