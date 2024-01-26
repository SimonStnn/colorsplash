from PIL import Image


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
