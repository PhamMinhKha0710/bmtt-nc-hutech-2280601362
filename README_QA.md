# Câu Hỏi và Câu Trả Lời cho Labs 1-4

Tài liệu này cung cấp bộ câu hỏi và câu trả lời tham khảo cho các buổi vấn đáp, bao gồm nội dung từ Lab 1 đến Lab 4.

## Lab 1: Python Basics

### Fundamentals

#### Q1: Tại sao chúng ta cần phân biệt giữa kiểu dữ liệu số nguyên (int) và số thực (float) trong Python? Hãy cho ví dụ về một tình huống mà việc chuyển đổi giữa hai kiểu dữ liệu này là cần thiết.

**Trả lời:**
- **Lý do phân biệt:**
  - **Số nguyên (int)** được sử dụng để biểu diễn các số không có phần thập phân, có thể lưu trữ chính xác các số lớn.
  - **Số thực (float)** biểu diễn số có phần thập phân, nhưng có giới hạn về độ chính xác do biểu diễn nhị phân.
  - Mỗi kiểu dữ liệu được lưu trữ khác nhau trong bộ nhớ và có các phép toán tối ưu riêng.

- **Ví dụ về chuyển đổi:**
  - Khi tính toán tiền lương: Số giờ làm có thể là số thực (7.5 giờ), nhưng khi hiển thị số tiền cần làm tròn thành số nguyên.
  ```python
  # Tính lương
  hours_worked = 7.5  # float
  hourly_rate = 15.0  # float
  salary = hours_worked * hourly_rate  # 112.5
  
  # Chuyển sang int khi cần làm tròn (không còn phần thập phân)
  rounded_salary = int(salary)  # 112
  ```
  
  - Khi chia hai số nguyên nhưng cần kết quả chính xác:
  ```python
  # Chia số nguyên sẽ bị cắt phần thập phân trong Python 2
  result_int = 5 / 2  # Kết quả là 2 trong Python 2 (trong Python 3 là 2.5)
  
  # Chuyển một số sang float trước khi chia
  result_float = 5 / float(2)  # Kết quả là 2.5
  # hoặc
  result_float = float(5) / 2  # Kết quả là 2.5
  ```

#### Q2: Giải thích sự khác biệt giữa input() và print() trong Python. Làm thế nào để xử lý khi người dùng nhập một số thay vì một chuỗi?

**Trả lời:**
- **input():**
  - Là hàm đầu vào, dùng để nhận dữ liệu từ người dùng qua bàn phím.
  - Luôn trả về một chuỗi (string), bất kể người dùng nhập gì.
  - Có thể hiển thị thông báo cho người dùng biết cần nhập gì.

- **print():**
  - Là hàm đầu ra, dùng để hiển thị dữ liệu ra màn hình.
  - Có thể hiển thị nhiều loại dữ liệu khác nhau.
  - Có thể định dạng cách hiển thị dữ liệu.

- **Xử lý khi người dùng nhập số:**
  - Sử dụng các hàm chuyển đổi kiểu dữ liệu như `int()` hoặc `float()`.
  - Nên kết hợp với try-except để xử lý lỗi khi người dùng nhập sai:
  
  ```python
  try:
      age_str = input("Nhập tuổi của bạn: ")
      age = int(age_str)  # Chuyển chuỗi thành số nguyên
      print("Tuổi của bạn là:", age)
  except ValueError:
      print("Lỗi: Vui lòng nhập một số nguyên cho tuổi!")
  
  # Hoặc với số thực
  try:
      height_str = input("Nhập chiều cao của bạn (m): ")
      height = float(height_str)  # Chuyển chuỗi thành số thực
      print("Chiều cao của bạn là:", height, "mét")
  except ValueError:
      print("Lỗi: Vui lòng nhập một số cho chiều cao!")
  ```

### Variables and Operations

#### Q3: Trong bài tập tính lương, làm thế nào để tính lương cho nhân viên khi có giờ làm vượt chuẩn? Giải thích cách áp dụng các toán tử điều kiện và phép tính toán.

**Trả lời:**
- **Tính lương với giờ làm vượt chuẩn:**
  - Xác định số giờ tiêu chuẩn và mức lương cho giờ tiêu chuẩn.
  - Xác định số giờ làm vượt chuẩn (giờ làm thực tế trừ giờ tiêu chuẩn, nếu dương).
  - Áp dụng hệ số lương cho giờ vượt chuẩn (thường là 1.5 hoặc 2.0 lần).
  - Tính tổng lương = lương giờ tiêu chuẩn + lương giờ vượt chuẩn.

- **Ví dụ từ code:**
  ```python
  soluongiolam = float(input("Nhập số lượng giờ làm: "))
  luonggio = float(input("Nhập thù lao mỗi giờ làm tiêu chuẩn: "))
  giotieuchuan = 44
  
  # Sử dụng hàm max để đảm bảo giờ vượt chuẩn không âm
  giovuotchuan = max(soluongiolam - giotieuchuan, 0)
  
  # Tính lương: giờ tiêu chuẩn * lương giờ + giờ vượt chuẩn * lương giờ * 1.5
  thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
  
  print("Thu nhập của bạn là: ", thuclinh)
  ```

- **Áp dụng toán tử điều kiện:**
  - Cách khác sử dụng if-else:
  ```python
  if soluongiolam <= giotieuchuan:
      thuclinh = soluongiolam * luonggio
  else:
      thuclinh = giotieuchuan * luonggio + (soluongiolam - giotieuchuan) * luonggio * 1.5
  ```

#### Q4: Có những cách nào để định dạng output của hàm print() để hiển thị số thực với số chữ số thập phân xác định?

**Trả lời:**
- **Phương pháp 1: Sử dụng String Formatting với %**
  ```python
  pi = 3.14159265359
  print("Giá trị của pi là: %.2f" % pi)  # Hiển thị 2 chữ số thập phân: 3.14
  ```

- **Phương pháp 2: Sử dụng hàm format()**
  ```python
  pi = 3.14159265359
  print("Giá trị của pi là: {}".format(round(pi, 2)))  # 3.14
  print("Giá trị của pi là: {:.2f}".format(pi))  # 3.14
  ```

- **Phương pháp 3: F-strings (từ Python 3.6)**
  ```python
  pi = 3.14159265359
  print(f"Giá trị của pi là: {pi:.2f}")  # 3.14
  ```

- **Phương pháp 4: Hàm round()**
  ```python
  pi = 3.14159265359
  print("Giá trị của pi là:", round(pi, 2))  # 3.14
  ```

- **Lưu ý:**
  - Để hiển thị giá trị tiền tệ, thường dùng dấu phẩy cho hàng nghìn:
  ```python
  amount = 1234567.89
  print(f"Số tiền: {amount:,.2f} VND")  # 1,234,567.89 VND
  ``` 

## Lab 2: Caesar Cipher and Web Applications

### Caesar Cipher

#### Q5: Giải thích thuật toán mã hóa Caesar. Tại sao độ dài của bảng chữ cái (alphabet) lại quan trọng trong quá trình mã hóa và giải mã?

**Trả lời:**
- **Nguyên lý của mã hóa Caesar:**
  - Là một loại mã thay thế, trong đó mỗi ký tự trong văn bản gốc được thay thế bằng một ký tự khác, được xác định bằng cách dịch chuyển một số vị trí cố định trong bảng chữ cái.
  - Mỗi chữ cái được thay thế bằng chữ cái đứng cách nó một khoảng bằng giá trị khóa K trong bảng chữ cái.
  - Ví dụ: Với khóa K=3, 'A' sẽ được mã hóa thành 'D', 'B' thành 'E', v.v.

- **Tầm quan trọng của độ dài bảng chữ cái:**
  - **Ảnh hưởng đến phép toán modulo:** Khi dịch chuyển vượt quá độ dài của bảng chữ cái, ta cần quay lại từ đầu bảng. Phép toán modulo (%) được dùng để đảm bảo điều này:
    ```python
    encrypted_index = (original_index + key) % len(alphabet)
    ```
  - **Ảnh hưởng đến không gian khóa:** Độ dài bảng chữ cái quyết định số lượng khóa có thể có. Với bảng chữ cái 26 ký tự tiếng Anh, chỉ có 25 khóa có ý nghĩa (không tính khóa K=0).
  - **Ảnh hưởng đến tính bảo mật:** Bảng chữ cái ngắn dễ bị tấn công bằng phương pháp thử hết các khóa (brute force).

- **Ví dụ từ code:**
  ```python
  def encrypt_text(self, text: str, key: int) -> str:
      alphabet_len = len(self.alphabet)
      text = text.upper()
      encrypted_text = []
      for letter in text:
          if letter in self.alphabet:
              letter_index = self.alphabet.index(letter)
              output_index = (letter_index + key) % alphabet_len
              output_letter = self.alphabet[output_index]
              encrypted_text.append(output_letter)
          else:
              encrypted_text.append(letter)  # Giữ nguyên các ký tự không thuộc bảng chữ cái
      return "".join(encrypted_text)
  ```

#### Q6: Phân tích các điểm yếu bảo mật của mã Caesar. Làm thế nào một kẻ tấn công có thể phá vỡ mã này mà không cần biết khóa?

**Trả lời:**
- **Điểm yếu của mã Caesar:**
  - **Không gian khóa nhỏ:** Với bảng chữ cái 26 ký tự, chỉ có 25 khóa khác nhau.
  - **Bảo toàn tần suất:** Mã không thay đổi tần suất xuất hiện của các ký tự, nên có thể bị tấn công bằng phân tích tần suất.
  - **Đơn ánh xạ:** Mỗi ký tự luôn được mã hóa thành cùng một ký tự, khiến mã dễ bị phá.

