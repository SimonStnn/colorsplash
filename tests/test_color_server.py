import unittest
from io import BytesIO
from PIL import Image
from api.index import app, has_alfa_value


class ColorServerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Disable Flask error catching during tests
        self.app.testing = True  # type: ignore

    def test_get_color_image_default(self):
        response = self.app.get("/api")
        self.assertEqual(response.status_code, 200)
        # Check if the response is a PNG image
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            # Check if the size of the image is 16x16
            self.assertEqual(img.size, (16, 16))
            # Check if the color of the image is white
            white_pixel = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == white_pixel for pixel in pixels))  # type: ignore

    def test_get_color_image_with_color(self):
        response = self.app.get("/api?color=00FF00")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 255, 0)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_width(self):
        response = self.app.get("/api?width=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            self.assertEqual(img.size, (32, 16))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_height(self):
        response = self.app.get("/api?height=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            self.assertEqual(img.size, (16, 32))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_width_and_height(self):
        response = self.app.get("/api?width=32&height=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            self.assertEqual(img.size, (32, 32))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_alfa(self):
        response = self.app.get("/api?color=00000000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/png")

        with Image.open(BytesIO(response.data)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 0, 0, 0)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_has_alfa_value(self):
        self.assertTrue(has_alfa_value("#00000000"))
        self.assertTrue(has_alfa_value("#00000001"))
        self.assertTrue(has_alfa_value("#00000056"))
        self.assertTrue(has_alfa_value("#00000FE"))
        self.assertTrue(has_alfa_value("#00000fe"))
        self.assertFalse(has_alfa_value("#000000"))
        self.assertFalse(has_alfa_value("#0000ff"))
        self.assertFalse(has_alfa_value("#000000ff"))
        self.assertFalse(has_alfa_value("#000000FF"))


if __name__ == "__main__":
    unittest.main()
