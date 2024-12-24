import os
import random
from collections import defaultdict

def split_data_by_subject(input_folder, train_ratio=0.6, test_ratio=0.2, val_ratio=0.2):
    # Kontrol oranlarının toplamı 1 olmalı
    assert train_ratio + test_ratio + val_ratio == 1, "Bölme oranlarının toplamı 1 olmalı."

    # Kategoriler (AD, CN, MCI, EMCI)
    categories = ['AD', 'CN', 'MCI', 'EMCI']
    
    # Subject id bazında dosyaları gruplama
    subject_to_files = defaultdict(list)
    
    for category in categories:
        category_folder = os.path.join(input_folder, category)
        for filename in os.listdir(category_folder):
            if filename.endswith('.npz'):
                # Subject ID'yi dosya adından al
                subject_id = filename.split('_')[0]
                file_path = os.path.join(category_folder, filename)
                label = category  # Label dosyanın bulunduğu klasör olacak
                subject_to_files[subject_id].append((file_path, label))
    
    # Subject ID'leri karıştır
    subject_ids = list(subject_to_files.keys())
    random.shuffle(subject_ids)
    
    # Eğitim, test ve doğrulama setleri için indeks belirleme
    num_subjects = len(subject_ids)
    train_cutoff = int(num_subjects * train_ratio)
    test_cutoff = int(num_subjects * (train_ratio + test_ratio))
    
    train_subjects = subject_ids[:train_cutoff]
    test_subjects = subject_ids[train_cutoff:test_cutoff]
    val_subjects = subject_ids[test_cutoff:]
    
    # Eğitim, test ve doğrulama setlerini oluşturma
    train_data, test_data, val_data = [], [], []
    train_labels, test_labels, val_labels = [], [], []
    
    for subject_id in train_subjects:
        for file_path, label in subject_to_files[subject_id]:
            train_data.append(file_path)
            train_labels.append(label)
    
    for subject_id in test_subjects:
        for file_path, label in subject_to_files[subject_id]:
            test_data.append(file_path)
            test_labels.append(label)
    
    for subject_id in val_subjects:
        for file_path, label in subject_to_files[subject_id]:
            val_data.append(file_path)
            val_labels.append(label)
    
    return (train_data, train_labels), (test_data, test_labels), (val_data, val_labels)

# Ana klasör yolu
input_folder = 'data_npy'

# Veriyi böl
(train_data, train_labels), (test_data, test_labels), (val_data, val_labels) = split_data_by_subject(input_folder)

# Sonuçları kontrol edebilirsiniz
print("Eğitim seti:", len(train_data))
print("Test seti:", len(test_data))
print("Doğrulama seti:", len(val_data))
print("Eğitim seti etiketleri:", train_labels)
print("Test seti etiketleri:", test_labels)
print("Doğrulama seti etiketleri:", val_labels)