- **Phương pháp tấn công không cần biết khóa:**
  1. **Tấn công vét cạn (Brute Force):** 
     - Do không gian khóa nhỏ, kẻ tấn công có thể thử tất cả 25 khóa có thể và chọn kết quả có ý nghĩa.
     - Ví dụ:
     ```python
     def brute_force_attack(ciphertext, alphabet):
         for key in range(1, len(alphabet)):
             plaintext = ""
             for char in ciphertext:
                 if char in alphabet:
                     idx = alphabet.index(char)
                     plaintext += alphabet[(idx - key) % len(alphabet)]
                 else:
                     plaintext += char
             print(f"Key {key}: {plaintext}")
     ```

  2. **Phân tích tần suất:** 
     - Dựa trên việc các chữ cái trong ngôn ngữ tự nhiên có tần suất xuất hiện khác nhau.
     - Ví dụ, trong tiếng Anh, 'E' là chữ cái phổ biến nhất, tiếp theo là 'T', 'A', 'O'...
     - Kẻ tấn công có thể đếm tần suất xuất hiện của từng ký tự trong văn bản đã mã hóa, so sánh với tần suất chuẩn của ngôn ngữ để tìm ra khóa.
     ```python
     def frequency_analysis(ciphertext):
         # Đếm tần suất xuất hiện của các ký tự
         freq = {}
         for char in ciphertext.upper():
             if char.isalpha():
                 freq[char] = freq.get(char, 0) + 1
         
         # Sắp xếp theo tần suất giảm dần
         sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
         
         # Giả sử ký tự phổ biến nhất là 'E' đã bị mã hóa
         most_common = sorted_freq[0][0]
         key = (ord(most_common) - ord('E')) % 26
         
         return key
     ```

  3. **Tấn công dựa trên từ khóa đã biết:**
     - Nếu kẻ tấn công có thể đoán được một phần của nội dung gốc (như "Hello" hoặc "The"), họ có thể dễ dàng tìm ra khóa.
     ```python
     def known_plaintext_attack(ciphertext, known_word):
         for i in range(len(ciphertext) - len(known_word) + 1):
             # Thử giả định rằng đoạn ciphertext ở vị trí i là known_word đã bị mã hóa
             segment = ciphertext[i:i+len(known_word)]
             potential_keys = []
             
             for j in range(len(known_word)):
                 if segment[j].isalpha() and known_word[j].isalpha():
                     key = (ord(segment[j]) - ord(known_word[j].upper())) % 26
                     potential_keys.append(key)
             
             # Nếu tất cả ký tự trong đoạn đều cho cùng một khóa
             if len(set(potential_keys)) == 1:
                 return potential_keys[0]
     ```

### Web Applications

#### Q7: Mô tả luồng hoạt động của ứng dụng web trong Lab 2, từ khi người dùng nhập văn bản cần mã hóa đến khi hiển thị kết quả.

**Trả lời:**
- **Luồng hoạt động của ứng dụng web mã hóa Caesar:**

  1. **Frontend (Giao diện người dùng):**
     - Người dùng mở trang web và nhìn thấy form với các trường để nhập văn bản và khóa mã hóa.
     - Người dùng nhập văn bản cần mã hóa, chọn khóa, và phương thức (mã hóa hoặc giải mã).
     - Khi người dùng nhấn nút "Submit", dữ liệu được gửi đến server thông qua một HTTP POST request.

  2. **Backend (Xử lý dữ liệu):**
     - Server nhận request từ client và trích xuất dữ liệu (văn bản, khóa, phương thức).
     - Flask routing định tuyến request đến hàm xử lý phù hợp.
     - Server gọi đến module mã hóa Caesar để thực hiện mã hóa hoặc giải mã văn bản với khóa đã cho.
     - Kết quả được đóng gói trong một response và gửi trả lại cho client.

  3. **Frontend (Hiển thị kết quả):**
     - Client nhận response từ server và hiển thị kết quả mã hóa/giải mã cho người dùng.
     - Người dùng có thể tiếp tục với văn bản khác hoặc sử dụng kết quả đã có.

- **Ví dụ chi tiết từ code:**
   ```python
   # Frontend (HTML template):
   '''
   <form method="POST" action="/encrypt">
       <input type="text" name="plaintext" placeholder="Nhập văn bản cần mã hóa">
       <input type="number" name="key" placeholder="Nhập khóa">
       <select name="method">
           <option value="encrypt">Mã hóa</option>
           <option value="decrypt">Giải mã</option>
       </select>
       <button type="submit">Submit</button>
   </form>
   <div id="result">
       {% if result %}
           <p>Kết quả: {{ result }}</p>
       {% endif %}
   </div>
   '''
   
   # Backend (Flask route):
   @app.route('/encrypt', methods=['GET', 'POST'])
   def encrypt_page():
       result = None
       if request.method == 'POST':
           text = request.form['plaintext']
           key = int(request.form['key'])
           method = request.form['method']
           
           cipher = CaesarCipher()
           if method == 'encrypt':
               result = cipher.encrypt_text(text, key)
           else:
               result = cipher.decrypt_text(text, key)
               
       return render_template('encrypt.html', result=result)
   ```

#### Q8: Flask được sử dụng như thế nào trong ứng dụng? Giải thích cách thức API hoạt động và cách frontend tương tác với backend.

**Trả lời:**
- **Flask trong ứng dụng:**
  - Flask là một web framework nhẹ cho Python, được sử dụng để xây dựng cả UI và API endpoints.
  - Trong Lab 2, Flask được sử dụng để:
    - Định nghĩa các routes (URLs) mà ứng dụng sẽ phản hồi.
    - Render templates HTML để hiển thị UI.
    - Xử lý các requests từ người dùng và trả về responses.
    - Xây dựng REST API để tương tác với client thông qua JSON.

- **Cấu trúc ứng dụng Flask:**
  ```python
  from flask import Flask, render_template, request, jsonify
  
  app = Flask(__name__)
  
  # Route cho trang chủ
  @app.route('/')
  def home():
      return render_template('index.html')
  
  # Route cho trang mã hóa với UI
  @app.route('/encrypt', methods=['GET', 'POST'])
  def encrypt_page():
      # Xử lý dữ liệu form nếu là POST request
      if request.method == 'POST':
          # Logic xử lý...
          return render_template('encrypt.html', result=result)
      return render_template('encrypt.html')
  ```

- **API Endpoints:**
  - API endpoints được định nghĩa để cho phép tương tác với ứng dụng thông qua HTTP requests.
  - Các endpoints thường trả về dữ liệu dạng JSON thay vì HTML.
  
  ```python
  # API endpoint cho mã hóa
  @app.route('/api/caesar/encrypt', methods=['POST'])
  def api_encrypt():
      data = request.get_json()
      text = data.get('text', '')
      key = data.get('key', 0)
      
      cipher = CaesarCipher()
      encrypted_text = cipher.encrypt_text(text, key)
      
      return jsonify({
          'original_text': text,
          'encrypted_text': encrypted_text,
          'key': key
      })
  ```

- **Tương tác Frontend-Backend:**
  1. **Tương tác qua Form HTML:**
     - Frontend sử dụng HTML form để gửi dữ liệu đến backend.
     - Khi submit form, dữ liệu được gửi đi trong HTTP request với method POST.
     - Backend xử lý dữ liệu và render lại template với kết quả.
     
     ```html
     <form method="POST" action="/encrypt">
         <!-- Form fields -->
         <button type="submit">Submit</button>
     </form>
     ```

  2. **Tương tác qua JavaScript/AJAX:**
     - Frontend có thể sử dụng JavaScript để gửi AJAX requests đến API endpoints.
     - Dữ liệu thường được gửi dưới dạng JSON.
     - Backend xử lý và trả về response cũng dưới dạng JSON.
     - Frontend cập nhật UI dựa trên dữ liệu nhận được mà không cần tải lại trang.
     
     ```javascript
     // Frontend JavaScript
     fetch('/api/caesar/encrypt', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json',
         },
         body: JSON.stringify({
             text: 'Hello World',
             key: 3
         })
     })
     .then(response => response.json())
     .then(data => {
         document.getElementById('result').textContent = data.encrypted_text;
     });
     ```

- **Lợi ích của kiến trúc này:**
  - **Phân tách rõ ràng:** UI và logic xử lý được tách riêng.
  - **Tái sử dụng:** API có thể được sử dụng bởi nhiều clients khác nhau (web, mobile, desktop).
  - **Khả năng mở rộng:** Dễ dàng thêm các tính năng mới mà không ảnh hưởng đến các phần khác.
  - **User Experience:** AJAX cho phép tương tác không đồng bộ, cải thiện trải nghiệm người dùng. 

## Lab 3: Các Thuật Toán Mã Hóa Khóa Công Khai

### RSA Cipher

#### Q9: Trình bày nguyên lý hoạt động của thuật toán RSA. Tại sao cặp khóa công khai và khóa riêng tư lại đảm bảo tính bảo mật?

**Trả lời:**
- **Nguyên lý hoạt động của RSA:**
  1. **Tạo khóa:**
     - Chọn hai số nguyên tố lớn, p và q.
     - Tính n = p × q, đây là modulus cho cả khóa công khai và riêng tư.
     - Tính φ(n) = (p-1) × (q-1), hàm Euler's totient.
     - Chọn một số e (mũ mã hóa) sao cho 1 < e < φ(n) và gcd(e, φ(n)) = 1 (e và φ(n) là số nguyên tố cùng nhau).
     - Tính d (mũ giải mã) sao cho d × e ≡ 1 (mod φ(n)).
     - Khóa công khai là (n, e), khóa riêng tư là (n, d).

  2. **Mã hóa:**
     - Nếu m là thông điệp (dạng số) cần mã hóa, thì ciphertext c được tính:
     - c = m^e mod n

  3. **Giải mã:**
     - Để giải mã, người nhận tính:
     - m = c^d mod n

- **Tại sao RSA an toàn:**
  - **Độ phức tạp của việc phân tích số nguyên:** An ninh của RSA dựa trên độ khó của việc phân tích một số lớn n thành các thừa số nguyên tố p và q. Với các khóa đủ lớn (thường là 2048-bit hoặc 4096-bit), việc này rất khó khăn với sức mạnh tính toán hiện tại.
  
  - **Mối quan hệ giữa khóa công khai và riêng tư:** Để tìm được khóa riêng tư d từ khóa công khai (e, n), kẻ tấn công cần biết giá trị của φ(n), mà để tính được φ(n) cần biết p và q - tức là cần phân tích n.
  
  - **Hàm một chiều với cửa hậu (Trapdoor one-way function):** Mã hóa RSA là hàm một chiều với cửa hậu, nghĩa là:
    - Dễ dàng tính c = m^e mod n, nhưng rất khó khăn để tìm m từ c mà không biết d.
    - Chỉ người biết "cửa hậu" (trapdoor) là d mới có thể dễ dàng giải mã.

  - **Không thể dẫn xuất khóa riêng tư từ khóa công khai:** Kẻ tấn công có thể biết (n, e) nhưng không thể tính d mà không phân tích được n.

- **Ví dụ áp dụng trong code:**
  ```python
  def generate_key_pair():
      # Tạo hai số nguyên tố ngẫu nhiên p và q
      p = generate_prime(bit_length=1024)
      q = generate_prime(bit_length=1024)
      
      # Tính modulus n
      n = p * q
      
      # Tính phi(n)
      phi = (p - 1) * (q - 1)
      
      # Chọn e: thường là 65537
      e = 65537
      
      # Tính d: inverse modular của e mod phi
      d = modinv(e, phi)
      
      # Trả về cặp khóa
      return {
          'public': {'n': n, 'e': e},
          'private': {'n': n, 'd': d}
      }
  
  def encrypt(message, public_key):
      n, e = public_key['n'], public_key['e']
      # Chuyển đổi message thành số
      m = int.from_bytes(message.encode(), 'big')
      # Mã hóa: c = m^e mod n
      c = pow(m, e, n)
      return c
  
  def decrypt(ciphertext, private_key):
      n, d = private_key['n'], private_key['d']
      # Giải mã: m = c^d mod n
      m = pow(ciphertext, d, n)
      # Chuyển đổi số thành message
      byte_length = (m.bit_length() + 7) // 8
      return m.to_bytes(byte_length, 'big').decode()
  ```

