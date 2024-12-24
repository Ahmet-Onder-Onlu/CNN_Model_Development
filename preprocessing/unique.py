"""import os
import glob

# Kategorilerin bulunduğu ana klasörün yolu
base_folder = '/home/user34/Desktop/TEST/data_npy'

# Kategoriler
categories = ['AD', 'CN', 'MCI', 'EMCI']

# Her kategori için benzersiz dosya isimlerini sayacak bir fonksiyon
def count_unique_files(category_folder):
    # Kategori klasöründeki tüm dosyaların yollarını al
    files = glob.glob(os.path.join(category_folder, '*.npz'))
    # Benzersiz dosya isimlerini saklamak için bir küme oluştur
    unique_ids = set()
    counter = 0    
    for file in files:
        # Dosya adını al ve yol kısmını çıkar
        filename = os.path.basename(file)
        # Dosya adındaki ilk '_' karakterine kadar olan kısmı al (örneğin S9024)
        identifier = filename.split('_')[0]
        counter += 1
        if counter < 10 and counter > 0:
            print("identifier: ", identifier)
        # Benzersiz dosya isimlerine ekle
        unique_ids.add(identifier)
    
    # Benzersiz dosya isimlerinin sayısını döndür
    return len(unique_ids)

# Kategoriler altındaki benzersiz dosya isimlerini hesapla
for category in categories:
    category_path = os.path.join(base_folder, category)
    unique_count = count_unique_files(category_path)
    print(f'Kategori {category} altında benzersiz dosya sayısı: {unique_count}')"""

import pandas as pd

# Excel dosyasını okuma
file_path = '/home/user34/Desktop/TEST/homogeneous_filtered_data_250_per_group.xlsx'
df = pd.read_excel(file_path)

# Her Group için benzersiz Subject sayısını hesaplama
unique_subjects_per_group = df.groupby('Group')['Subject'].nunique()

# Sonucu yazdırma
print(unique_subjects_per_group)

