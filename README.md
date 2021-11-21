# CloudConvertDirectory
Convert all files in a directory to another file format using the [CloudConvert API](https://cloudconvert.com/api/v2#overview).

## Dependencies

* Python ^3.7.

```
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.7"
cloudconvert = "2.0.0"
fire = "0.4.0"

[tool.poetry.dev-dependencies]
black = "^21.11b1"
```

## Usage
`python convert.py dir <FROm> <TO> /path/to/directory --API_KEY=<API Key>`

E.g. `python convert.py dir heic jpg /path/to/directory --API_KEY=<API Key>`

## Authors -- Contributors

* **dbrennand** - *Author* - [dbrennand](https://github.com/dbrennand)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
