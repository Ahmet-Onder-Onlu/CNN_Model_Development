import zipfile
import nibabel as nib
import io
import tempfile
import shutil
import os

# Zip dosyasının yolu
zip_file_path = '/home/user34/Downloads/TEST/TEST/ADNI/021_S_0343/MPR-R__GradWarp__N3/2006-04-06_09_24_45.0/I33636/TEST.zip'

# Zip dosyasının içindeki NIfTI dosyasının yolu (klasör ile birlikte)
nifti_filename = '_S12835_I33636.nii'

# Zip dosyasını aç
with zipfile.ZipFile(zip_file_path, 'r') as zf:
    # NIfTI dosyasını zip dosyasının içinden oku
    with zf.open(nifti_filename) as nifti_file:
        # NIfTI dosyasını bellekteki bir byte akışına dönüştür
        file_in_memory = io.BytesIO(nifti_file.read())
        
        # Geçici bir dosya oluştur
        with tempfile.NamedTemporaryFile(delete=False, suffix='.nii') as temp_file:
            # Byte akışını geçici dosyaya yaz
            temp_file.write(file_in_memory.getvalue())
            temp_file_path = temp_file.name
        
        # Geçici dosyayı nibabel ile yükle
        nifti_img = nib.load(temp_file_path)
        
        # NIfTI verisini numpy dizisine dönüştür
        nifti_data = nifti_img.get_fdata()

        # Veriyi kontrol et
        print(nifti_data.shape)

        # Geçici dosyayı temizle
        os.remove(temp_file_path)