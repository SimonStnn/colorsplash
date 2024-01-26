from PIL import Image

def create_gradient(color1: str, color2: str, width: int, height: int):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width) # type: ignore
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base
