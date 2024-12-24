import nibabel as nib

def get_orientation(nifti_image):
    header = nifti_image.header
    affine = nifti_image.affine
    orientation = nib.aff2axcodes(affine)
    return orientation

# Örnek kullanım
nifti_image = nib.load('/home/user34/Downloads/1000lik/AD/ADNI_002_S_0816_MR_MPR____N3_Br_20070217004849769_S19532_I40725.nii')
orientation = get_orientation(nifti_image)
print("Orientation:", orientation)