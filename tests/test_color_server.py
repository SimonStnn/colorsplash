import unittest
from io import BytesIO
from PIL import Image
from fastapi.testclient import TestClient
from api.index import app
from api.lib import has_alfa_value


class ColorServerTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_color_image_default(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            white_pixel = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == white_pixel for pixel in pixels))  # type: ignore

    def test_get_color_image_with_color(self):
        response = self.client.get("/api?color=00FF00")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 255, 0)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_width(self):
        response = self.client.get("/api?width=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (32, 16))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_height(self):
        response = self.client.get("/api?height=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 32))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_width_and_height(self):
        response = self.client.get("/api?width=32&height=32")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (32, 32))
            expected_color = (255, 255, 255)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_alfa(self):
        response = self.client.get("/api?color=00000000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 0, 0, 0)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

        response = self.client.get("/api?color=000000FE")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 0, 0, 254)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

        response = self.client.get("/api?color=000000fd")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 0, 0, 253)
            pixels = list(img.getdata())  # type: ignore
            self.assertTrue(all(pixel == expected_color for pixel in pixels))  # type: ignore

    def test_get_color_image_with_ff_as_alfa(self):
        response = self.client.get("/api?color=000000ff")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "image/png")

        with Image.open(BytesIO(response.content)) as img:
            self.assertEqual(img.size, (16, 16))
            expected_color = (0, 0, 0)
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
