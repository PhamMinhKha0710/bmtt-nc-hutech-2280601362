# Bảo Mật Thông Tin và Mã Hóa
> Phạm Minh Kha - 2280601362

Repository này chứa các bài thực hành về bảo mật thông tin và mã hóa, từ cơ bản đến nâng cao. Mỗi lab tập trung vào các khía cạnh khác nhau của bảo mật thông tin và mật mã học.

## Cấu Trúc Repository

Repository được tổ chức thành các thư mục lab khác nhau:

```
├── Lab_01/     # Python cơ bản
├── Lab_02/     # Caesar Cipher và ứng dụng web
├── lab-03/     # Mã hóa khóa công khai (RSA và ECC)
├── lab-04/     # Socket, Hash, WebSocket và Diffie-Hellman
└── lab-05/     # Lab mới nhất
```

## Nội Dung Các Lab

### Lab 1: Lập Trình Python Cơ Bản
- **Nội dung:** Các kỹ thuật cơ bản trong Python - nhập xuất, biến, toán tử, cấu trúc điều khiển
- **Thư mục:** `Lab_01/`
- **Các bài tập chính:**
  - Xử lý đầu vào/đầu ra cơ bản
  - Tính toán với biến và toán tử
  - Thực hiện các tính toán đơn giản

### Lab 2: Caesar Cipher và Ứng Dụng Web
- **Nội dung:** Triển khai mã hóa Caesar trong ứng dụng web Flask
- **Thư mục:** `Lab_02/`
- **Các thành phần chính:**
  - Module mã hóa Caesar
  - Ứng dụng web với Flask
  - API cho mã hóa/giải mã
  - Templates giao diện người dùng

### Lab 3: Mã Hóa Khóa Công Khai
- **Nội dung:** Triển khai và sử dụng các thuật toán mã hóa RSA và ECC
- **Thư mục:** `lab-03/`
- **Các thành phần chính:**
  - RSA Cipher với PyQt5 GUI
  - ECC Cipher với PyQt5 GUI
  - API cho các thuật toán mã hóa
  - Chức năng ký và xác thực chữ ký số

### Lab 4: Bảo Mật Truyền Thông
- **Nội dung:** Socket, Hash, WebSocket và trao đổi khóa Diffie-Hellman
- **Thư mục:** `lab-04/`
- **Các module chính:**
  - `aes_rsa_socket/`: Mã hóa kết hợp AES và RSA trong socket
  - `hash/`: Các thuật toán hash (MD5, SHA-256, SHA-3, BLAKE2)
  - `dh_key_pair/`: Triển khai trao đổi khóa Diffie-Hellman
  - `websocket/`: Ứng dụng chat an toàn với WebSocket

## Yêu Cầu và Cài Đặt

### Yêu cầu chung
- Python 3.7+
- pip (trình quản lý gói Python)

### Cài đặt dependencies
Mỗi lab có file `requirements.txt` riêng. Để cài đặt dependencies cho một lab cụ thể:

```bash
cd <thư_mục_lab>
pip install -r requirements.txt
```

### Các thư viện chính được sử dụng
- Flask: Cho phát triển web
- PyQt5: Cho giao diện đồ họa
- PyCryptodome: Cho các thuật toán mã hóa
- websockets: Cho WebSocket
- requests: Cho gọi API

## Chạy Các Lab

### Lab 1
Các script Python đơn giản, chạy trực tiếp:
```bash
python Lab_01/ex01/test1.py
```

### Lab 2
Khởi động server Flask:
```bash
cd Lab_02
python app.py
```
Sau đó mở trình duyệt tại http://localhost:5000

### Lab 3
Chạy ứng dụng RSA hoặc ECC:
```bash
cd lab-03
python rsa_cipher.py
# hoặc
python ecc_cipher.py
```

### Lab 4
#### AES-RSA Socket
```bash
cd lab-04/aes_rsa_socket
# Khởi động server trước:
python server.py
# Sau đó khởi động client trong terminal khác:
python client.py
```

#### Hash Functions
```bash
cd lab-04/hash
python md5_library.py
```

## Tài Liệu Tham Khảo
- [Các câu hỏi và trả lời cho buổi vấn đáp](README_QA.md)
- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/)

## Thông Tin Liên Hệ
- **Sinh viên:** Phạm Minh Kha
- **MSSV:** 2280601362
- **Lớp:** Bảo mật thông tin - Hutech
