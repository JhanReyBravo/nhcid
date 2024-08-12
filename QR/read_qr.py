from cryptography.fernet import Fernet
import base64
import hashlib
import cv2
from models import get_connection

def generate_key_from_pin(pin: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(pin.encode()).digest())

def decrypt_content(encrypted_content: str, pin: str) -> str:
    key = generate_key_from_pin(pin)
    f = Fernet(key)
    decrypted_content = f.decrypt(encrypted_content.encode())
    return decrypted_content.decode()

def read_qr_code(file_path: str, pin: str) -> str:
    # Use OpenCV to read the QR code
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    encrypted_content, _, _ = detector.detectAndDecode(img)
    
    if not encrypted_content:
        return "QR code could not be read or is empty"
    
    try:
        decrypted_content = decrypt_content(encrypted_content, pin)
        return decrypted_content
    except Exception as e:
        return f"Decryption failed: {e}"

def get_qr_data_from_db(file_path: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM qrcode_data WHERE file_path = %s', (file_path,))
    qr_data = cursor.fetchone()
    cursor.close()
    conn.close()
    return qr_data

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the file path of the QR code (e.g., 'secure_qr.png'): ")
    pin = input("Enter the PIN to decrypt the content: ")
    result = read_qr_code(file_path, pin)
    print("Decrypted content:", result)

    qr_data = get_qr_data_from_db(file_path)
    if qr_data:
        print(f"Content: {qr_data[1]}")
        print(f"Encrypted Content: {qr_data[2]}")
        print(f"PIN: {qr_data[3]}")
        print(f"File Path: {qr_data[4]}")
    else:
        print("No data found in the database for the given file path.")
