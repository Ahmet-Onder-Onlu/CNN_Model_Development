import os
import nibabel as nib
from collections import defaultdict

# Nii dosyalarının bulunduğu ana dizin
veri_dizini = '/home/user34/Desktop/TEST/1000lik_copy'

# Farklı shape'leri saklamak ve sayısını tutmak için bir sözlük
shape_sayim = defaultdict(int)
counter = 0

# Dizin ve alt dizinler içindeki tüm dosyalar üzerinde gezinme
for alt_dizin, _, dosyalar in os.walk(veri_dizini):
    for dosya_adi in dosyalar:
        if dosya_adi.endswith('.nii') or dosya_adi.endswith('.nii.gz'):
            # Dosyanın tam yolu
            dosya_yolu = os.path.join(alt_dizin, dosya_adi)
            counter += 1

            # Nii dosyasını yükleme
            img = nib.load(dosya_yolu)

            # Dosyanın shape'ini alma
            shape = img.shape

            # Shape'in sayısını artırma
            shape_sayim[shape] += 1

# Kaç farklı shape olduğunu ekrana yazdırma
print(f"Farklı shape sayısı: {len(shape_sayim)}") 
print("Her shape için dosya sayısı:")
for shape, sayi in shape_sayim.items():
    print(f"Shape: {shape}, Dosya Sayısı: {sayi}")

print("Toplam dosya sayısı:", counter)