#### Q10: Trong mã nguồn rsa_cipher.py, giải thích quá trình ký (sign) và xác thực (verify) một thông điệp. Tại sao chúng ta cần hai quy trình này?

**Trả lời:**
- **Quá trình ký (Sign) thông điệp:**
  1. **Tính giá trị hash của thông điệp:** Sử dụng một hàm băm mật mã học (như SHA-256) để tạo ra một giá trị hash cố định độ dài cho thông điệp.
  2. **Ký giá trị hash:** Sử dụng khóa riêng tư để "mã hóa" giá trị hash, tạo ra chữ ký số.
  3. **Đính kèm chữ ký vào thông điệp gốc:** Chữ ký và thông điệp sẽ được gửi cùng nhau.

  ```python
  def sign_message(message, private_key):
      # Tính giá trị hash của thông điệp
      h = hashlib.sha256(message.encode()).digest()
      # Chuyển đổi hash thành số nguyên
      hash_int = int.from_bytes(h, 'big')
      # Ký giá trị hash bằng khóa riêng tư: s = h^d mod n
      n, d = private_key['n'], private_key['d']
      signature = pow(hash_int, d, n)
      return signature
  ```

- **Quá trình xác thực (Verify) thông điệp:**
  1. **Tính giá trị hash của thông điệp nhận được:** Người nhận tính lại giá trị hash của thông điệp.
  2. **Giải mã chữ ký:** Sử dụng khóa công khai của người gửi để "giải mã" chữ ký, thu được giá trị hash ban đầu.
  3. **So sánh giá trị hash:** So sánh giá trị hash được tính từ thông điệp với giá trị hash được giải mã từ chữ ký. Nếu khớp nhau, thông điệp được xác thực.

  ```python
  def verify_signature(message, signature, public_key):
      # Tính lại giá trị hash của thông điệp
      h = hashlib.sha256(message.encode()).digest()
      hash_int = int.from_bytes(h, 'big')
      
      # Giải mã chữ ký bằng khóa công khai: h' = s^e mod n
      n, e = public_key['n'], public_key['e']
      decrypted_hash = pow(signature, e, n)
      
      # So sánh hai giá trị hash
      return hash_int == decrypted_hash
  ```

- **Tại sao cần hai quy trình này:**
  1. **Xác thực người gửi (Authentication):** 
     - Chỉ người sở hữu khóa riêng tư mới có thể tạo ra chữ ký hợp lệ.
     - Người nhận có thể xác minh rằng thông điệp đến từ người gửi đúng, không phải kẻ mạo danh.

  2. **Toàn vẹn dữ liệu (Integrity):** 
     - Nếu thông điệp bị sửa đổi trong quá trình truyền, giá trị hash sẽ thay đổi.
     - Khi so sánh giá trị hash được tính từ thông điệp với giá trị giải mã từ chữ ký, sẽ không khớp nhau.

  3. **Không thể chối bỏ (Non-repudiation):** 
     - Người gửi không thể phủ nhận đã gửi thông điệp, vì chỉ họ mới có thể tạo ra chữ ký hợp lệ bằng khóa riêng tư của mình.

  4. **Phát hiện giả mạo (Tampering detection):** 
     - Bất kỳ thay đổi nào đối với thông điệp đều sẽ khiến quá trình xác thực thất bại.

- **Ví dụ từ ứng dụng thực tế:**
  - Trong các giao dịch ngân hàng, ký số đảm bảo rằng chỉ chủ tài khoản mới có thể ủy quyền giao dịch.
  - Trong email, chữ ký số giúp người nhận biết email đến từ người gửi hợp pháp.
  - Trong phần mềm, chữ ký số đảm bảo rằng phần mềm đã được phát hành bởi nhà phát triển tin cậy.

### ECC (Elliptic Curve Cryptography)

#### Q11: So sánh thuật toán ECC với RSA. Điểm mạnh và điểm yếu của mỗi thuật toán là gì?

**Trả lời:**
- **So sánh ECC và RSA:**

  | Tiêu chí | ECC (Elliptic Curve Cryptography) | RSA |
  |----------|-------------------------------------|-----|
  | **Nguyên lý** | Dựa trên đường cong elliptic trên trường hữu hạn | Dựa trên độ khó của bài toán phân tích số thành thừa số nguyên tố |
  | **Độ dài khóa** | Ngắn hơn (256-bit ECC ≈ 3072-bit RSA về bảo mật) | Dài hơn (thường 2048-4096 bit) |
  | **Hiệu suất** | Nhanh hơn với khóa ngắn hơn | Chậm hơn với khóa dài hơn |
  | **Sử dụng tài nguyên** | Tiêu thụ ít tài nguyên hơn (CPU, bộ nhớ) | Tiêu thụ nhiều tài nguyên hơn |
  | **Độ phức tạp thuật toán** | Phức tạp hơn để hiểu và triển khai đúng | Tương đối đơn giản để hiểu và triển khai |
  | **Tuổi đời/Mức độ kiểm nghiệm** | Mới hơn, ít được kiểm nghiệm hơn | Cũ hơn, được kiểm nghiệm kỹ hơn |
  | **Chống lại máy tính lượng tử** | Bị tấn công bởi thuật toán Shor nhưng yêu cầu máy tính lượng tử lớn hơn | Dễ bị tấn công bởi máy tính lượng tử sử dụng thuật toán Shor |
  | **Tiêu chuẩn và triển khai** | Có nhiều tham số cần chọn cẩn thận, dễ xảy ra lỗi | Tham số ít và rõ ràng hơn |

- **Điểm mạnh của ECC:**
  1. **Hiệu quả về độ dài khóa:**
     - Khóa ECC ngắn hơn nhiều so với RSA cho cùng một mức độ bảo mật.
     - ECC 256-bit tương đương với RSA 3072-bit về khả năng chống phá mã.

  2. **Hiệu suất cao hơn:**
     - Tạo khóa, mã hóa và giải mã nhanh hơn, đặc biệt trên thiết bị có tài nguyên hạn chế.
     - Tiêu thụ ít pin và CPU hơn trên thiết bị di động.

  3. **Lưu trữ và truyền dữ liệu hiệu quả:**
     - Khóa ngắn hơn nghĩa là ít lưu trữ và băng thông mạng.
     - Phù hợp cho IoT và thiết bị nhúng.

  4. **Khả năng chống lại máy tính lượng tử:**
     - Máy tính lượng tử cần lớn hơn để phá vỡ ECC so với RSA cùng kích thước.

- **Điểm yếu của ECC:**
  1. **Độ phức tạp:**
     - Toán học đằng sau ECC phức tạp hơn, khó hiểu hơn.
     - Triển khai đúng rất quan trọng và dễ mắc lỗi.

  2. **Kiểm nghiệm ít hơn:**
     - ECC chưa được nghiên cứu và kiểm nghiệm lâu dài như RSA.
     - Có ít triển khai mã nguồn mở đáng tin cậy.

  3. **Vấn đề bằng sáng chế:**
     - Một số phương pháp triển khai ECC đã từng gặp vấn đề về bằng sáng chế.

  4. **Nhiều tham số để chọn:**
     - Đòi hỏi lựa chọn cẩn thận các tham số đường cong (curve parameters).
     - Một số đường cong đã bị phát hiện có lỗ hổng bảo mật.

- **Điểm mạnh của RSA:**
  1. **Được kiểm nghiệm kỹ:**
     - Đã được sử dụng và phân tích trong hơn 40 năm.
     - Nhiều triển khai đã được kiểm tra kỹ lưỡng.

  2. **Đơn giản để hiểu:**
     - Nguyên lý cơ bản dễ dàng giải thích và hiểu.
     - Dễ triển khai hơn với ít tham số cần chọn.

  3. **Hỗ trợ rộng rãi:**
     - Được hỗ trợ trong hầu hết các thư viện mật mã và sản phẩm.
     - Tiêu chuẩn công nghiệp được chấp nhận rộng rãi.

  4. **Không có vấn đề bằng sáng chế:**
     - Bằng sáng chế của RSA đã hết hạn.

- **Điểm yếu của RSA:**
  1. **Khóa dài:**
     - Cần khóa dài hơn nhiều để đạt được mức độ bảo mật tương đương với ECC.
     - Khóa dài hơn làm chậm các thao tác mã hóa/giải mã.

  2. **Hiệu suất thấp hơn:**
     - Các phép toán RSA đòi hỏi nhiều tài nguyên tính toán hơn.
     - Tiêu thụ nhiều năng lượng hơn trên thiết bị di động và nhúng.

  3. **Dễ bị tấn công bằng máy tính lượng tử:**
     - Thuật toán Shor trên máy tính lượng tử có thể phá vỡ RSA hiệu quả.
     - RSA dễ bị tấn công bởi máy tính lượng tử hơn so với ECC.

  4. **Chi phí truyền tải và lưu trữ cao hơn:**
     - Khóa và chữ ký dài hơn đòi hỏi nhiều băng thông và không gian lưu trữ.

- **Kết luận:**
  - **Lựa chọn phụ thuộc vào bối cảnh:**
     - Đối với các thiết bị hạn chế tài nguyên (IoT, di động): ECC thường là lựa chọn tốt hơn.
     - Đối với hệ thống cần tương thích rộng rãi và đã được kiểm nghiệm: RSA có thể là lựa chọn an toàn hơn.
     - Nhiều hệ thống hiện đại hỗ trợ cả hai để đảm bảo tính linh hoạt và tương thích.

#### Q12: Giải thích cách ứng dụng sử dụng PyQt5 để tạo giao diện người dùng. Những thành phần UI nào được sử dụng và chúng tương tác với API như thế nào?

**Trả lời:**
- **PyQt5 trong ứng dụng mã hóa:**
  - PyQt5 là một bộ công cụ binding Python cho Qt - framework C++ để phát triển giao diện người dùng đồ họa (GUI).
  - Trong Lab 3, PyQt5 được sử dụng để tạo giao diện đồ họa cho các ứng dụng mã hóa RSA và ECC.

