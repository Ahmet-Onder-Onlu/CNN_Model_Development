import os
import nibabel as nib
from deepbrain import Extractor
import numpy as np

def saveAsCompressedNumpyArray(image, save_path):
    # Save as compressed .npz file
    np.savez_compressed(save_path, image=image)

def process_nifti_files(input_folder, output_folder):
    categories = ['AD', 'CN', 'MCI', 'EMCI']
    
    for category in categories:
        category_input_path = os.path.join(input_folder, category)
        category_output_path = os.path.join(output_folder, category)
        
        if not os.path.exists(category_output_path):
            os.makedirs(category_output_path)
        
        for nii_file in os.listdir(category_input_path):
            if nii_file.endswith('.nii') or nii_file.endswith('.nii.gz'):
                nii_path = os.path.join(category_input_path, nii_file)
                
                # Load the nii file
                img = nib.load(nii_path).get_fdata()

                # Apply brain extraction
                ext = Extractor()
                prob = ext.run(img)

                # Create mask
                th = 0.5
                mask = prob
                mask[prob < th] = 0
                mask[prob >= th] = 1
                mask = mask.astype(int)

                # Remove Skull
                masked_img = np.multiply(img, mask)
                
                # Output numpy filename
                npz_filename = os.path.join(category_output_path, nii_file.replace('.nii', '.npz').replace('.nii.gz', '.npz'))
                
                # Save as compressed numpy array without padding
                saveAsCompressedNumpyArray(masked_img, npz_filename)

input_folder = '/home/user34/Desktop/TEST/1000lik_copy'
output_folder = 'data_npy'

process_nifti_files(input_folder, output_folder)
