"""import os
import numpy as np
import cv2

def convert_npz_to_video(input_folder, output_folder, num_files=12):
    # Eğer çıktı klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Klasördeki tüm .npz dosyalarını listele
    npz_files = [f for f in os.listdir(input_folder) if f.endswith('.npz')]
    
    # İlk `num_files` kadar dosyayı seç
    selected_files = [npz_files[i] for i in (0, 2, 10, 15, 20, 25)]
    
    for npz_file in selected_files:
        file_path = os.path.join(input_folder, npz_file)
        # .npz dosyasını yükle ve numpy array'e çevir
        data = np.load(file_path)
        image = data['image']  # 'image' anahtarını kullanarak veriyi çek
        
        # Her axial dilimi (image[i,:,:]) birer frame olarak işleyip video oluştur
        height, width = image.shape[1], image.shape[2]
        output_video_path = os.path.join(output_folder, npz_file.replace('.npz', '.avi'))
        
        # VideoWriter objesi oluştur
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI formatı için codec
        out = cv2.VideoWriter(output_video_path, fourcc, 5, (width, height), isColor=False)  # 5 fps, grayscale
        
        # Her axial dilimi bir frame olarak ekle
        for i in range(image.shape[0]):
            frame = image[i, :, :]
            # Frame değerlerini normalize et (isteğe bağlı)
            frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            out.write(frame)
        
        # VideoWriter objesini serbest bırak
        out.release()
        print(f"Video saved: {output_video_path}")

# Giriş ve çıkış klasörlerini belirle
input_folder = '/home/user34/Desktop/TEST/data_npy_2/AD'  # Buraya npz dosyalarının olduğu klasör yolunu girin
output_folder = 'output_videos_1'  # Çıktı klasörünüz

# Fonksiyonu çalıştır
convert_npz_to_video(input_folder, output_folder)"""

"""import os
import numpy as np
import cv2

def convert_npz_to_video_sagittal(input_folder, output_folder, num_files=12):
    # Eğer çıktı klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Klasördeki tüm .npz dosyalarını listele
    npz_files = [f for f in os.listdir(input_folder) if f.endswith('.npz')]
    
    # İlk `num_files` kadar dosyayı seç
    selected_files = [npz_files[i] for i in (0, 2, 10, 15, 20, 25)]
    
    for npz_file in selected_files:
        file_path = os.path.join(input_folder, npz_file)
        # .npz dosyasını yükle ve numpy array'e çevir
        data = np.load(file_path)
        image = data['image']  # 'image' anahtarını kullanarak veriyi çek
        
        # Sagittal dilimler (image[:, i, :]) üzerinden işlem yap
        height, width = image.shape[0], image.shape[2]
        output_video_path = os.path.join(output_folder, npz_file.replace('.npz', '_sagittal.avi'))
        
        # VideoWriter objesi oluştur
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI formatı için codec
        out = cv2.VideoWriter(output_video_path, fourcc, 5, (width, height), isColor=False)  # 5 fps, grayscale
        
        # Her sagittal dilimi bir frame olarak ekle
        for i in range(image.shape[1]):
            frame = image[:, i, :]
            # Frame değerlerini normalize et (isteğe bağlı)
            frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            out.write(frame)
        
        # VideoWriter objesini serbest bırak
        out.release()
        print(f"Sagittal video saved: {output_video_path}")

# Giriş ve çıkış klasörlerini belirle
input_folder = '/home/user34/Desktop/TEST/data_npy_2/AD'
output_folder = 'output_videos_2'

# Fonksiyonu çalıştır
convert_npz_to_video_sagittal(input_folder, output_folder)"""

import os
import numpy as np
import cv2

def convert_npz_to_video_coronal(input_folder, output_folder, num_files=12):
    # Eğer çıktı klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Klasördeki tüm .npz dosyalarını listele
    npz_files = [f for f in os.listdir(input_folder) if f.endswith('.npz')]
    
    # İlk `num_files` kadar dosyayı seç
    selected_files = [npz_files[i] for i in (0, 2, 10, 15, 20, 25)]
    
    for npz_file in selected_files:
        file_path = os.path.join(input_folder, npz_file)
        # .npz dosyasını yükle ve numpy array'e çevir
        data = np.load(file_path)
        image = data['image']  # 'image' anahtarını kullanarak veriyi çek
        
        # Coronal dilimler (image[:, :, i]) üzerinden işlem yap
        height, width = image.shape[1], image.shape[2]
        output_video_path = os.path.join(output_folder, npz_file.replace('.npz', '_coronal.avi'))
        
        # VideoWriter objesi oluştur
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI formatı için codec
        out = cv2.VideoWriter(output_video_path, fourcc, 5, (width, height), isColor=False)  # 5 fps, grayscale
        
        # Her coronal dilimi bir frame olarak ekle
        for i in range(image.shape[0]):
            frame = image[i, :, :]
            # Frame değerlerini normalize et (isteğe bağlı)
            frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            out.write(frame)
        
        # VideoWriter objesini serbest bırak
        out.release()
        print(f"Coronal video saved: {output_video_path}")

# Giriş ve çıkış klasörlerini belirle
input_folder = '/home/user34/Desktop/TEST/data_npy_2/AD'
output_folder = 'output_videos_AD'

# Fonksiyonu çalıştır
convert_npz_to_video_coronal(input_folder, output_folder)


