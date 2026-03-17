import io
from fastapi import FastAPI
from fastapi.responses import Response
from PIL import Image

from api import lib

app = FastAPI()


@app.get("/api")
def get_color_image(
    color: str = "#ffffff",
    colors: str = "",
    width: int = 16,
    height: int = 16,
) -> Response:
    color = color.strip().lower()
    if not color:
        color = "#ffffff"

    if not color.startswith("#"):
        color = "#" + color

    color_list: list[str] = []
    if colors:
        color_list = [
            ("#" + c if c[0] != "#" else c).lower()
            for c in colors.split(",")
            if c
        ]

    mode = "RGB"
    if lib.has_alfa_value(color) or any(lib.has_alfa_value(c) for c in color_list):
        mode = "RGBA"

    if color_list:
        image = lib.create_gradient(
            mode, (width, height), [color, *color_list])
    else:
        image = Image.new(mode, (width, height), color)

    image_io = io.BytesIO()
    image.save(image_io, "PNG")
    image_io.seek(0)

    return Response(content=image_io.read(), media_type="image/png")
