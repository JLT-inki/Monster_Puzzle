"""File containing the TextEditor class."""

class TextEditor:
    """
    Class used to read and write from/to TXT files.

    Methods
    -------
    read_file
        Read a TXT file and return its content.
    write_to_file
        Write content to a TXT file.

    """

    def __init__(self) -> None:
        """Construct one TextEditor object."""

    def read_file(self, path_to_file: str) -> list[str]:
        """
        Read a TXT file and return its content.

        Parameters
        ----------
        path_to_file: str
            Path to the file that needs to be read.

        Returns
        -------
        file_content: list[str]
            Content of the file. Each string represents one line of the file.

        """
        # Open the file
        with open(path_to_file, mode="r", encoding="utf8") as input_file:
            # Read the content
            file_content: list[str] = input_file.read().splitlines()

            # Close the file
            input_file.close()

        # Return the content
        return file_content

    def write_to_file(self, content: list[str], path_to_file: str) -> None:
        """
        Write content to a TXT file.

        Parameters
        ----------
        content: list[str]
            Content that shall be written to a TXT file.
            Each string represents one line of the file.
        path_to_file: str
            Path to the file in which the content shall be written.

        """
        with open(path_to_file, mode="w", encoding="utf8") as output_file:
            # Write each line
            for line in content:
                output_file.write(line + "\n")

            # Close the file
            output_file.close()
