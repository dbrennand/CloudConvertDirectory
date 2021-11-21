# CloudConvertDirectory
Convert all files in a directory to another file format using the [CloudConvert API](https://cloudconvert.com/api/v2#overview).

## Dependencies

* Python ^3.7.

```
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.7"
fire = "0.4.0"
cloudconvert = {git = "https://github.com/cloudconvert/cloudconvert-python.git", rev = "v1"}

[tool.poetry.dev-dependencies]
black = "^21.11b1"
```

## Usage
`python convert.py <FROM> <TO> /path/to/directory <API_KEY>`

E.g. `python convert.py heic jpg /path/to/directory <API_KEY>`

## Authors -- Contributors

* **dbrennand** - *Author* - [dbrennand](https://github.com/dbrennand)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
