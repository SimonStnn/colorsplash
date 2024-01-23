# Colorsplash

Simple way to generate your own color images via HTTP requests

## Features

- [Colorsplash](#colorsplash)
  - [Features](#features)
  - [Color image](#color-image)
    - [Setting a color](#setting-a-color)
    - [Passing an alfa value](#passing-an-alfa-value)
    - [Setting the size of the image](#setting-the-size-of-the-image)
  - [All query parameters](#all-query-parameters)

## Color image

### Setting a color

To set the color of the image you can pass the `&color` query parameter. You pass in a hex color value (e.g. `&color=FF0000`)

```md
![Color](https://colorsplash.vercel.app/api?color=00ee77)
```

> Example: ![Color](https://colorsplash.vercel.app/api?color=00ee77)

### Passing an alfa value

You can also pass in an alfa value with the `&color` query paramter. The image in the response will then have an alfa value.

```md
![Color](https://colorsplash.vercel.app/api?color=00ee7750)
```

> Example: ![Color](https://colorsplash.vercel.app/api?color=00ee7750)

> [!NOTE]\
> If the alfa value is `ff` the image will be a RGB image, not RGBA.

### Setting the size of the image

You can set the size of the image by passing the `&width` and `&height` query parameters.

```md
![Color](https://colorsplash.vercel.app/api?width=50&height=10)
```

> Example: ![Color](https://colorsplash.vercel.app/api?width=50&height=10)

## All query parameters

| Name     | Description                 | Type   | Default  |
| :--      | :---------                  | :--    | :-----   |
| `color`  | Set the color of the image  | string | `FFFFFF` |
| `width`  | Set the width of the image  | int    | 16       |
| `height` | Set the height of the image | int    | 16       |
