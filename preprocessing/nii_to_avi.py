import nibabel as nib
from deepbrain import Extractor
import cv2
import numpy as np

def saveAsVideo(image):
    # Height ve width dinamik olarak görüntü boyutlarına göre ayarlanıyor.
    height, width = image.shape[0], image.shape[1]

    # Video writer'ı initialize et
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    fps = 10
    video_filename = 'output_1.avi'
    out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))
    
    # 3. indis boyunca iterasyon yap
    for i in range(image.shape[2]):  # 3. boyut (Z) üzerinden iterasyon yapılıyor.
        data = image[:, :, i]  # 3. boyuta göre slice alınıyor
        data = cv2.normalize(data, None, 255, 0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        data_3D = cv2.merge([data, data, data])  # Grayscale görüntüyü 3 kanallı hale getir
        out.write(data_3D)
    
    out.release()

import nibabel as nib
from deepbrain import Extractor
# Load a nifti as 3d numpy image [H, W, D]
img = nib.load('ADNI_005_S_5119_MR_MT1__N3m_Br_20130429145738871_S185463_I369214.nii').get_fdata()

ext = Extractor()
prob = ext.run(img)

# mask
max_val = np.amax(prob)
th = 0.5
mask = prob
mask[prob < th] = 0
mask[prob >= th] = 1
mask = mask.astype(int)

# Skull'ı çıkar
masked_img = np.multiply(img, mask)

# Masked görüntüyü video olarak kaydet
saveAsVideo(img)
