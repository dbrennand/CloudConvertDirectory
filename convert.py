import cloudconvert
import os
import fire
import pathlib


def convert(FROM: str, TO: str, DIRECTORY: str, API_KEY: str):
    """Converts all files in a directory to another file format.

    Args:
        FROM (str): The file format to search for and convert.
        TO (str): The file format to convert files to.
        DIRECTORY (str): The absolute path to the directory to search for and convert files.
        API_KEY (str): A CloudConvert API key.
    """
    # Obtain CloudConvert API object
    api = cloudconvert.Api(api_key=API_KEY)
    home_dir = str(pathlib.Path.home())
    # Iterate over every file in the directory and if it matches the FROM file format
    # send it to CloudConvert API for conversion
    for _, _, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith(FROM):
                print(
                    f"Found file: {os.path.basename(file)} matching file format: {FROM}"
                )
                print(f"Uploading file: {os.path.basename(file)} for conversion.")
                basename = os.path.splitext(os.path.basename(file))[0]
                convert = api.convert(
                    {
                        "inputformat": FROM,
                        "outputformat": TO,
                        "input": "upload",
                        "file": open(f"{DIRECTORY}/{file}", "rb"),
                    }
                )
                # Wait for the conversion to finish
                convert.wait()
                # Download converted file
                download_path = f"{home_dir}/CloudConvertDownloads/{basename}.{TO}"
                convert.download(download_path)
                print(f"{download_path} downloaded successfully!")


if __name__ == "__main__":
    fire.Fire(convert)
