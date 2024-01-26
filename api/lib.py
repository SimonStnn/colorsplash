from PIL import Image


# Check if a hex color is is transparent
def has_alfa_value(color: str):
    return len(color) > 7 and color[7:].lower() != "ff"


def create_gradient(mode: str, size: tuple[int, int], colors: list[str]):
    width, height = size
    base = Image.new(mode, (width, height), colors[0])
    for i in range(1, len(colors)):
        top = Image.new(mode, (width, height), colors[i])
        mask = Image.new("L", (width, height))
        mask_data = []
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)  # type: ignore
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
    return base
