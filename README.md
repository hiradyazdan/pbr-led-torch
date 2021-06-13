# sr-rendering

## Requirements

- Python 2.7
- RenderMan 23.5

## Usage

### Run

### Command Line Help

```shell
python ./app.py --help
```

#### Output to "rib file" and render

```shell
python ./app.py --rib
prman ./candleholder.rib
```

#### Render to default Framebuffer (it) directly

```shell
python ./app.py
```

### Render to exr

```shell
python ./app.py -o exr
```

#### Note:

***Saving from image tool to jpeg or png requires the `Burn In Mapping On Save`
to be selected from `Catalog` tab, otherwise the saved image will be dark.***