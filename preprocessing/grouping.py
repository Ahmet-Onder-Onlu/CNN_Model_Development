# -- coding: utf-8 --
"""
Created on Thu Aug  8 14:27:51 2024

@author: hp
"""
import re
from collections import defaultdict
from tqdm import tqdm
import numpy as np
from PIL import Image
import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, f1_score
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models

# Dosya yollarını tanımla
DATA_PATH = "C:/Users/furka/PycharmProjects/Arvis/Data2/Data"


def validate_filename(filename):
    pattern = re.compile(r'OAS1_\d+_MR\d+_mpr-\d+_\d+.jpg')
    return bool(pattern.match(filename))

def get_info_from_filename(filename):
    pattern = re.compile(r'OAS1_(\d+)_MR(\d+)_mpr-(\d+)_(\d+).jpg')
    match = pattern.match(filename)
    if match:
        patient_id = match.group(1)
        mr_id = match.group(2)
        scan_id = match.group(3)
        layer_id = match.group(4)
        return patient_id, mr_id, scan_id, layer_id
    return None

def group_files_by_patient_scan(files):
    groups = defaultdict(list)

    for filename in files:
        if validate_filename(filename):
            info = get_info_from_filename(filename)
            if info:
                patient_id, mr_id, scan_id, layer_id = info
                key = (patient_id, mr_id, scan_id)
                groups[key].append((layer_id, filename))

    for key in groups:
        groups[key].sort(key=lambda x: int(x[0]))
        groups[key] = [filename for _, filename in groups[key]]

    return groups


def create_ref_df(dataset_path):
    paths, labels = [], []
    patient_ids, mr_ids, scan_ids, layer_ids = [], [], [], []

    for folder in os.listdir(dataset_path):
        for file in os.listdir(os.path.join(dataset_path, folder)):
            if not validate_filename(file):
                raise ValueError(f'Invalid filename: {folder}/{file}')

            patient_id, mr_id, scan_id, layer_id = get_info_from_filename(file)

            paths.append(os.path.join(dataset_path, folder, file))
            labels.append(folder)
            patient_ids.append(patient_id)
            mr_ids.append(mr_id)
            scan_ids.append(scan_id)
            layer_ids.append(layer_id)

    ref_df = pd.DataFrame({
        'path': paths,
        'label': labels,
        'patient_id': patient_ids,
        'mr_id': mr_ids,
        'scan_id': scan_ids,
        'layer_id': layer_ids
    })

    ref_df = ref_df.astype({
        'path': 'string',
        'label': 'string',
        'patient_id': 'int64',
        'mr_id': 'int64',
        'scan_id': 'int64',
        'layer_id': 'int64'
    })

    return ref_df

def split_dataset(ref_df, train_size=0.6, val_size=0.2, test_size=0.2):
    patient_ids = ref_df['patient_id'].unique()
    train_val_ids, test_ids = train_test_split(patient_ids, test_size=test_size, random_state=42)
    train_ids, val_ids = train_test_split(train_val_ids, test_size=val_size / (train_size + val_size), random_state=42)

    train_df = ref_df[ref_df['patient_id'].isin(train_ids)]
    val_df = ref_df[ref_df['patient_id'].isin(val_ids)]
    test_df = ref_df[ref_df['patient_id'].isin(test_ids)]

    return train_df, val_df, test_df


def load_images(ref_df, target_size=(224, 224)):
    labels = []
    images = []
    paths = []

    grouped = ref_df.groupby(['patient_id', 'mr_id', 'scan_id'])

    for group_key, group_df in grouped:
        group_images = []
        group_labels = []
        group_paths = []

        for idx, row in tqdm(group_df.iterrows(), total=group_df.shape[0]):
            img = Image.open(row['path']).convert('L')
            img = img.resize(target_size)  # Resize to target size (224x224)
            img = np.array(img) / 255.0  # Normalize the image
            group_images.append(img)
            group_labels.append(row['label'])
            group_paths.append(row['path'])

        images.append(np.stack(group_images, axis=-1))  # Combine into 3D
        labels.append(group_labels[0])  # Assuming all labels in the group are the same
        paths.append(group_paths)

    return images, labels, paths


# Veri setinizin yolunu belirtin
dataset_path = DATA_PATH

# 1. Referans DataFrame'i oluşturun
ref_df = create_ref_df(dataset_path)

# 2. Veriyi eğitim, doğrulama ve test setlerine ayırın
train_df, val_df, test_df = split_dataset(ref_df)

# 3. Eğitim, doğrulama ve test setlerini yükleyin
train_images, train_labels, train_paths = load_images(train_df)
val_images, val_labels, val_paths = load_images(val_df)
test_images, test_labels, test_paths = load_images(test_df)

# Sonuçları kontrol edin
print(f"Eğitim setindeki 3D görüntü sayısı: {len(train_images)}")
print(f"Doğrulama setindeki 3D görüntü sayısı: {len(val_images)}")
print(f"Test setindeki 3D görüntü sayısı: {len(test_images)}")


def create_3d_cnn_model(input_shape, num_classes):
    model = models.Sequential()

    # First Convolutional Block
    model.add(layers.Conv3D(32, (3, 3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(layers.MaxPooling3D((2, 2, 2)))
    model.add(layers.BatchNormalization())

    # Second Convolutional Block
    model.add(layers.Conv3D(64, (3, 3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling3D((2, 2, 2)))
    model.add(layers.BatchNormalization())

    # Third Convolutional Block
    model.add(layers.Conv3D(128, (3, 3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling3D((2, 2, 2)))
    model.add(layers.BatchNormalization())

    # Fourth Convolutional Block
    model.add(layers.Conv3D(256, (3, 3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling3D((2, 2, 2)))
    model.add(layers.BatchNormalization())

    # Flatten and Dense Layers
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return model


class F1ScoreCallback(tf.keras.callbacks.Callback):
    def __init__(self, validation_data):
        self.validation_data = validation_data

    def on_epoch_end(self, epoch, logs=None):
        val_images, val_labels = self.validation_data
        val_predictions = np.argmax(self.model.predict(val_images), axis=-1)
        f1 = f1_score(val_labels, val_predictions, average='weighted')
        print(f' - val_f1_score: {f1:.4f}')


# Model parametrelerini tanımlayın
input_shape = (
len(train_images[0]), train_images[0][0].shape[0], train_images[0][0].shape[1], 1)  # (depth, height, width, channels)
num_classes = len(set(train_labels))  # Örnek olarak 4 sınıf

# Modeli oluşturun
model = create_3d_cnn_model(input_shape, num_classes)

# Model özetini yazdırın
model.summary()

# Modeli eğitin
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
f1_score_callback = F1ScoreCallback(validation_data=(val_images, val_labels))

history = model.fit(
    np.array(train_images),
    np.array(train_labels),
    validation_data=(np.array(val_images), np.array(val_labels)),
    epochs=30,
    batch_size=2,
    callbacks=[early_stopping, f1_score_callback]
)

# Modeli değerlendirin
test_loss, test_accuracy = model.evaluate(np.array(test_images), np.array(test_labels))
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# Test seti ile tahmin yapın
test_predictions = np.argmax(model.predict(np.array(test_images)), axis=-1)

# Karışıklık matrisini oluşturun
cm = confusion_matrix(test_labels, test_predictions)
cm_display = ConfusionMatrixDisplay(confusion_matrix=cm)
cm_display.plot(cmap=plt.cm.Blues)
plt.show()