- **Các thành phần UI chính được sử dụng:**
  1. **QMainWindow:**
     - Container chính cho tất cả các thành phần UI khác.
     - Cung cấp menu, thanh trạng thái và layout tổng thể.
     ```python
     class MyApp(QMainWindow):
         def __init__(self):
             super().__init__()
             self.ui = Ui_MainWindow()
             self.ui.setupUi(self)
     ```

  2. **QWidget và QLayout:**
     - QWidget là đơn vị cơ bản cho tất cả các phần tử UI.
     - QLayout (QVBoxLayout, QHBoxLayout, QGridLayout) quản lý vị trí và kích thước của các widget.
     ```python
     # Trong file UI được tạo bởi Qt Designer:
     self.centralwidget = QtWidgets.QWidget(MainWindow)
     self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
     ```

  3. **QPushButton:**
     - Nút nhấn để người dùng thực hiện các hành động như mã hóa, giải mã, tạo khóa.
     ```python
     self.ui.btn_gen_keys = QtWidgets.QPushButton("Generate Keys")
     self.ui.btn_encrypt = QtWidgets.QPushButton("Encrypt")
     self.ui.btn_decrypt = QtWidgets.QPushButton("Decrypt")
     ```

  4. **QTextEdit và QLineEdit:**
     - QTextEdit: Cho phép nhập/hiển thị văn bản nhiều dòng (văn bản gốc, văn bản đã mã hóa).
     - QLineEdit: Cho phép nhập một dòng văn bản (khóa, tham số).
     ```python
     self.ui.txt_plain_text = QtWidgets.QTextEdit()
     self.ui.txt_cipher_text = QtWidgets.QTextEdit()
     self.ui.txt_key = QtWidgets.QLineEdit()
     ```

  5. **QLabel:**
     - Hiển thị text tĩnh làm nhãn cho các trường nhập liệu.
     ```python
     self.ui.lbl_plain_text = QtWidgets.QLabel("Plain Text:")
     self.ui.lbl_cipher_text = QtWidgets.QLabel("Cipher Text:")
     ```

  6. **QMessageBox:**
     - Hộp thoại thông báo hiển thị thông tin, cảnh báo hoặc lỗi.
     ```python
     msg = QMessageBox()
     msg.setIcon(QMessageBox.Information)
     msg.setText("Keys generated successfully!")
     msg.exec_()
     ```

  7. **QTabWidget:**
     - Tạo giao diện có nhiều tab để phân tách các chức năng (mã hóa, giải mã, ký, xác thực).
     ```python
     self.ui.tabWidget = QtWidgets.QTabWidget()
     self.ui.tab_encrypt = QtWidgets.QWidget()
     self.ui.tab_sign = QtWidgets.QWidget()
     ```

- **Tương tác giữa UI và API:**
  1. **Event-driven programming:**
     - PyQt5 sử dụng mô hình lập trình hướng sự kiện.
     - Các signal (tín hiệu) được kết nối với slot (hàm xử lý) để phản hồi hành động của người dùng.
     ```python
     # Kết nối sự kiện clicked của nút với hàm xử lý tương ứng
     self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
     self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
     self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
     ```

  2. **Gọi API thông qua HTTP requests:**
     - UI sử dụng thư viện `requests` để gọi đến các API endpoints trên máy chủ.
     - Dữ liệu được đóng gói dưới dạng JSON và gửi đi qua HTTP POST requests.
     ```python
     def call_api_encrypt(self):
         url = "http://127.0.0.1:5000/api/rsa/encrypt"
         payload = {
             "message": self.ui.txt_plain_text.toPlainText(),
             "key_type": "public"
         }
         try:
             response = requests.post(url, json=payload)
             if response.status_code == 200:
                 data = response.json()
                 self.ui.txt_cipher_text.setText(data["encrypted_message"])
                 msg = QMessageBox()
                 msg.setIcon(QMessageBox.Information)
                 msg.setText("Encrypted Successfully")
                 msg.exec_()
             else:
                 print("Error while calling API")
         except requests.exceptions.RequestException as e:
             print("Error: %s" % e)
     ```

  3. **Cập nhật UI với kết quả API:**
     - Sau khi nhận được response từ API, dữ liệu được trích xuất và hiển thị trên UI.
     - Sử dụng các phương thức setText() hoặc setPlainText() để cập nhật nội dung.
     ```python
     # Cập nhật trường văn bản với kết quả từ API
     self.ui.txt_cipher_text.setText(data["encrypted_message"])
     ```

  4. **Xử lý lỗi:**
     - Try-except blocks bắt các lỗi khi gọi API như timeout, connection error.
     - QMessageBox hiển thị thông báo lỗi cho người dùng.
     ```python
     try:
         response = requests.post(url, json=payload)
         # Xử lý response
     except requests.exceptions.RequestException as e:
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Critical)
         msg.setText(f"Error: {str(e)}")
         msg.exec_()
     ```

- **Quy trình tổng thể:**
  1. Người dùng nhập dữ liệu vào các trường trên UI.
  2. Người dùng nhấn nút để thực hiện hành động (ví dụ: mã hóa, giải mã).
  3. Event handler được kích hoạt, thu thập dữ liệu từ UI.
  4. Dữ liệu được đóng gói thành JSON và gửi đến API endpoint thích hợp.
  5. API xử lý yêu cầu và trả về kết quả.
  6. UI nhận kết quả và cập nhật giao diện hiển thị cho người dùng.
  7. Hiển thị thông báo success/error thông qua QMessageBox. 

## Lab 4: Bảo Mật Truyền Thông và Hàm Băm

### Socket Communications and Encryption

#### Q13: Mô tả quá trình thiết lập kết nối bảo mật giữa client và server trong ứng dụng socket. Làm thế nào để trao đổi khóa AES một cách an toàn?

**Trả lời:**
- **Quá trình thiết lập kết nối bảo mật trong ứng dụng socket:**

  1. **Khởi tạo kết nối TCP:**
     - Server tạo socket và lắng nghe trên một cổng (port) cụ thể.
     - Client tạo socket và kết nối đến server.
     ```python
     # Server side
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_socket.bind(('localhost', 12345))
     server_socket.listen(5)
     
     # Client side
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.connect(('localhost', 12345))
     ```

  2. **Tạo và trao đổi khóa RSA:**
     - Cả client và server đều tạo cặp khóa RSA của riêng mình (khóa công khai và khóa riêng tư).
     - Client gửi khóa công khai của mình cho server và server gửi khóa công khai của mình cho client.
     ```python
     # Server side
     server_key = RSA.generate(2048)
     client_socket.send(server_key.publickey().export_key(format="PEM"))
     client_public_key = RSA.import_key(client_socket.recv(2048))
     
     # Client side
     client_key = RSA.generate(2048)
     client_socket.send(client_key.publickey().export_key(format="PEM"))
     server_public_key = RSA.import_key(client_socket.recv(2048))
     ```

  3. **Tạo và trao đổi khóa AES:**
     - Server tạo khóa AES ngẫu nhiên (khóa đối xứng).
     - Server mã hóa khóa AES bằng khóa công khai của client (dùng RSA).
     - Server gửi khóa AES đã mã hóa cho client.
     - Client giải mã khóa AES bằng khóa riêng tư của mình.
     ```python
     # Server side
     aes_key = get_random_bytes(16)  # 128-bit key
     cipher_rsa = PKCS1_OAEP.new(client_public_key)
     encrypted_aes_key = cipher_rsa.encrypt(aes_key)
     client_socket.send(encrypted_aes_key)
     
     # Client side
     encrypted_aes_key = client_socket.recv(2048)
     cipher_rsa = PKCS1_OAEP.new(client_key)
     aes_key = cipher_rsa.decrypt(encrypted_aes_key)
     ```

  4. **Thiết lập truyền thông bảo mật:**
     - Cả client và server bây giờ đều có chung một khóa AES.
     - Tất cả dữ liệu trao đổi tiếp theo giữa client và server sẽ được mã hóa và giải mã bằng khóa AES này.

- **Tại sao phương pháp này an toàn:**
  - **Kết hợp mã hóa bất đối xứng (RSA) và đối xứng (AES):**
    - RSA được sử dụng để trao đổi khóa AES an toàn.
    - AES được sử dụng để mã hóa nội dung truyền thông (vì AES nhanh hơn RSA nhiều).
  
  - **Bảo vệ khóa AES:**
    - Khóa AES không bao giờ được truyền "trần" trên mạng.
    - Nó được mã hóa bằng khóa công khai của người nhận, chỉ người nhận mới có thể giải mã.
  
  - **Khóa riêng tư không bị lộ:**
    - Khóa riêng tư RSA của cả hai bên không bao giờ được chia sẻ hoặc truyền qua mạng.

- **Chi tiết về quá trình mã hóa/giải mã tin nhắn:**
  ```python
  # Hàm mã hóa bằng AES
  def encrypt_message(key, message):
      cipher = AES.new(key, AES.MODE_CBC)
      ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
      return cipher.iv + ciphertext  # Ghép iv và ciphertext
  
  # Hàm giải mã bằng AES
  def decrypt_message(key, encrypted_message):
      iv = encrypted_message[:AES.block_size]  # Lấy iv từ thông điệp
      ciphertext = encrypted_message[AES.block_size:]  # Lấy phần ciphertext
      cipher = AES.new(key, AES.MODE_CBC, iv)
      decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
      return decrypted_message.decode()
  ```

- **Luồng truyền thông sau khi thiết lập:**
  1. Người gửi chuẩn bị tin nhắn văn bản.
  2. Tin nhắn được mã hóa bằng khóa AES chia sẻ.
  3. Tin nhắn đã mã hóa được gửi qua socket.
  4. Người nhận nhận tin nhắn đã mã hóa.
  5. Người nhận giải mã tin nhắn bằng khóa AES chia sẻ.
  6. Người nhận đọc tin nhắn gốc.

#### Q14: Phân tích các bước mã hóa và giải mã tin nhắn trong ứng dụng. Tại sao chúng ta sử dụng cả AES và RSA trong cùng một ứng dụng?

**Trả lời:**
- **Các bước mã hóa tin nhắn:**
  1. **Chuẩn bị tin nhắn:**
     - Chuyển đổi tin nhắn văn bản thành dạng bytes.
     ```python
     message_bytes = message.encode()
     ```

  2. **Padding:**
     - Thêm padding vào tin nhắn để đảm bảo độ dài là bội số của kích thước khối AES (16 bytes).
     ```python
     padded_message = pad(message_bytes, AES.block_size)
     ```

  3. **Khởi tạo vector khởi tạo (IV):**
     - Tạo IV ngẫu nhiên cho mỗi lần mã hóa.
     - IV đảm bảo rằng cùng một tin nhắn sẽ tạo ra ciphertext khác nhau mỗi lần mã hóa.
     ```python
     cipher = AES.new(key, AES.MODE_CBC)  # Tự động tạo IV ngẫu nhiên
     iv = cipher.iv
     ```

  4. **Mã hóa tin nhắn:**
     - Sử dụng khóa AES chia sẻ và IV để mã hóa tin nhắn đã padding.
     ```python
     ciphertext = cipher.encrypt(padded_message)
     ```

  5. **Đóng gói thông điệp:**
     - Ghép IV và ciphertext để tạo thành thông điệp hoàn chỉnh.
     - IV cần được gửi cùng với ciphertext để người nhận có thể giải mã.
     ```python
     encrypted_message = iv + ciphertext
     ```

  6. **Gửi tin nhắn đã mã hóa:**
     ```python
     socket.send(encrypted_message)
     ```

