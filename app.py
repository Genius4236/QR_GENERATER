from flask import Flask, request, render_template, send_file
import qrcode
import os
from datetime import datetime

app = Flask(__name__)

# Ensure static folder exists
@app.before_request
def create_static_folder():
    if not os.path.exists('static'):
        os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        if text:
            try:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(text)
                qr.make(fit=True)

                # Create QR image with cyberpunk colors
                img = qr.make_image(fill_color="#00ff41", back_color="black")
                
                # Generate unique filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f'qr_code_{timestamp}.png'
                
                # Save image
                img_path = os.path.join('static', filename)
                img.save(img_path)
                
                return render_template('index.html', qr_image=filename)
            except Exception as e:
                # Log error and return template without QR
                print(f"Error generating QR code: {str(e)}")
                return render_template('index.html', error="Failed to generate QR code")
    
    return render_template('index.html')

if __name__ == '__main__':
    # Use environment variable for port, default to 5000
    port = int(os.environ.get('PORT', 5000))
    # In development, use debug mode on localhost
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True)
    else:
        # In production, bind to all interfaces
        app.run(host='0.0.0.0', port=port)