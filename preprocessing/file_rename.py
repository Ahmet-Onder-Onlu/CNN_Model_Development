"""import os

# Ana klasör yolunu belirleyin
main_folder = '/home/user34/Desktop/TEST/data_npy'

# Alt kategorileri belirleyin
categories = ['AD', 'CN', 'MCI', 'EMCI']

# Klasördeki her kategori için dosyaları yeniden adlandırma işlemi
for category in categories:
    category_path = os.path.join(main_folder, category)
    for filename in os.listdir(category_path):
        if filename.endswith('.npz'):
            # Dosya adının ".npz" den önceki kısmı: Örneğin "I66044"
            new_filename = filename.split('_')[-1]
            # Dosyanın tam eski ve yeni yolları
            old_filepath = os.path.join(category_path, filename)
            new_filepath = os.path.join(category_path, new_filename)
            # Dosyayı yeniden adlandırma
            os.rename(old_filepath, new_filepath)
            print(f"{filename} -> {new_filename} olarak yeniden adlandırıldı.")"""

"""import os
import pandas as pd

# Ana klasör yolunu belirleyin
main_folder = '/home/user34/Desktop/TEST/data_npy'

# Alt kategorileri belirleyin
categories = ['AD', 'CN', 'MCI', 'EMCI']

# DataFrame'i yükleyin (örnek olarak CSV'den okunuyor)
df = pd.read_excel('/home/user34/Desktop/TEST/homogeneous_filtered_data_250_per_group.xlsx')  # Burada kendi CSV dosyanızın yolunu belirtin

# Klasördeki her kategori için dosyaları yeniden adlandırma işlemi
for category in categories:
    category_path = os.path.join(main_folder, category)
    for filename in os.listdir(category_path):
        if filename.endswith('.npz'):
            # ".npz" den önceki kısmı al: Örneğin "I35928"
            image_data_id = filename.split('.npz')[0]
            
            # DataFrame'de "Image Data ID" sütununda bu değeri arayın
            match = df[df['Image Data ID'] == image_data_id]
            
            if not match.empty:
                # Eşleşen satırdaki "Subject" değerini al
                subject = match['Subject'].values[0]
                
                # Yeni dosya adı oluştur: "Subject_ImageDataID.npz" formatında
                new_filename = f"{subject}_{image_data_id}.npz"
                
                # Dosyanın tam eski ve yeni yolları
                old_filepath = os.path.join(category_path, filename)
                new_filepath = os.path.join(category_path, new_filename)
                
                # Dosyayı yeniden adlandırma
                os.rename(old_filepath, new_filepath)
                print(f"{filename} -> {new_filename} olarak güncellendi.")
            else:
                print(f"{filename} için eşleşme bulunamadı.")"""

import os
from collections import defaultdict

# Ana klasör yolunu belirtin
main_folder = '/home/user34/Desktop/TEST/data_npy'

# Alt kategorileri belirleyin
categories = ['AD', 'CN', 'MCI', 'EMCI']

# Benzersiz ID'leri saklayacağımız dictionary
unique_ids_per_category = defaultdict(set)

# Her kategori için benzersiz ID'leri toplama
for category in categories:
    category_path = os.path.join(main_folder, category)
    for filename in os.listdir(category_path):
        if filename.endswith('.npz'):
            # "002_S_0816_I40725.npz" gibi dosya adından "002_S_0816" kısmını al
            unique_id = '_'.join(filename.split('_')[:3])
            # Benzersiz ID'yi ilgili kategorinin set'ine ekle
            unique_ids_per_category[category].add(unique_id)

# Her kategori için benzersiz ID sayılarını yazdırma
for category, unique_ids in unique_ids_per_category.items():
    print(f"{category}: {len(unique_ids)}")