- **Các bước giải mã tin nhắn:**
  1. **Nhận tin nhắn đã mã hóa:**
     ```python
     encrypted_message = socket.recv(1024)
     ```

  2. **Tách IV và ciphertext:**
     - Lấy IV từ đầu thông điệp.
     - Phần còn lại là ciphertext.
     ```python
     iv = encrypted_message[:AES.block_size]
     ciphertext = encrypted_message[AES.block_size:]
     ```

  3. **Khởi tạo đối tượng AES với IV nhận được:**
     ```python
     cipher = AES.new(key, AES.MODE_CBC, iv)
     ```

  4. **Giải mã ciphertext:**
     ```python
     padded_message = cipher.decrypt(ciphertext)
     ```

  5. **Loại bỏ padding:**
     ```python
     message_bytes = unpad(padded_message, AES.block_size)
     ```

  6. **Chuyển đổi bytes thành văn bản:**
     ```python
     original_message = message_bytes.decode()
     ```

- **Tại sao sử dụng cả RSA và AES:**
  
  1. **Kết hợp ưu điểm của cả hai:**
     - **RSA (mã hóa bất đối xứng):**
       - Giải quyết vấn đề trao đổi khóa an toàn.
       - Không cần kênh bảo mật trước để trao đổi khóa.
       - Cung cấp tính xác thực và không thể chối bỏ.
     
     - **AES (mã hóa đối xứng):**
       - Hiệu suất cao hơn RSA rất nhiều (nhanh hơn 100-1000 lần).
       - Phù hợp để mã hóa lượng dữ liệu lớn.
       - Tiêu thụ ít tài nguyên hơn.

  2. **Giới hạn của từng thuật toán:**
     - **RSA chậm và giới hạn kích thước dữ liệu:**
       - RSA có tốc độ mã hóa/giải mã chậm, không phù hợp cho việc mã hóa tin nhắn dài hoặc liên tục.
       - RSA chỉ có thể mã hóa dữ liệu có kích thước nhỏ hơn kích thước khóa (ví dụ: với khóa 2048 bit, chỉ mã hóa được khoảng 245 bytes).
     
     - **AES không giải quyết được vấn đề trao đổi khóa:**
       - AES đòi hỏi cả hai bên phải biết khóa chung.
       - Không có cách nào an toàn để trao đổi khóa AES trên kênh không an toàn mà không sử dụng mã hóa bất đối xứng.

  3. **Phương pháp hybrid kết hợp:**
     - Sử dụng RSA để trao đổi khóa AES an toàn.
     - Sử dụng AES để mã hóa/giải mã nội dung truyền thông.
     - Đây là phương pháp được sử dụng phổ biến trong nhiều giao thức bảo mật như HTTPS/TLS.

  4. **Hiệu quả về mặt tài nguyên:**
     - Chỉ thực hiện một lần mã hóa/giải mã RSA (chậm) để trao đổi khóa AES.
     - Sử dụng nhiều lần mã hóa/giải mã AES (nhanh) cho tất cả giao tiếp sau đó.

- **Ví dụ ứng dụng thực tế:**
  - **HTTPS/TLS:** Dùng RSA/ECC để trao đổi khóa phiên, sau đó dùng AES để mã hóa dữ liệu.
  - **VPN:** Sử dụng mã hóa bất đối xứng để thiết lập kênh bảo mật, sau đó dùng mã hóa đối xứng cho truyền dữ liệu.
  - **PGP/GPG:** Sử dụng RSA để mã hóa khóa phiên, và khóa phiên để mã hóa nội dung email.

### Hash Functions

#### Q15: So sánh các thuật toán hash MD5, SHA-256, SHA-3 và BLAKE2. Ưu và nhược điểm của mỗi thuật toán là gì?

**Trả lời:**
- **So sánh các thuật toán hash:**

  | Thuật toán | Độ dài output | Năm ra đời | Tốc độ | Tính bảo mật | Trạng thái hiện tại |
  |------------|---------------|------------|--------|--------------|---------------------|
  | **MD5**    | 128 bit       | 1992       | Rất nhanh | Không an toàn | Đã bị phá vỡ hoàn toàn |
  | **SHA-256**| 256 bit       | 2001       | Trung bình | An toàn | Được sử dụng rộng rãi |
  | **SHA-3**  | Linh hoạt (thường 224-512 bit) | 2015 | Chậm hơn SHA-2 | Rất an toàn | Tiêu chuẩn mới nhất |
  | **BLAKE2** | Linh hoạt (thường 256-512 bit) | 2012 | Nhanh hơn MD5 | Rất an toàn | Tối ưu cho phần mềm |

- **MD5 (Message Digest Algorithm 5):**
  - **Ưu điểm:**
    - Rất nhanh, hiệu suất cao.
    - Dễ triển khai.
    - Tạo ra fingerprint ngắn (128 bit).
  
  - **Nhược điểm:**
    - Đã bị phá vỡ hoàn toàn: có thể tạo ra collisions.
    - Không an toàn cho bất kỳ ứng dụng bảo mật nào.
    - Chỉ nên dùng cho kiểm tra tính toàn vẹn dữ liệu không liên quan đến bảo mật.

  - **Ví dụ từ code:**
    ```python
    import hashlib
    
    def md5_hash(message):
        md5 = hashlib.md5()
        md5.update(message.encode())
        return md5.hexdigest()
    
    # Ví dụ: md5_hash("Hello World") = "3e25960a79dbc69b674cd4ec67a72c62"
    ```

- **SHA-256 (Secure Hash Algorithm 256-bit):**
  - **Ưu điểm:**
    - An toàn hơn nhiều so với MD5.
    - Được sử dụng rộng rãi và tin cậy trong nhiều ứng dụng.
    - Là một phần của gia đình SHA-2, vẫn được coi là an toàn.
    - Được sử dụng trong Bitcoin và nhiều hệ thống blockchain.
  
  - **Nhược điểm:**
    - Chậm hơn MD5.
    - Thuộc họ SHA-2, có cùng cấu trúc cơ bản với SHA-1 (đã bị phá vỡ).
    - Tiêu tốn nhiều tài nguyên tính toán hơn các thuật toán mới hơn.

  - **Ví dụ từ code:**
    ```python
    import hashlib
    
    def sha256_hash(message):
        sha256 = hashlib.sha256()
        sha256.update(message.encode())
        return sha256.hexdigest()
    
    # Ví dụ: sha256_hash("Hello World") = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    ```

- **SHA-3 (Secure Hash Algorithm 3):**
  - **Ưu điểm:**
    - Kiến trúc hoàn toàn khác với SHA-1 và SHA-2, sử dụng cấu trúc sponge function.
    - Rất an toàn, được thiết kế để chống lại các tấn công lượng tử.
    - Tiêu chuẩn hash mới nhất của NIST (2015).
    - Linh hoạt với nhiều độ dài output.
  
  - **Nhược điểm:**
    - Chậm hơn SHA-2 và BLAKE2 trên phần cứng thông thường.
    - Chưa được sử dụng rộng rãi như SHA-256.
    - Triển khai phức tạp hơn.

  - **Ví dụ từ code:**
    ```python
    import hashlib
    
    def sha3_256_hash(message):
        sha3 = hashlib.sha3_256()
        sha3.update(message.encode())
        return sha3.hexdigest()
    
    # Ví dụ: sha3_256_hash("Hello World")
    ```

- **BLAKE2:**
  - **Ưu điểm:**
    - Rất nhanh, thậm chí nhanh hơn MD5 trên nhiều nền tảng.
    - An toàn như SHA-3.
    - Tối ưu hóa cho phần mềm (không cần phần cứng chuyên dụng).
    - Hỗ trợ song song hóa và đa luồng.
    - Hỗ trợ salt và personalization.
  
  - **Nhược điểm:**
    - Chưa phải là tiêu chuẩn NIST.
    - Ít được sử dụng rộng rãi hơn so với SHA-256.
    - Ít được hỗ trợ trong các thư viện và nền tảng cũ hơn.

  - **Ví dụ từ code:**
    ```python
    import hashlib
    
    def blake2b_hash(message):
        blake2 = hashlib.blake2b()
        blake2.update(message.encode())
        return blake2.hexdigest()
    
    # Ví dụ: blake2b_hash("Hello World")
    ```

- **Khuyến nghị sử dụng:**
  1. **Cho ứng dụng bảo mật mới:** SHA-3 hoặc BLAKE2
  2. **Cho ứng dụng chuẩn và tương thích rộng rãi:** SHA-256
  3. **Cho các ứng dụng cần hiệu suất cực cao và bảo mật tốt:** BLAKE2
  4. **MD5:** Chỉ dùng cho kiểm tra tính toàn vẹn không liên quan đến bảo mật

#### Q16: Tại sao hàm băm lại quan trọng trong bảo mật thông tin? Hãy giải thích một ứng dụng thực tế của hàm băm trong việc lưu trữ mật khẩu.

**Trả lời:**
- **Tầm quan trọng của hàm băm trong bảo mật thông tin:**
  1. **Tính toàn vẹn dữ liệu (Data Integrity):**
     - Hàm băm tạo ra "dấu vân tay" (fingerprint) của dữ liệu.
     - Bất kỳ thay đổi nào trong dữ liệu đều dẫn đến giá trị hash khác biệt.
     - Cho phép phát hiện dữ liệu bị sửa đổi, dù chỉ là thay đổi nhỏ nhất.

  2. **Tính một chiều (One-way Function):**
     - Không thể tính ngược từ giá trị hash để có được dữ liệu gốc.
     - Bảo vệ thông tin nhạy cảm như mật khẩu khi lưu trữ.

  3. **Tính chống va chạm (Collision Resistance):**
     - Rất khó tìm được hai thông điệp khác nhau có cùng giá trị hash.
     - Đảm bảo tính duy nhất của dữ liệu được xác thực.

  4. **Hiệu quả về mặt tính toán:**
     - Tính toán hash nhanh, bất kể kích thước của dữ liệu đầu vào.
     - Giá trị hash có độ dài cố định, bất kể dữ liệu đầu vào dài hay ngắn.

  5. **Xác thực không cần dữ liệu gốc:**
     - Có thể xác thực tính toàn vẹn mà không cần lưu trữ hoặc tiết lộ dữ liệu gốc.

