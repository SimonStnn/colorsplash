import io
from flask import Flask, request, send_file
from PIL import Image

from api import lib

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def get_color_image():
    # Get the color parameter from the request
    color = request.args.get("color", "#ffffff").lower()
    colors = request.args.get("colors")
    # Default to white if no color provided
    if color[0] != "#":
        color = "#" + color
    if colors:
        colors = [
            "#" + color if color[0] != "#" else color for color in colors.split(",")
        ]
        colors = [color.lower() for color in colors]

    # Get the size parameters from the request
    image_width = int(request.args.get("width", "16"))
    image_height = int(request.args.get("height", "16"))
    size = (image_width, image_height)

    mode = "RGBA" if lib.has_alfa_value(color) else "RGB"

    if colors:
        image = lib.create_gradient(mode, size, [color, *colors])
    else:
        # Create a solid color image using Pillow (PIL)
        image = Image.new(mode, size, color)

    # Save the image to a BytesIO object
    image_io = io.BytesIO()
    image.save(image_io, "PNG")
    image_io.seek(0)

    # Send the image as a response
    return send_file(image_io, mimetype="image/png")
