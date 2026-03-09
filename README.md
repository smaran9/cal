# 🔢 Decimal ↔ Binary Calculator Web App

A beautiful, interactive calculator app for converting between decimal and binary number systems, running on localhost with a modern web UI.

## 📋 Features

✨ **Beautiful Web Interface** - Modern gradient design with smooth animations
🔄 **Bidirectional Conversion** - Convert Decimal → Binary and Binary → Decimal  
📋 **Conversion History** - Keep track of recent conversions
📋 **Copy to Clipboard** - Easily copy results
⚡ **Real-time Conversion** - Instant results
📱 **Responsive Design** - Works on desktop and mobile

## 🚀 How to Run

### 1. Install Python
Make sure Python 3.7+ is installed on your system.

### 2. Install Dependencies
Open PowerShell in the project folder and run:
```powershell
pip install -r requirements.txt
```

### 3. Start the Server
```powershell
python app.py
```

You should see:
```
==================================================
🚀 Decimal to Binary Converter Calculator
==================================================
✅ Server running on: http://localhost:5000
⏰ Press Ctrl+C to stop the server
==================================================
```

### 4. Open in Browser
Visit: **http://localhost:5000**

That's it! Your calculator app is now live! 🎉

## 📖 Usage

### Decimal to Binary:
1. Enter a decimal number (e.g., 42)
2. Click "Convert to Binary"
3. See the result and conversion history
4. Click "Copy" to copy the result

### Binary to Decimal:
1. Click the "Binary → Decimal" tab
2. Enter a binary number (e.g., 101010)
3. Click "Convert to Decimal"
4. See the result instantly

## 🛑 Stop the Server
Press **Ctrl+C** in the terminal to stop the server.

## 📁 File Structure
```
dsa.c++/
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Web UI (HTML, CSS, JavaScript)
└── README.md                # This file
```

## 🎨 Features Explained

- **Tab System**: Switch between Decimal→Binary and Binary→Decimal
- **Error Handling**: Validates input before conversion
- **Live History**: Shows recent conversions
- **Copy Button**: Quick copy to clipboard
- **Keyboard Support**: Press Enter to convert
- **Info Box**: Educational content about number systems

## 🔧 Troubleshooting

**Port already in use?**
- Change port in app.py line 47: `app.run(debug=True, port=5001)`

**Flask not installing?**
- Try: `python -m pip install --upgrade pip`
- Then: `pip install -r requirements.txt`

**Can't access localhost:5000?**
- Make sure Python app is running
- Try: `http://127.0.0.1:5000`

---

**Made with ❤️ | Enjoy your calculator!**
