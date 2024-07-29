""" Đây là đoạn mã Python thực hiện lấy ra 1 mẫu dữ liệu để thống kê, có khoảng 200 nghệ sĩ. """

# Khai báo các thư viện cần thiết
import pandas as pd
from sklearn.model_selection import train_test_split


def read_data(file_path):
    """Đọc dữ liệu từ file Excel và kiểm tra lỗi."""
    try:
        df = pd.read_excel(file_path)
        if df.empty:
            raise ValueError("File dữ liệu trống.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File không tồn tại tại đường dẫn: {file_path}")
    except Exception as e:
        raise Exception(f"Lỗi khi đọc file: {str(e)}")

def check_column_exists(df, column_name):
    """Kiểm tra sự tồn tại của cột trong DataFrame."""
    if column_name not in df.columns:
        raise ValueError(f"Cột '{column_name}' không tồn tại trong dữ liệu.")

def validate_sample_size(df, sample_size):
    """Kiểm tra kích thước mẫu có hợp lệ không."""
    if not isinstance(sample_size, int) or sample_size <= 0:
        raise ValueError("Kích thước mẫu phải là số nguyên dương.")
    if sample_size > len(df):
        raise ValueError("Kích thước mẫu không được lớn hơn số lượng bản ghi trong dữ liệu.")

def check_missing_values(df, column_name):
    """Kiểm tra giá trị thiếu trong cột phân tầng."""
    if df[column_name].isnull().any():
        raise ValueError(f"Cột '{column_name}' chứa giá trị thiếu.")

def remove_small_classes(df, stratify_column, min_count=4):
    """Loại bỏ các lớp có số lượng phần tử nhỏ hơn min_count."""
    class_counts = df[stratify_column].value_counts()
    small_classes = class_counts[class_counts < min_count].index
    if not small_classes.empty:
        df = df[~df[stratify_column].isin(small_classes)]
    return df

def validate_class_count(df, stratify_column, sample_size):
    """Kiểm tra số lượng lớp phân tầng có nhỏ hơn hoặc bằng kích thước mẫu không."""
    num_classes = df[stratify_column].nunique()
    if sample_size < num_classes:
        raise ValueError(f"Kích thước mẫu ({sample_size}) phải lớn hơn hoặc bằng số lượng lớp phân tầng ({num_classes}).")

def stratified_sampling(df, stratify_column, sample_size):
    """Thực hiện lấy mẫu ngẫu nhiên phân tầng và kiểm tra lỗi."""
    try:
        df_sample, _ = train_test_split(df, test_size=(len(df) - sample_size) / len(df), stratify=df[stratify_column], random_state=42)
        return df_sample
    except ValueError as e:
        raise ValueError(f"Lỗi khi lấy mẫu: {str(e)}")
    except Exception as e:
        raise Exception(f"Lỗi không xác định khi lấy mẫu: {str(e)}")

def save_sample(df_sample, output_file):
    """Lưu mẫu vào file Excel và kiểm tra lỗi."""
    try:
        df_sample.to_excel(output_file, index=False)
    except Exception as e:
        raise Exception(f"Lỗi khi lưu file mẫu: {str(e)}")

def main(file_path, stratify_column, sample_size, output_file):
    try:
        # Đọc dữ liệu
        df = read_data(file_path)

        # Kiểm tra cột phân tầng
        check_column_exists(df, stratify_column)

        # Kiểm tra giá trị thiếu trong cột phân tầng
        check_missing_values(df, stratify_column)

        # Loại bỏ các lớp có ít hơn 2 phần tử
        df = remove_small_classes(df, stratify_column)

        # Kiểm tra kích thước mẫu
        validate_sample_size(df, sample_size)

        # Kiểm tra số lượng lớp phân tầng
        validate_class_count(df, stratify_column, sample_size)

        # Lấy mẫu ngẫu nhiên phân tầng
        df_sample = stratified_sampling(df, stratify_column, sample_size)

        # Lưu mẫu vào file mới
        save_sample(df_sample, output_file)

        print(f"Đã lấy mẫu thành công và lưu vào file: {output_file}")

    except FileNotFoundError as e:
        print(f"Đã xảy ra lỗi: {str(e)}. Vui lòng kiểm tra đường dẫn file.")
    except ValueError as e:
        print(f"Đã xảy ra lỗi: {str(e)}. Vui lòng kiểm tra giá trị nhập vào.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {str(e)}. Vui lòng kiểm tra lại.")

if __name__ == "__main__":
    # Đường dẫn file đầu vào và đầu ra
    input_file = 'C:/CHOICHOI/Statistics_Artist/data/nghesi.xlsx'
    output_file = 'C:/CHOICHOI/Statistics_Artist/results/200samples.xlsx'
    stratify_column = 'star'
    sample_size = 200

    # Chạy chương trình chính
    main(input_file, stratify_column, sample_size, output_file)