
## 🔐 ImageCrypto – Image Encryption & Decryption Tool

A simple Flask web app for encrypting and decrypting images using pixel manipulation (XOR) with a password key.

## 🚀 Features
- Encrypt any image (`.jpg`, `.jpeg`, `.png`, `.gif`) using a password/key  
- Decrypt previously encrypted images with the same password  
- Responsive UI with Bootstrap 5  
- Download encrypted/decrypted images

## 🛠️ How It Works
- Uses XOR logic to modify image pixels based on your password
- The same password is needed to decrypt the image

## 📁 Project Structure
```
ImageCrypto/
│
├── app.py                 # Main Flask server
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── style.css          # Custom styles (optional)
├── uploads/               # Uploaded original images
├── processed/             # Encrypted/Decrypted output
└── README.md              # This file
```

## 💻 Run Locally
```bash
pip install flask pillow numpy
python app.py
```
Visit: http://localhost:5000
