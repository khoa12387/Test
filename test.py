import os
import gdown
import zipfile
import pandas as pd

def download_and_extract_data(url, data_dir):
    """Tải xuống dữ liệu từ URL đã cho và giải nén vào thư mục được chỉ định.

    Args:
        url (str): URL của tệp .zip cần tải xuống.
        thu_muc_du_lieu (str): Thư mục để lưu dữ liệu đã tải xuống và giải nén.

    """

    try:  # Download file zip sử dụng gdown
        output_filename = gdown.download(url, quiet=False, output=data_dir)

        # Extract the .zip file using zipfile
        with zipfile.ZipFile(output_filename, 'r') as zip_ref:
            zip_ref.extractall(data_dir)

        print(f"Data downloaded and extracted successfully to {data_dir}")
    except zipfile.BadZipFile as e:
        print(f"Lỗi: File .zip không hợp lệ: {e}")
    except Exception as e:
        print(f"Lỗi giải nén file .zip: {e}")

def get_data_dimensions(csv_file):
    """Trả về số hàng và cột trong tệp CSV đã cho.

    Args:
        tep_csv (str): Đường dẫn đến tệp CSV.

    Returns:
        tuple: Bộ gồm số hàng và cột.
    """

    try:
        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        # Get the number of rows and columns
        num_rows = df.shape[0]
        num_columns = df.shape[1]

        return num_rows, num_columns

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None

def display_specific_columns(csv_file, output_file, columns):
    """Hiển thị các cột được chỉ định từ tệp CSV và lưu chúng vào tệp mới.

    Args:
        tep_csv (str): Đường dẫn đến tệp CSV.
        tep_ket_qua (str): Đường dẫn đến tệp kết quả.
        cac_cot (list): Danh sách tên cột cần hiển thị.

    Returns:
        None
    """

    try:
        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        # Select the specified columns
        selected_df = df[columns]

        # Save the selected columns to a new CSV file
        selected_df.to_csv(output_file, index=False)

        print(f"Specific columns saved to {output_file}")

    except Exception as e:
        print(f"Error displaying and saving specific columns: {e}")

if __name__ == "__main__":
    url = "https://drive.google.com/uc?id=1yyL20BNKv3PxJRJVjJ_2Q-HidvIUis45&export=download"
    data_dir = "Test"
    csv_file = os.path.join(data_dir, "customers-100.csv")  # Khi đã giải nén ra file "customer-100.csv"
    output_file = "result.csv"
    columns_to_display = ["Index", "Customer Id", "First Name", "Last Name", "Company","City","Country","Phone 1", "Phone 2" , "Email","Subscription Date","Website"]

    download_and_extract_data(url, data_dir)

    num_rows, num_columns = get_data_dimensions(csv_file)
    if num_rows is not None and num_columns is not None:
        print(f"The CSV file has {num_rows} rows and {num_columns} columns.")

    display_specific_columns(csv_file, output_file, columns_to_display)