- **Ứng dụng của hàm băm trong việc lưu trữ mật khẩu:**
  1. **Quy trình lưu trữ mật khẩu an toàn:**
     - **Không bao giờ lưu trữ mật khẩu dưới dạng văn bản thô (plain text).**
     - Thay vào đó, lưu trữ giá trị hash của mật khẩu.
     
     ```python
     # Ví dụ: Đăng ký người dùng
     def register_user(username, password):
         # Thêm salt ngẫu nhiên
         salt = os.urandom(16)
         
         # Tính hash của mật khẩu + salt
         password_hash = hashlib.pbkdf2_hmac(
             'sha256',                 # Thuật toán hash
             password.encode('utf-8'), # Mật khẩu dạng bytes
             salt,                     # Salt ngẫu nhiên
             100000                    # Số lần lặp (work factor)
         )
         
         # Lưu username, salt và password_hash vào database
         db.save_user(username, salt, password_hash)
     ```

  2. **Quy trình xác thực mật khẩu:**
     - Khi người dùng đăng nhập, hệ thống tính lại hash của mật khẩu họ cung cấp.
     - So sánh với giá trị hash đã lưu trong cơ sở dữ liệu.
     - Nếu giống nhau, mật khẩu chính xác; nếu khác, mật khẩu sai.
     
     ```python
     # Ví dụ: Xác thực người dùng
     def authenticate_user(username, password):
         # Lấy salt và password_hash từ database
         user = db.get_user(username)
         if user is None:
             return False
             
         salt = user.salt
         stored_password_hash = user.password_hash
         
         # Tính lại hash với mật khẩu người dùng nhập và salt đã lưu
         computed_hash = hashlib.pbkdf2_hmac(
             'sha256',
             password.encode('utf-8'),
             salt,
             100000
         )
         
         # So sánh hash tính được với hash đã lưu
         if computed_hash == stored_password_hash:
             return True  # Đăng nhập thành công
         else:
             return False  # Mật khẩu không đúng
     ```

  3. **Tại sao cách này an toàn:**
     - **Bảo vệ khỏi rò rỉ dữ liệu:** Nếu cơ sở dữ liệu bị xâm phạm, kẻ tấn công chỉ có được giá trị hash, không thể biết mật khẩu gốc.
     - **Tính một chiều:** Không thể tính ngược từ hash để có mật khẩu.
     - **Sử dụng salt:** Salt là giá trị ngẫu nhiên thêm vào mật khẩu trước khi tính hash, giúp:
       - Ngăn chặn tấn công bằng bảng tra cứu (rainbow tables).
       - Đảm bảo rằng hai người dùng với cùng mật khẩu sẽ có hash khác nhau.
     - **Work factor (số lần lặp):** Làm tăng thời gian tính toán hash, khiến tấn công brute-force trở nên khó khăn hơn.

  4. **Thực hành tốt nhất:**
     - Sử dụng thuật toán hash chuyên dụng cho mật khẩu: bcrypt, Argon2, PBKDF2, scrypt.
     - Tránh sử dụng MD5 hoặc SHA-1 đơn thuần cho mật khẩu.
     - Sử dụng salt đủ dài (ít nhất 16 bytes) và duy nhất cho mỗi người dùng.
     - Điều chỉnh work factor để cân bằng giữa bảo mật và hiệu suất.
     
     ```python
     # Ví dụ sử dụng bcrypt (được khuyến nghị hơn)
     import bcrypt
     
     def register_bcrypt(username, password):
         # bcrypt tự động tạo salt và tích hợp nó với hash
         password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
         db.save_user(username, password_hash)
     
     def authenticate_bcrypt(username, password):
         user = db.get_user(username)
         if user is None:
             return False
         
         # bcrypt.checkpw tự động tách salt từ hash để xác thực
         return bcrypt.checkpw(password.encode(), user.password_hash)
     ```

  5. **Lỗi thường gặp khi lưu trữ mật khẩu:**
     - Lưu mật khẩu dưới dạng plain text.
     - Sử dụng mã hóa đối xứng thay vì hàm băm (mã hóa có thể giải mã).
     - Sử dụng hash không có salt.
     - Sử dụng thuật toán hash yếu (MD5, SHA-1).
     - Sử dụng salt không đủ ngẫu nhiên hoặc dùng chung cho nhiều người dùng.

### WebSockets và Diffie-Hellman

#### Q17: Sự khác biệt giữa WebSocket và HTTP thông thường là gì? Tại sao WebSocket lại phù hợp cho ứng dụng chat thời gian thực?

**Trả lời:**
- **So sánh WebSocket và HTTP thông thường:**

  | Tiêu chí | WebSocket | HTTP Thông thường |
  |----------|-----------|-------------------|
  | **Kết nối** | Kết nối liên tục, hai chiều | Kết nối tạm thời, theo yêu cầu |
  | **Mô hình truyền thông** | Full-duplex (đồng thời cả hai chiều) | Half-duplex (một chiều tại mỗi thời điểm) |
  | **Khởi tạo kết nối** | Bắt đầu bằng HTTP, sau đó nâng cấp thành WebSocket | Mỗi yêu cầu tạo kết nối mới |
  | **Overhead** | Ít overhead sau khi kết nối đã thiết lập | Mỗi yêu cầu có HTTP headers tạo overhead lớn |
  | **Phản hồi từ server** | Server có thể chủ động gửi dữ liệu | Client phải luôn yêu cầu dữ liệu từ server |
  | **Định dạng dữ liệu** | Hỗ trợ cả dữ liệu nhị phân và văn bản | Chủ yếu là văn bản, nhị phân cần mã hóa |
  | **Độ trễ** | Thấp, phù hợp cho ứng dụng thời gian thực | Cao hơn do phải thiết lập kết nối mới |
  | **Sử dụng tài nguyên** | Hiệu quả hơn khi có nhiều tương tác | Kém hiệu quả với tương tác thường xuyên |

- **Cách WebSocket hoạt động:**
  1. **Thiết lập kết nối:**
     - Client gửi HTTP request với header đặc biệt để yêu cầu nâng cấp kết nối:
     ```
     GET /chat HTTP/1.1
     Host: server.example.com
     Upgrade: websocket
     Connection: Upgrade
     Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
     Sec-WebSocket-Version: 13
     ```
     
     - Server đồng ý nâng cấp kết nối bằng response:
     ```
     HTTP/1.1 101 Switching Protocols
     Upgrade: websocket
     Connection: Upgrade
     Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
     ```

  2. **Truyền thông hai chiều:**
     - Sau khi thiết lập, cả client và server có thể gửi dữ liệu bất kỳ lúc nào.
     - Dữ liệu được gửi trong các "frames" (khung) có định dạng riêng.
     - Không cần HTTP header cho mỗi tin nhắn, giảm overhead.

  3. **Đóng kết nối:**
     - Cả client hoặc server đều có thể đóng kết nối bằng cách gửi frame đóng.
     - Kết nối TCP bên dưới cũng được đóng.

- **Tại sao WebSocket phù hợp cho ứng dụng chat thời gian thực:**
  1. **Truyền thông hai chiều:**
     - Server có thể chủ động đẩy tin nhắn mới đến tất cả client mà không cần client yêu cầu.
     - Client có thể nhận tin nhắn từ các người dùng khác ngay lập tức.

  2. **Độ trễ thấp:**
     - Không cần thiết lập kết nối mới cho mỗi tin nhắn.
     - Không có overhead của HTTP headers, giảm độ trễ.
     - Phù hợp cho trò chuyện thời gian thực và phản hồi tức thì.

  3. **Hiệu quả về tài nguyên:**
     - Một kết nối WebSocket tiêu tốn ít tài nguyên hơn nhiều kết nối HTTP.
     - Giảm tải cho server khi có nhiều người dùng cùng lúc.

  4. **Không cần polling:**
     - Không cần sử dụng kỹ thuật long polling hoặc short polling để kiểm tra tin nhắn mới.
     - Tiết kiệm băng thông và tài nguyên server.

  5. **Hỗ trợ nhiều loại dữ liệu:**
     - Dễ dàng truyền cả text và binary data (như file, hình ảnh).

- **Ví dụ từ code:**
  ```javascript
  // Client-side JavaScript
  // Tạo kết nối WebSocket
  const socket = new WebSocket('ws://example.com/chat');
  
  // Xử lý các sự kiện
  socket.onopen = function(event) {
      console.log('Connection established');
      // Gửi tin nhắn sau khi kết nối
      socket.send('Hello Server!');
  };
  
  socket.onmessage = function(event) {
      console.log('Message received: ' + event.data);
      // Hiển thị tin nhắn mới trong UI
      displayMessage(event.data);
  };
  
  socket.onclose = function(event) {
      console.log('Connection closed');
  };
  
  // Gửi tin nhắn khi người dùng nhấn nút
  function sendMessage(message) {
      socket.send(message);
  }
  ```

  ```python
  # Server-side Python (với thư viện websockets)
  import asyncio
  import websockets
  
  # Lưu trữ tất cả các kết nối client
  connected_clients = set()
  
  async def chat_server(websocket, path):
      # Thêm client vào danh sách
      connected_clients.add(websocket)
      try:
          async for message in websocket:
              # Khi nhận tin nhắn từ một client, broadcast đến tất cả client khác
              for client in connected_clients:
                  if client != websocket:
                      await client.send(message)
      finally:
          # Khi client ngắt kết nối, xóa khỏi danh sách
          connected_clients.remove(websocket)
  
  # Khởi chạy server
  start_server = websockets.serve(chat_server, "localhost", 8765)
  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()
  ```

#### Q18: Trong môi trường thực tế, làm thế nào để phòng tránh tấn công Man-in-the-Middle khi sử dụng Diffie-Hellman?

**Trả lời:**
- **Điểm yếu của Diffie-Hellman cơ bản:**
  - Diffie-Hellman (DH) là một phương pháp an toàn để hai bên trao đổi khóa mà không cần chia sẻ bí mật trước.
  - Tuy nhiên, DH cơ bản dễ bị tấn công Man-in-the-Middle (MitM) vì nó không xác thực danh tính của các bên tham gia.
  - Trong tấn công MitM, kẻ tấn công đứng giữa hai bên giao tiếp, thiết lập các phiên DH riêng biệt với mỗi bên, có thể đọc và sửa đổi thông tin.

