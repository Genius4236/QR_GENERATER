# QR Code Generator Web Application

A futuristic web application for generating QR codes from user-inputted text, built with Python Flask and HTML/CSS.

## Features

- **User-Friendly Interface**: Clean, futuristic design with neon colors and animations.
- **Real-Time QR Generation**: Enter text and instantly generate a QR code.
- **Responsive Design**: Works on desktop and mobile devices.
- **Input Validation**: Handles empty inputs gracefully.
- **Image Display**: Generated QR codes are displayed directly on the page.

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3
- **QR Code Library**: qrcode[pil]
- **Styling**: Custom CSS with gradients, animations, and glow effects

## Installation

1. **Clone or Download the Project**:
   - Place the project files in a directory, e.g., `c:/Users/mdkhi/OneDrive/Desktop/QR CODE`.

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   & "C:/Users/mdkhi/OneDrive/Desktop/QR CODE/venv/Scripts/Activate.ps1"

4. **Install Dependencies**:
   ```bash
   pip install flask qrcode[pil]
   ```

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Access the Web App**:
   - Open your browser and go to `http://127.0.0.1:5000`.

3. **Generate QR Code**:
   - Enter text in the input field.
   - Click "Generate QR Code".
   - The QR code will appear below the form.

## Project Structure

```
QR CODE/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML template
├── static/                # Directory for generated QR code images
│   └── qr_code.png        # Generated QR code (created dynamically)
├── venv/                  # Virtual environment (created during setup)
└── README.md              # This file
```

## Contributing

Feel free to fork the project and submit pull requests for improvements.

## License

This project is open-source and available under the MIT License.
