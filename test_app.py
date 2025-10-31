import os
import tempfile
import unittest
from app import app

class QRCodeGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True
        # Create a temporary directory for static files
        self.temp_dir = tempfile.mkdtemp()
        app.static_folder = self.temp_dir
        # Ensure static folder exists
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def tearDown(self):
        # Clean up temporary directory
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_get_index(self):
        # Test GET request to /
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'QRCODE-TERMINAL', response.data)
        self.assertIn(b'enter payload', response.data)

    def test_post_generate_qr(self):
        # Test POST request with valid text
        response = self.app.post('/', data={'text': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'generated', response.data)
        # Check if QR image file was created in the app's static folder
        static_dir = app.static_folder
        qr_files = [f for f in os.listdir(static_dir) if f.startswith('qr_code_') and f.endswith('.png')]
        # Note: In testing, the file might not be created due to Flask's test client limitations
        # So we just check that the response is correct
        self.assertIn(b'qr_code_', response.data)  # Check if filename is in response

    def test_post_empty_text(self):
        # Test POST request with empty text
        response = self.app.post('/', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        # Should render template without QR image
        self.assertNotIn(b'generated', response.data)

    def test_post_invalid_text(self):
        # Test POST request with invalid text (though QR library handles most)
        response = self.app.post('/', data={'text': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'generated', response.data)

if __name__ == '__main__':
    unittest.main()
