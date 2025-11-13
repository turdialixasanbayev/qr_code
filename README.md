# 🧾 QR Code Generator

Bu loyiha — oddiy, qulay va foydali **QR kod generator** dasturi bo‘lib, Python yordamida yozilgan. Siz URL, matn yoki boshqa ma’lumotlardan tezda QR kod rasm fayllarini yaratishingiz mumkin.

---

## 🚀 Boshlash

### Talablar
- Python 3.7 yoki undan yuqori
- Quyidagi kutubxonalar kerak bo‘ladi: `qrcode`, `Pillow`

### O‘rnatish
```bash
git clone https://github.com/turdialixasanbayev/qr_code.git
cd qr_code
pip install -r requirements.txt
```

### Ishga tushirish
```bash
python main.py
```

Dastur sizdan kiritiladigan URL yoki matnni so‘raydi:
```bash
Enter the URL: https://example.com
```

Natijada `/home/turdiali/Projects/qr_codes/` papkasida `qrcode_<uuid>.png` nomli fayl hosil bo‘ladi.

---

## 🧩 Foydalanish (modul sifatida)
Agar `main.py` faylini modul sifatida ishlatmoqchi bo‘lsangiz:

```python
from main import generate_qr

generate_qr("https://example.com", "my_qr.png")
```

**Parametrlar:**
- `data` — QR kodga kiritiladigan ma’lumot (matn, URL va h.k.)
- `filename` — saqlanadigan fayl nomi (masalan, `my_qr.png`)

---

## 📁 Loyiha tuzilmasi
```
qr_code/
│
├── main.py              # Asosiy dastur (QR kod generator)
├── requirements.txt     # Kerakli kutubxonalar ro‘yxati
├── README.md            # Loyiha haqida hujjat
├── .gitignore           # Git uchun cheklovlar
└── qr_codes/            # Yaratilgan QR kod fayllari saqlanadigan papka
```

---

## 💡 Misol
```python
import qrcode
import uuid
import os

url = input("Enter the URL: ").strip()
unique_filename = f"qrcode_{uuid.uuid4().hex}.png"
directory = "/home/turdiali/Projects/qr_codes"
file_path = os.path.join(directory, unique_filename)

os.makedirs(directory, exist_ok=True)

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print(f"✅ QR code saved to: {file_path}")
```

---

## 🤝 Hissa qo‘shish
1. Loyiha fork qiling  
2. O‘z filialingizni yarating (`feature/your-feature`)  
3. O‘zgartirishlaringizni commit va push qiling  
4. Pull request yuboring  

Hamma turdagi takliflar (kodni optimallashtirish, yangi imkoniyatlar, dokumentatsiya) mamnuniyat bilan qabul qilinadi.

---

## 📜 Litsenziya
Ushbu loyiha **MIT License** ostida tarqatiladi.  
© 2025 [@turdialixasanbayev](https://github.com/turdialixasanbayev)
