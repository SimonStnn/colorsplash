# Colorsplash

## Features

- [Colorsplash](#colorsplash)
  - [Features](#features)
  - [Color image](#color-image)
    - [Setting a color](#setting-a-color)
    - [Setting the size of the image](#setting-the-size-of-the-image)
  - [All query parameters](#all-query-parameters)

## Color image

### Setting a color

To set the color of the image you can pass the `&color` query parameter. You pass in a hex color value (e.g. `&color=FF0000`)

```md
![Color](https://colorsplash.vercel.app/api?color=FF0000)
```

> Example: ![Color](https://colorsplash.vercel.app/api?color=FF0000)

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
