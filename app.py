from flask import Flask, request, render_template, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img_path = os.path.join('static', 'qr_code.png')
            img.save(img_path)
            return render_template('index.html', qr_image='qr_code.png')
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)

if __name__ == '__main__':
    # Use environment variable for port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)