- **Phương pháp phòng tránh tấn công MitM với Diffie-Hellman:**

  1. **Authenticated Diffie-Hellman:**
     - Kết hợp DH với cơ chế xác thực để đảm bảo danh tính các bên.
     - Xác thực có thể thông qua chữ ký số, khóa bí mật được chia sẻ trước, hoặc chứng chỉ số.
     
     ```python
     # Ví dụ: Ký thông số DH bằng RSA trước khi gửi
     def sign_dh_params(dh_public_key, private_key):
         # Tạo chữ ký số cho khóa công khai DH
         signature = private_key.sign(
             dh_public_key.to_bytes(),
             padding.PSS(
                 mgf=padding.MGF1(hashes.SHA256()),
                 salt_length=padding.PSS.MAX_LENGTH
             ),
             hashes.SHA256()
         )
         return signature
     
     # Đối tác xác minh chữ ký trước khi sử dụng tham số
     def verify_dh_params(dh_public_key, signature, partner_public_key):
         try:
             partner_public_key.verify(
                 signature,
                 dh_public_key.to_bytes(),
                 padding.PSS(
                     mgf=padding.MGF1(hashes.SHA256()),
                     salt_length=padding.PSS.MAX_LENGTH
                 ),
                 hashes.SHA256()
             )
             return True  # Chữ ký hợp lệ
         except:
             return False  # Chữ ký không hợp lệ
     ```

  2. **Diffie-Hellman với PKI (Public Key Infrastructure):**
     - Sử dụng chứng chỉ số X.509 để xác thực tham số DH.
     - Dựa vào hệ thống CA (Certificate Authority) để xác minh danh tính.
     - Được sử dụng trong TLS/SSL.
     
     ```python
     # Trong TLS, các tham số DH được bảo vệ bởi chứng chỉ server
     # Ví dụ trừu tượng:
     def tls_handshake(client, server):
         # Server gửi chứng chỉ và tham số DH
         server_cert, dh_params = server.get_certificate_and_dh_params()
         
         # Client xác minh chứng chỉ server với CA
         if client.verify_certificate(server_cert):
             # Sử dụng DH để trao đổi khóa
             client_dh = client.generate_dh_key()
             client.send(client_dh.public_key)
             
             # Tính toán khóa chia sẻ
             shared_secret = client_dh.compute_shared_key(dh_params)
         else:
             # Chứng chỉ không hợp lệ, có thể là tấn công MitM
             client.abort_connection()
     ```

  3. **Certificate Pinning (Gắn chứng chỉ):**
     - Gắn cứng danh tính của đối tác (thông qua chứng chỉ hoặc khóa công khai) vào ứng dụng.
     - Không tin tưởng hệ thống CA mặc định.
     - Thay đổi chứng chỉ server sẽ bị phát hiện.
     
     ```java
     // Ví dụ Certificate Pinning trong Android
     String hostname = "example.com";
     CertificatePinner certificatePinner = new CertificatePinner.Builder()
         .add(hostname, "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
         .build();
     
     OkHttpClient client = new OkHttpClient.Builder()
         .certificatePinner(certificatePinner)
         .build();
     ```

  4. **Out-of-band Verification (Xác minh ngoại tuyến):**
     - Xác minh tham số DH hoặc khóa thông qua một kênh khác.
     - Ví dụ: Xác minh fingerprint qua điện thoại, SMS, hoặc đối chiếu trực tiếp.
     - Signal và các ứng dụng nhắn tin an toàn sử dụng phương pháp này.
     
     ```
     # Ví dụ hiển thị fingerprint của phiên kết nối
     "Mã xác nhận an toàn với Alice: 25 01 79 33 68 97 FB 02"
     
     # Alice cũng xem được mã này và có thể xác nhận qua điện thoại
     "Mã của tôi cũng là 25 01 79 33 68 97 FB 02"
     ```

  5. **Perfect Forward Secrecy (PFS):**
     - Sử dụng cặp khóa DH mới cho mỗi phiên, đảm bảo rằng nếu một khóa bị xâm phạm, các phiên trước đó vẫn an toàn.
     - Kết hợp với xác thực mạnh.
     
     ```python
     # Tạo tham số DH mới cho mỗi phiên
     def establish_session():
         # Tạo khóa DH mới
         dh_params = generate_new_dh_parameters()
         dh_key = generate_dh_keypair(dh_params)
         
         # Ký tham số với khóa xác thực dài hạn
         signature = sign_with_long_term_key(dh_key.public_key)
         
         # Gửi tham số và chữ ký
         send_to_partner(dh_params, dh_key.public_key, signature)
     ```

  6. **ECDHE (Elliptic Curve Diffie-Hellman Ephemeral):**
     - Sử dụng variant của DH dựa trên đường cong elliptic.
     - Cung cấp bảo mật tương đương với DH truyền thống nhưng với khóa ngắn hơn.
     - Thường kết hợp với xác thực RSA hoặc ECDSA.
     - Phổ biến trong các phiên bản hiện đại của TLS.
     
     ```python
     # Sử dụng ECDHE trong TLS
     def tls_ecdhe_handshake():
         # Server chọn đường cong (e.g., P-256) và tạo cặp khóa
         curve = EllipticCurve.P256
         server_key = generate_ecdh_keypair(curve)
         
         # Server ký tham số ECDHE với khóa dài hạn
         server_signature = sign_with_certificate_key(server_key.public_key)
         
         # Client xác minh chữ ký và tạo khóa của riêng mình
         if verify_signature(server_key.public_key, server_signature, server_cert):
             client_key = generate_ecdh_keypair(curve)
             
             # Hai bên tính khóa chung
             shared_secret = compute_ecdh_secret(client_key.private, server_key.public)
     ```

  7. **MITM Detection (Phát hiện tấn công):**
     - Triển khai các cơ chế để phát hiện dấu hiệu của tấn công MitM.
     - Kiểm tra thay đổi bất thường trong chứng chỉ, độ trễ mạng, hoặc địa chỉ IP.
     - Ghi log và cảnh báo khi phát hiện hành vi đáng ngờ.

- **Kết hợp các biện pháp bảo vệ:**
  - Trong thực tế, các hệ thống an toàn sử dụng kết hợp nhiều biện pháp trên.
  - Ví dụ: TLS 1.3 sử dụng ECDHE với Perfect Forward Secrecy, xác thực chứng chỉ X.509, và có thể kết hợp với certificate pinning ở phía client.
  - Signal Protocol sử dụng Triple Diffie-Hellman với xác thực khóa và out-of-band verification.

- **Ứng dụng thực tế:**
  - **HTTPS/TLS:** Sử dụng authenticated DH/ECDHE với PKI.
  - **SSH:** Key fingerprint verification.
  - **Signal, WhatsApp:** Double Ratchet Algorithm với Triple DH và safety numbers verification.
  - **VPN:** Authenticated Key Exchange (AKE) protocols.

## Câu Hỏi Tổng Hợp

#### Q19: Làm thế nào để kết hợp các kỹ thuật mã hóa từ Lab 2, 3, và 4 để tạo một hệ thống truyền tin an toàn toàn diện?

**Trả lời:**
- **Kiến trúc hệ thống truyền tin an toàn toàn diện:**
  
  1. **Xác thực người dùng:**
     - Sử dụng hàm băm (SHA-256/bcrypt) để lưu trữ và xác thực mật khẩu người dùng.
     - Triển khai xác thực hai yếu tố (2FA) sử dụng mã HMAC dựa trên thời gian (TOTP).
     - Lưu trữ dữ liệu xác thực trong cơ sở dữ liệu an toàn.

  2. **Thiết lập kết nối an toàn:**
     - Sử dụng giao thức TLS/SSL với chứng chỉ X.509 để xác thực server.
     - Thiết lập phiên trao đổi khóa Diffie-Hellman dạng ECDHE cho Perfect Forward Secrecy.
     - Xác minh tính toàn vẹn của kết nối bằng certificate pinning hoặc HSTS.

  3. **Bảo vệ dữ liệu trong quá trình truyền:**
     - Sử dụng mã hóa đối xứng AES-256-GCM để bảo vệ dữ liệu phiên.
     - Thực hiện mã hóa từ đầu đến cuối (end-to-end encryption) cho tin nhắn riêng tư.
     - Sử dụng WebSocket cho truyền thông tin thời gian thực với độ trễ thấp.

  4. **Ký và xác thực dữ liệu:**
     - Sử dụng RSA hoặc ECDSA để ký các thông điệp quan trọng.
     - Xác minh chữ ký dùng khóa công khai của người gửi.
     - Tạo mã xác thực thông điệp (HMAC) cho dữ liệu nhỏ cần tính toàn vẹn.

  5. **Bảo vệ dữ liệu tĩnh:**
     - Mã hóa dữ liệu nhạy cảm lưu trữ bằng AES với khóa được bảo vệ bởi mật khẩu người dùng.
     - Tạo hash SHA-256 cho tệp tin để kiểm tra tính toàn vẹn.
     - Triển khai cơ chế xoay khóa định kỳ (key rotation).

  6. **Giải pháp kết hợp:**
     - **Chat bảo mật:** WebSocket + ECDHE + AES + E2EE (tương tự Signal Protocol).
     - **Chia sẻ tệp tin:** RSA để mã hóa khóa AES → AES để mã hóa tệp tin → SHA-256 để xác minh tính toàn vẹn.
     - **API bảo mật:** TLS + JWT (JSON Web Tokens) có chữ ký RSA hoặc HMAC.

- **Luồng hoạt động chi tiết:**
  1. **Đăng ký và xác thực người dùng:**
     ```
     1. Người dùng đăng ký với username/password
     2. Server tạo salt và hash password + salt (bcrypt)
     3. Server tạo cặp khóa RSA cho người dùng
     4. Khóa riêng tư được mã hóa bằng khóa dẫn xuất từ password
     5. Lưu username, password_hash, salt, public_key, encrypted_private_key
     ```

  2. **Đăng nhập và thiết lập phiên:**
     ```
     1. Người dùng cung cấp username/password
     2. Server xác thực bằng cách so sánh password_hash
     3. Nếu thành công, server tạo session_token và session_key ngẫu nhiên
     4. session_token được ký bằng khóa server (JWT)
     5. Client lưu session_token để xác thực các yêu cầu tiếp theo
     ```

  3. **Truyền tin nhắn an toàn giữa hai người dùng:**
     ```
     1. Client A tải khóa công khai của Client B từ server
     2. Client A tạo khóa AES ngẫu nhiên cho tin nhắn
     3. Client A mã hóa tin nhắn bằng khóa AES
     4. Client A mã hóa khóa AES bằng khóa công khai của B
     5. Client A ký gói tin nhắn bằng khóa riêng tư của mình
     6. Gói tin nhắn (encrypted_message + encrypted_key + signature) được gửi qua WebSocket
     7. Client B xác minh chữ ký bằng khóa công khai của A
     8. Client B giải mã khóa AES bằng khóa riêng tư của mình
     9. Client B giải mã tin nhắn bằng khóa AES
     ```

