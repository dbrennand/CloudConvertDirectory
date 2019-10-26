# CloudConvertDirectory
A script to convert all files in a given directory from a given file type to another filetype using the CloudConvert API.

## Dependencies

* Written in Python 3.7.

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
black = "*"

[packages]
cloudconvert = "*"
fire = "*"

[requires]
python_version = "3.7"

[pipenv]
allow_prereleases = true
```

## Usage
`python convert.py convertdir {from_extension} {to_extension} /path/to/directory --API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Actual example:

`python convert.py convertdir heic jpg /path/to/directory --API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

## Authors -- Contributors

* **Dextroz** - *Author* - [Dextroz](https://github.com/Dextroz)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
