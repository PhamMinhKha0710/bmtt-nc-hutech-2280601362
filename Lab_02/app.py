from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()  # Create instance

# Trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# Trang Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

# Xử lý mã hóa
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    caesar = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)  # Use instance method
    return render_template("caesar.html", 
                         input_text=text,
                         key=key,
                         result=encrypted_text,
                         operation="encrypt")

# Xử lý giải mã
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    caesar = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)  # Use instance method
    return render_template("caesar.html",
                         input_text=text,
                         key=key,
                         result=decrypted_text,
                         operation="decrypt")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