- **Kết hợp các thuật toán từ các Lab:**
  - **Lab 2 (Caesar):** Mặc dù Caesar Cipher không an toàn cho mục đích bảo mật thực tế, nhưng nguyên lý của nó (mã hóa thay thế) đã được mở rộng thành các kỹ thuật phức tạp hơn trong mã hóa hiện đại. Thay vì sử dụng nó trực tiếp, ta sử dụng AES là một hệ thống mã hóa khối hiện đại và mạnh mẽ hơn.
  
  - **Lab 3 (RSA/ECC):** Sử dụng để xác thực và ký số các thông điệp, cũng như để mã hóa an toàn các khóa phiên. ECC có thể được ưu tiên cho các thiết bị di động do hiệu suất cao hơn và khóa ngắn hơn.
  
  - **Lab 4 (Socket Communications):** Socket bảo mật bằng TLS thay vì tự triển khai, kết hợp với WebSocket cho truyền thông thời gian thực. Sử dụng các thuật toán hash mạnh (SHA-256, BLAKE2) để đảm bảo tính toàn vẹn dữ liệu và lưu trữ mật khẩu an toàn.

- **Ưu điểm của giải pháp kết hợp:**
  - **Bảo mật nhiều lớp:** Nhiều cơ chế bảo mật bổ sung cho nhau.
  - **Perfect Forward Secrecy:** Nếu một khóa bị xâm phạm, chỉ ảnh hưởng đến một phiên.
  - **Hiệu suất tối ưu:** Sử dụng mã hóa đối xứng (nhanh) cho dữ liệu lớn và mã hóa bất đối xứng (chậm hơn nhưng an toàn hơn) cho trao đổi khóa.
  - **Xác thực mạnh:** Đảm bảo nguồn gốc và tính toàn vẹn của thông điệp.
  - **Mã hóa từ đầu đến cuối:** Dữ liệu chỉ có thể được đọc bởi người gửi và người nhận dự định.

#### Q20: Phân tích các điểm yếu bảo mật tiềm ẩn trong mã nguồn của các lab. Đề xuất các cải tiến để tăng cường bảo mật.

**Trả lời:**
- **Điểm yếu bảo mật tiềm ẩn và đề xuất cải tiến:**

  1. **Lab 2 (Caesar Cipher):**
     - **Điểm yếu:** Caesar Cipher là một thuật toán mã hóa yếu, dễ dàng bị phá vỡ bằng phân tích tần suất hoặc tấn công vét cạn.
     - **Đề xuất cải tiến:**
       - Thay thế bằng thuật toán mã hóa mạnh hơn như AES cho mục đích bảo mật thực tế.
       - Nếu vẫn giữ Caesar cho mục đích học tập, hãy triển khai thêm Vigenère cipher để tăng độ phức tạp.
       - Thêm cảnh báo rõ ràng trong code và UI về hạn chế bảo mật của thuật toán.

  2. **Lab 3 (RSA/ECC):**
     - **Điểm yếu:**
       - Không có xử lý lỗi đầy đủ khi mã hóa/giải mã.
       - Thiếu padding chuẩn cho RSA (như OAEP), có thể dẫn đến tấn công.
       - Kích thước khóa có thể không đủ lớn cho bảo mật hiện đại.
     - **Đề xuất cải tiến:**
       - Sử dụng PKCS#1 v2.0 OAEP padding cho mã hóa RSA.
       - Tăng kích thước khóa RSA lên ít nhất 2048 bits.
       - Triển khai xử lý lỗi đầy đủ với thông báo lỗi chung, không tiết lộ chi tiết nội bộ.
       - Sử dụng mã hóa dựa trên ECC thay vì RSA khi có thể, đặc biệt trên thiết bị di động.

  3. **Lab 4 (Socket Communications):**
     - **Điểm yếu:**
       - Tự triển khai giao thức bảo mật có thể dẫn đến lỗi bảo mật.
       - Không có xác thực đủ mạnh cho các bên tham gia.
       - Khóa AES được tạo có thể không đủ ngẫu nhiên hoặc an toàn.
     - **Đề xuất cải tiến:**
       - Sử dụng TLS/SSL thay vì tự triển khai giao thức mã hóa.
       - Triển khai xác thực mạnh dựa trên chứng chỉ hoặc định danh phi tập trung.
       - Sử dụng các thư viện mật mã học đã được kiểm chứng thay vì tự viết code mã hóa.
       - Sử dụng CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) cho việc tạo khóa.

  4. **Hash Functions:**
     - **Điểm yếu:**
       - Sử dụng MD5 cho các ví dụ, là thuật toán hash yếu và đã bị phá vỡ.
       - Thiếu salt khi tạo hash cho mật khẩu.
     - **Đề xuất cải tiến:**
       - Sử dụng SHA-256, SHA-3 hoặc BLAKE2 thay thế MD5.
       - Với hash mật khẩu, triển khai bcrypt, Argon2 hoặc PBKDF2 với salt ngẫu nhiên và work factor phù hợp.
       - Thiết lập cơ chế tự động tăng work factor khi sức mạnh tính toán tăng.

  5. **WebSocket:**
     - **Điểm yếu:**
       - Kết nối WebSocket có thể không được bảo mật (ws:// thay vì wss://).
       - Thiếu cơ chế xác thực liên tục cho kết nối WebSocket.
     - **Đề xuất cải tiến:**
       - Luôn sử dụng WebSocket bảo mật (wss://) dựa trên TLS/SSL.
       - Triển khai xác thực token JWT cho kết nối WebSocket ban đầu.
       - Thêm cơ chế heartbeat và kiểm tra định kỳ trạng thái kết nối.

  6. **Vấn đề chung trong tất cả các Lab:**
     - **Điểm yếu:**
       - Hardcoded keys/secrets trong code.
       - Thiếu logging đầy đủ cho các sự kiện bảo mật.
       - Không có cơ chế phát hiện và phản ứng với tấn công.
       - Mã nguồn thiếu chú thích về các cân nhắc bảo mật.
     - **Đề xuất cải tiến:**
       - Sử dụng biến môi trường hoặc file cấu hình an toàn cho secrets.
       - Triển khai logging bảo mật với chi tiết phù hợp (không ghi log dữ liệu nhạy cảm).
       - Thêm cơ chế phát hiện bất thường (anomaly detection) và rate limiting.
       - Chú thích đầy đủ code với các cân nhắc bảo mật và lý do cho các quyết định triển khai.

- **Phương pháp tiếp cận toàn diện:**
  1. **Threat Modeling:**
     - Thực hiện phân tích rủi ro và mô hình hóa mối đe dọa trước khi triển khai.
     - Xác định các tài sản cần bảo vệ, các vector tấn công tiềm năng và biện pháp giảm thiểu.

  2. **Secure Coding Practices:**
     - Tuân thủ các nguyên tắc lập trình an toàn như OWASP Top 10.
     - Sử dụng code review tập trung vào bảo mật và kiểm tra tự động.
     - Cập nhật thường xuyên các thư viện và dependencies.

  3. **Defense in Depth:**
     - Triển khai nhiều lớp bảo vệ thay vì dựa vào một biện pháp duy nhất.
     - Áp dụng nguyên tắc đặc quyền tối thiểu (principle of least privilege).
     - Thiết kế các hệ thống với khả năng fail-secure (khi gặp lỗi, luôn ưu tiên bảo mật).

  4. **Kiểm định thường xuyên:**
     - Thực hiện các bài kiểm tra thâm nhập (penetration testing) định kỳ.
     - Sử dụng các công cụ phân tích mã tĩnh và động.
     - Triển khai chương trình bug bounty nếu có thể.

## Câu Hỏi Bổ Sung về Bảo Mật

#### Q21: Giải thích khái niệm Zero Trust Security Model và ứng dụng của nó trong bảo mật hệ thống thông tin hiện đại?

**Trả lời:**
- **Zero Trust Security Model:**
  - **Định nghĩa:** Mô hình bảo mật dựa trên nguyên tắc "không tin tưởng bất kỳ ai" - dù là bên trong hay bên ngoài mạng tổ chức.
  - **Nguyên tắc cốt lõi:** "Never trust, always verify" (Không bao giờ tin tưởng, luôn xác minh).
  
- **Các thành phần chính:**
  1. **Xác thực liên tục:** Mọi người dùng, thiết bị và phiên đều phải được xác thực liên tục.
  2. **Kiểm soát truy cập dựa trên ngữ cảnh:** Quyết định truy cập dựa trên nhiều yếu tố (định danh, thiết bị, vị trí, hành vi).
  3. **Phân đoạn vi mô (Micro-segmentation):** Chia nhỏ mạng thành các phân đoạn riêng biệt để hạn chế di chuyển ngang.
  4. **Nguyên tắc đặc quyền tối thiểu:** Chỉ cấp quyền tối thiểu cần thiết cho công việc.
  5. **Mã hóa toàn diện:** Mã hóa dữ liệu cả khi lưu trữ và truyền tải.
  6. **Giám sát liên tục:** Phát hiện bất thường và phản ứng tự động.

- **Ứng dụng trong hệ thống thông tin hiện đại:**
  1. **Môi trường đám mây và multi-cloud:** Bảo vệ tài nguyên khi ranh giới mạng truyền thống không còn rõ ràng.
  2. **Làm việc từ xa:** Đảm bảo truy cập an toàn cho người dùng từ mọi vị trí.
  3. **IoT và BYOD:** Quản lý và bảo vệ thiết bị đa dạng kết nối vào mạng.
  4. **Microservices và Containers:** Bảo vệ các thành phần ứng dụng riêng biệt.
  5. **DevSecOps:** Tích hợp bảo mật vào vòng đời phát triển phần mềm.

- **Lợi ích:**
  - Giảm thiểu bề mặt tấn công
  - Hạn chế khả năng di chuyển ngang của kẻ tấn công
  - Phát hiện vi phạm nhanh hơn
  - Cải thiện khả năng kiểm soát truy cập
  - Phù hợp với xu hướng BYOD, làm việc từ xa và đám mây

- **Triển khai trong thực tế:**
  ```
  1. Xác định tài nguyên quan trọng cần bảo vệ
  2. Triển khai xác thực mạnh (MFA)
  3. Áp dụng kiểm soát truy cập dựa trên vai trò và ngữ cảnh
  4. Thiết lập phân đoạn mạng
  5. Triển khai mã hóa toàn diện
  6. Xây dựng hệ thống giám sát và phản ứng
  7. Liên tục đánh giá và cải tiến
  ```

- **Ví dụ triển khai:**
  - **Bảo mật API:** API Gateway với JWT và OAuth kết hợp phân tích hành vi
  - **Ứng dụng web:** Sử dụng token ngắn hạn, xác thực liên tục, và kiểm soát phiên
  - **Mạng doanh nghiệp:** Sử dụng ZTNA (Zero Trust Network Access) thay thế VPN truyền thống