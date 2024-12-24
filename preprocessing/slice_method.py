import nibabel as nib
import numpy as np
import os

def crop_center(image, target_shape=(160, 192, 192)):
    """
    Verilen 3D görüntüyü ortadan slice alarak belirli boyutlara getirir.
    
    Args:
        image (numpy array): 3D numpy array olarak görüntü.
        target_shape (tuple): Hedef boyutlar (depth, height, width).
    
    Returns:
        cropped_image (numpy array): Kesilmiş 3D görüntü.
    """
    current_shape = image.shape
    crop_slices = []

    for dim in range(3):
        start = (current_shape[dim] - target_shape[dim]) // 2
        end = start + target_shape[dim]
        crop_slices.append(slice(start, end))

    return image[tuple(crop_slices)]

def process_nii_file(input_path, output_path, target_shape=(160, 192, 192)):
    """
    Bir NIfTI dosyasını okur, hedef boyutlarda ortadan slice alır ve yeni bir NIfTI dosyası olarak kaydeder.
    
    Args:
        input_path (str): Giriş NIfTI dosyasının yolu.
        output_path (str): Çıkış NIfTI dosyasının kaydedileceği yol.
        target_shape (tuple): Hedef boyutlar (depth, height, width).
    """
    # NIfTI dosyasını yükle
    nii = nib.load(input_path)
    image = nii.get_fdata()

    # Görüntüyü kes
    cropped_image = crop_center(image, target_shape)

    # Yeni bir NIfTI objesi oluştur
    cropped_nii = nib.Nifti1Image(cropped_image, affine=nii.affine)

    # Yeni dosyayı kaydet
    nib.save(cropped_nii, output_path)
    print(f"Saved cropped image to {output_path}")

# Örnek kullanım:
input_dir = "/home/user34/Desktop/TEST/distinct_shapes"
output_dir = "reshape_zoom"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".nii") or filename.endswith(".nii.gz"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        process_nii_file(input_path, output_path)
