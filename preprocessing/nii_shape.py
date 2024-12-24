import nibabel as nib

def print_nifti_shapes(file_path1, file_path2):
    # İlk NIfTI dosyasını yükle ve NumPy dizisine dönüştür
    nifti_image1 = nib.load(file_path1)
    numpy_array1 = nifti_image1.get_fdata()
    
    # İkinci NIfTI dosyasını yükle ve NumPy dizisine dönüştür
    nifti_image2 = nib.load(file_path2)
    numpy_array2 = nifti_image2.get_fdata()
    
    # Her iki dizinin şekillerini yazdır
    print(f"First NIfTI file shape: {numpy_array1.shape}")
    print(f"Second NIfTI file shape: {numpy_array2.shape}")

# Kullanım örneği
file_path1 = '/home/user34/Desktop/TEST/ADNI_006_S_4546_reoriented.nii'
file_path2 = '/home/user34/Downloads/1000lik/AD/ADNI_005_S_0929_MR_MPR__GradWarp__B1_Correction__N3_Br_20070918115600657_S31919_I73546.nii'

print_nifti_shapes(file_path1, file_path2)
