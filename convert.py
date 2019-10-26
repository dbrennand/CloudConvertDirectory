try:
    import cloudconvert
    import os
    import fire
    from pathlib import Path
except ImportError as exc:
    raise ImportError(f"Failed to import required modules: {exc}")


class Convert(object):
    def __init__(self, API_KEY: str = None):
        if API_KEY is None:
            raise ValueError("Provide an API key in order to use the API.")
        self.API_KEY = API_KEY

    def cloudconvert_auth(self):
        """
        A helper function which returns a valid cloudconvert Api() object.
        """
        api = cloudconvert.Api(api_key=self.API_KEY)
        return api

    def convertdir(self, FROM: str, TO: str, DIRECTORY: str):
        """
        Searches a directory specified by the user of files matching the "FROM" parameter.
        Converts them using CloudConvert to the specified file type of the users choice "TO" parameter.
        :param FROM: The file type to search for and convert.
        :param TO: The file type to convert the files to.
        :param directory: The full path to the directory to search and convert files.
        """
        user_home = str(Path.home())
        api = self.cloudconvert_auth()
        for _, _, files in os.walk(DIRECTORY):
            for file in files:
                if file.endswith(FROM):
                    print(
                        f"Found file: {os.path.basename(file)} matching extension {FROM}"
                    )
                    print(f"Processing file: {os.path.basename(file)}")
                    basename_without_ext = os.path.splitext(os.path.basename(file))[0]
                    process = api.convert(
                        {
                            "inputformat": f"{FROM}",
                            "outputformat": f"{TO}",
                            "input": "upload",
                            "file": open(f"{DIRECTORY}/{file}", "rb"),
                        }
                    )
                    # wait until conversion finished
                    process.wait()
                    # download output file
                    download_path = f"{user_home}/Downloads/{basename_without_ext}.{TO}"
                    process.download(download_path)
                    print(f"{download_path} downloaded successfully!")


if __name__ == "__main__":
    fire.Fire(Convert)

