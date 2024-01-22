import io
from flask import Flask, request, send_file
from PIL import Image

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_color_image():
    # Get the color parameter from the request
    color = request.args.get(
        "color", "#FFFFFF"
    )  # Default to white if no color provided
    if color[0] != "#":
        color = "#" + color

    # Get the size parameters from the request
    image_width = int(request.args.get("width", "16"))
    image_height = int(request.args.get("height", "16"))

    # Create a solid color image using Pillow (PIL)
    image = Image.new("RGB", (image_width, image_height), color)

    # Save the image to a BytesIO object
    image_io = io.BytesIO()
    image.save(image_io, "PNG")
    image_io.seek(0)

    # Send the image as a response
    return send_file(image_io, mimetype="image/png")
