import os
import numpy as np
import nibabel as nib
from scipy.ndimage import zoom

def save_as_nii(image, output_path, affine):
    # Yeni Nifti dosyasını oluşturma
    new_img = nib.Nifti1Image(image, affine)
    # Dosyayı kaydetme
    nib.save(new_img, output_path)

def process_nii_files(input_dir, output_dir, target_shape=(256, 256, 256)):
    # Yeni .nii dosyalarını kaydetmek için klasör oluştur
    os.makedirs(output_dir, exist_ok=True)

    # Klasör içindeki tüm .nii dosyalarını işle
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.nii') or file.endswith('.nii.gz'):
                # Dosya yolunu oluştur
                nii_path = os.path.join(root, file)
                
                # Nifti dosyasını yükle
                img = nib.load(nii_path)
                img_data = img.get_fdata()
                img_affine = img.affine  # Orijinal affine matrisini sakla

                # Orijinal boyutları alalım
                original_shape = img_data.shape

                # Her eksen için ölçek oranını hesaplayalım
                zoom_factors = [t / o for t, o in zip(target_shape, original_shape)]

                # Yeniden boyutlandırma işlemini yapalım
                resized_img = zoom(img_data, zoom_factors, order=3)  # order=3 cubic interpolation kullanır

                # Yeni .nii dosyası olarak kaydedilecek yol
                output_filename = os.path.splitext(file)[0] + '_resized.nii'
                output_path = os.path.join(output_dir, output_filename)

                # .nii dosyasını kaydet
                save_as_nii(resized_img, output_path, img_affine)
                print(f"Processed and saved: {output_path}")

# Girdi ve çıktı klasör yolları
input_directory = '/home/user34/Desktop/TEST/distinct_shapes'
output_directory = 'nii_reshape'

# İşleme başla
process_nii_files(input_directory, output_directory)
