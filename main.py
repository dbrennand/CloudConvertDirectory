import cloudconvert
import argparse
import os
import pathlib


def check_directory(path: str):
    """
    Ensure the directory exists.

    Args:
        path (str): The directory to check exists.

    Returns:
        boolean: True if the directory exists.

    Raises:
        ValueError: If the directory does not exist.
    """
    if not os.path.isdir(path):
        raise ValueError(f"'{path}' is not a valid directory.")
    return path


parser = argparse.ArgumentParser(
    description="Convert all heic files in a directory to jpg format using the CloudConvert REST API."
)
parser.add_argument(
    "directory",
    type=check_directory,
    help="Path to the directory containing the heic files to convert to jpg format.",
)
parser.add_argument("--api-key", type=str, required=True, help="CloudConvert API key.")
args = parser.parse_args()

# Get the user's current home directory and create a subdirectory to hold converted files
convert_directory = pathlib.Path(f"{str(pathlib.Path.home())}/converted")
convert_directory.mkdir(exist_ok=True)

# Initialise the CloudConvert object
api = cloudconvert.configure(api_key=args.api_key)

for root, _, files in os.walk(args.directory):
    for _file in files:
        if _file.endswith("heic"):
            print(
                f"File '{os.path.basename(_file)}' contains matching file extension 'heic'."
            )
            # Get the filename without the extension
            file_basename = os.path.splitext(os.path.basename(_file))[0]
            print(
                f"Creating tasks to convert file '{os.path.basename(_file)}' to 'jpg' format."
            )
            # Create the CloudConvert job
            job = cloudconvert.Job.create(
                payload={
                    "tasks": {
                        "import-1": {"operation": "import/upload"},
                        "convert-1": {
                            "operation": "convert",
                            "input": ["import-1"],
                            "input_format": "heic",
                            "output_format": "jpg",
                            "fit": "max",
                            "strip": False,
                            "quality": 100,
                            "filename": f"{file_basename}.jpg",
                        },
                        "export-1": {
                            "operation": "export/url",
                            "input": ["convert-1"],
                            "inline": False,
                            "archive_multiple_files": False,
                        },
                    },
                    "tag": "jobbuilder",
                }
            )
            # Get the IDs for the various tasks
            import_task_id = job["tasks"][0]["id"]
            convert_task_id = job["tasks"][1]["id"]
            export_task_id = job["tasks"][2]["id"]

            # Get the import task and upload the file to it
            import_task = cloudconvert.Task.find(id=import_task_id)
            import_upload = cloudconvert.Task.upload(
                file_name=os.path.join(root, _file), task=import_task
            )
            # Wait for the convert task to complete
            convert_task = cloudconvert.Task.wait(id=convert_task_id)
            # Wait for the export task to complete
            export_task = cloudconvert.Task.wait(id=export_task_id)
            converted_file = export_task.get("result").get("files")[0]
            cloudconvert.download(
                url=converted_file["url"],
                filename=os.path.join(convert_directory, converted_file["filename"]),
            )
            print(
                f"Successfully converted file '{os.path.basename(_file)}' to '{os.path.join(convert_directory, converted_file['filename'])}'."
            )
        else:
            continue
