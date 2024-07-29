""" Thống kê cơ bản trên tập dữ liệu mẫu """
import pandas as pd

# Đọc dữ liệu từ tập tin 200samples.xlsx
file_path = "C:/CHOICHOI/Statistics_Artist/results/200samples.xlsx"
data = pd.read_excel(file_path)

# Xem qua một số dòng dữ liệu đầu tiên
print(data.head(5))

# Số nghệ sĩ có heart >800
num_artists_heart_gt_800 = data[data['heart'] > 800]['artist'].nunique()
print(f"Số nghệ sĩ có heart > 800 là: {num_artists_heart_gt_800}")

# Thống kê tần suất nghệ sĩ có heart >500
frequency_artists_heart_gt_500 = data[data['heart'] > 500]['artist'].value_counts()
print(f"Thống kê tần suất nghệ sĩ có heart > 500 là: {frequency_artists_heart_gt_500}")

# Tính các đại lượng thống kê cơ bản trên cột dữ liệu 'heart'
heart_statistics = data['heart'].describe()
print("thống kê cơ bản trên cột dữ liệu 'heart' \n", heart_statistics)

# Thống kê describe trên các cột dữ liệu là số
describe_statistics = data.describe()
print("Kết quả thu được\n", describe_statistics)

# Lập bảng thống kê tần số của cột dữ liệu 'star'
star_frequency = data['star'].value_counts()
print("Bảng thống kê tần số của cột dữ liệu 'star' như sau:\n", star_frequency)

# Lập bảng truy vấn chéo dữ liệu giữa 'star' và 'word'
star_word_crosstab = pd.crosstab(data['star'], data['words'])
print("Bảng truy vấn chéo giữa 2 cột 'star' và 'word' như sau: \n \n", star_word_crosstab)