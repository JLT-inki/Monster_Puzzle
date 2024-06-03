"""File containing the Piece class."""

# Import for methods that use Piece as a type hint
from __future__ import annotations

class Piece:
    """
    Class representing one piece of the puzzle.

    Attributes
    ----------
    sides: list[int]
        Sides of the piece.
    is_upside_down: bool
        Indication whether the piece is upside down or not.
        TRUE means that the piece is upside down.
        FALSE means that the piece is not upside down.

    Methods
    -------
    set_pieces
        Set the sides of the piece.
    set_is_upside_down
        Set the indication whether the piece is upside down or not.
    get_pieces
        Return the sides of the piece.
    get_is_upside_down
        Return the indication whether the piece is upside down or not.
    create_pieces_from_file
        Create a list of pieces from the content of a TXT file.
    two_pieces_match
        Check whether two pieces can be placed together with the given sides.
    rotate
        Rotate the piece by 120° to the right.
    flip
        Flip the piece.
    get_sides_of_pieces
        Get the sides of all pieces contained in a two dimensional list.

    """

    def __init__(self, sides: list[int]) -> None:
        """
        Construct on Piece object with the given parameters.

        Parameters
        ----------
        sides: list[int]
            Sides of the piece.

        """
        self.set_sides(sides)

        # Initialize the piece to be NOT upside down
        self.set_is_upside_down(False)

    def set_sides(self, sides: list[int]) -> None:
        """
        Set the sides of the piece.

        Parameters
        ----------
        sides: list[int]
            Sides of the piece.

        """
        self.sides = sides

    def set_is_upside_down(self, is_upside_down: bool) -> None:
        """
        Set the indication whether the piece is upside down or not.

        Parameters
        ----------
        is_upside_down: bool
            Indication whether the piece is upside down or not.

        """
        self.is_upside_down = is_upside_down

    def get_sides(self) -> list[int]:
        """
        Return the sides of the piece.

        Returns
        -------
        sides: list[int]
            Sides of the piece.

        """
        return self.sides

    def get_is_upside_down(self) -> bool:
        """
        Return the indication whether the piece is upside down or not.

        Returns
        -------
        is_upside_down: bool
            Indication whether the piece is upside down or not.

        """
        return self.is_upside_down

    @staticmethod
    def create_pieces_from_file(file_content: list[str]) -> list[Piece]:
        """
        Create a list of pieces from the content of a TXT file.

        Parameters
        ----------
        file_content: list[str]
            Content of a TXT file, containing piece information.
            Each string represents one line of the file.

        Returns
        -------
        piece_list: List[Piece]
            List containing the created pieces.

        """
        # Initialize the return value
        piece_list: list[Piece] = []

        # Ignore the first & second line as they don't contain pieces
        for line in file_content[2:]:
            # Get the values of each line
            values: list[int] = [int(element) for element in line.split()]

            # Create a Piece object with these values and add it to the return value
            piece_list.append(Piece(values))

        return piece_list

    @staticmethod
    def two_pieces_match(piece1: Piece, piece2: Piece, side_piece1: int,
                         side_piece2: int) -> bool:
        """
        Check whether two pieces can be placed together with the given sides.

        Parameters
        ----------
        piece1: Piece
            First piece of this check.
        piece2: Piece
            Second piece of this check.
        side_piece1: int
            Integer indicating on which side piece 1 shall be connected to piece 2.
        side_piece2: int
            Integer indicating on which side piece 2 shall be connected to piece 1.

        Returns
        -------
        bool
            TRUE if the two pieces can be placed together on the given sides,
            FALSE otherwise.

        Notes
        -----
        The value of the second piece is negated because one side should be positive
        while the other side should be negative. Thus, the values should not be the
        same but instead be the negated values of one another.

        """
        return piece1.get_sides()[side_piece1] == -piece2.get_sides()[side_piece2]

    def rotate(self) -> None:
        """Rotate the piece by 120° to the right."""
        # Get the values of each side
        sides: list[int] = self.get_sides()

        # Move the first element to the end of the list
        sides.append(sides.pop(0))

        # Set the updated values
        self.set_sides(sides)

    def flip(self) -> None:
        """Flip the piece."""
        # Negate the indication whether the piece is upside down or not
        self.set_is_upside_down(not self.get_is_upside_down())

        # Switch the left and the right side
        sides_flipped: list[int] = self.get_sides()
        sides_flipped.reverse()
        self.set_sides(sides_flipped)

    @staticmethod
    def get_sides_of_pieces(pieces: list[list[Piece]]) -> list[str]:
        """
        Get the sides of all pieces contained in a two dimensional list.

        Parameters
        ----------
        pieces: list[list[Piece]]
            Two dimensional list containing the pieces.

        Returns
        -------
        pieces_information: list[str]
            Sides of all the pieces

        """
        # Initialize the return value
        pieces_information: list[str] = []

        # Go through each line of the pieces
        for line in pieces:
            # Add the values of each piece in the line
            pieces_information.append("".join([str(piece.get_sides())
                                               for piece in line]))

        return pieces_information
