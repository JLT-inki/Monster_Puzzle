"""Main file of the project 'Monster Puzzle'."""

import sys

# Import used classes
from classes.piece import Piece
from classes.puzzle import Puzzle
from classes.text_editor import TextEditor

# Constants for the input and output files
INPUT_FOLDER: str = "./../input/"
OUTPUT_FOLDER: str = "./../output/"
FILES: list[str] = [
    "puzzle0.txt", "puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]


def main() -> int:
    """Find a solution for each puzzle and write it into a TXT file."""
    # Initialize the text editor
    text_editor: TextEditor = TextEditor()

    # Go through each puzzle
    for file in FILES:
        # Get the pieces from the file
        file_content: list[str] = text_editor.read_file(INPUT_FOLDER + file)

        # Create the pieces
        pieces: list[Piece] = Piece.create_pieces_from_file(file_content)

        # Initialize the puzzle object
        puzzle: Puzzle = Puzzle(9, pieces)

        # Find a solution for each puzzle
        solution: list[list[Piece]] = puzzle.find_solution(
            0, 0, [[], [], []], puzzle.get_pieces())

        # Get the sides of all the pieces
        solution_sides: list[str] = Piece.get_sides_of_pieces(solution)

        # Write the solution to a TXT file
        text_editor.write_to_file(solution_sides, OUTPUT_FOLDER + file)

    # Return Exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
