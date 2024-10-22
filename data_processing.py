import os
import shutil
import random

# Đường dẫn đến thư mục chứa ảnh
correct_folder = '/mnt/d/training_yolo/sitting_good'  # Thư mục ngồi đúng
wrong_folder = '/mnt/d/training_yolo/sitting_bad'      # Thư mục ngồi sai

# Đường dẫn đến thư mục mới
base_dir = 'data'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')

# Tạo thư mục nếu chưa tồn tại
for directory in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(directory, 'sitting_good'), exist_ok=True)
    os.makedirs(os.path.join(directory, 'sitting_bad'), exist_ok=True)

# Chia tỷ lệ dữ liệu (70% huấn luyện, 20% xác thực, 10% kiểm tra)
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Hàm chia dữ liệu
def split_data(source_folder, destination_folder, ratios):
    # Lấy danh sách file
    files = os.listdir(source_folder)
    random.shuffle(files)  # Xáo trộn file để chia ngẫu nhiên
    total_files = len(files)

    # Tính số lượng file cho mỗi tập
    train_count = int(total_files * ratios[0])
    val_count = int(total_files * ratios[1])
    
    # Chia và di chuyển file
    for i, file in enumerate(files):
        if i < train_count:
            shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'train', os.path.basename(source_folder)))
        elif i < train_count + val_count:
            shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'val', os.path.basename(source_folder)))
        else:
            shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'test', os.path.basename(source_folder)))

# Chia dữ liệu cho cả hai thư mục
split_data(correct_folder, base_dir, [train_ratio, val_ratio])
split_data(wrong_folder, base_dir, [train_ratio, val_ratio])
