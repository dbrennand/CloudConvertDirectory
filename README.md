# CloudConvertHeic

Convert all heic files in a directory to jpg format using the [CloudConvert REST API](https://cloudconvert.com/api/v2#overview).

## Usage

> This project requires [uv](https://docs.astral.sh/uv/).

1. Install the project dependencies:

    ```bash
    uv sync
    ```

2. Run the conversion:

    ```
    uv run main.py --api-key '<API Key>' /path/to/directory
    ```

## Authors

- [Daniel Brennand](https://github.com/dbrennand)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
