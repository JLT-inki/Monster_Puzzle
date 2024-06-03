"""File containing the Puzzle class."""

# Import used class
from classes.piece import Piece

class Puzzle:
    """
    Class representing on puzzle.

    Attributes
    ----------
    size: int
        Number of pieces of the puzzle.
    pieces: list[Piece]
        The pieces of the puzzle.

    Methods
    -------
    set_size
        Set the size of the puzzle.
    set_pieces
        Set the pieces of the puzzle.
    get_size
        Return the size of the puzzle.
    get_pieces
        Return the pieces of the puzzle.
    find_solution
        Find ONE solution of the puzzle.

    """

    def __init__(self, size: int, pieces: list[Piece]) -> None:
        """
        Construct on Puzzle object with the given parameters.

        Parameters
        ----------
        size: int
            Number of pieces of the puzzle.
        pieces: list[Piece]
            The pieces of the puzzle.

        """
        self.set_size(size)
        self.set_pieces(pieces)

    def set_size(self, size: int) -> None:
        """
        Set the size of the puzzle.

        Parameters
        ----------
        size: int
            Number of pieces of the puzzle.

        """
        self.size = size

    def set_pieces(self, pieces: list[Piece]) -> None:
        """
        Set the pieces of the puzzle.

        Parameters
        ----------
        pieces: list[Piece]
            The pieces of the puzzle.

        """
        self.pieces: list[Piece] = pieces

    def get_size(self) -> int:
        """
        Return the size of the puzzle.

        Returns
        -------
        size: int
            Number of pieces of the puzzle.

        """
        return self.size

    def get_pieces(self) -> list[Piece]:
        """
        Return the pieces of the puzzle.

        Returns
        -------
        pieces: list[Piece]
            The pieces of the puzzle.

        """
        return self.pieces

    def find_solution(self, row: int, position: int, placed_pieces: list[list[Piece]],
                      remaining_pieces: list[Piece]) -> list[list[Piece]]:
        """
        Find ONE solution of the puzzle.

        Parameters
        ----------
        row: int
            Current row in which a piece should be placed.
        position: int
            Position in the current row in which a piece should be placed.
        placed_pieces: list[list[Piece]]
            Two dimensional list representing the pieces that are already placed.
            The position in the list represents the position of the piece in the actual
            puzzle.
        remaining_pieces: list[Piece]
            Pieces that have yet to be placed.

        Returns
        -------
        placed_pieces_new: list[list[Piece]]
            The first solution that was found. The position in the list represents the
            position of the piece in the actual puzzle.

        Notes
        -----
        This method only returns the first solution that it finds. In the case that no
        solution is found None is returned instead.

        """
        # Calculate the number of pieces that can be placed in this row
        width_row: int = row * 2 + 1

        # Go through each piece
        for piece in remaining_pieces:
            # Go through each rotation
            for _ in range(3):
                # Initialize the indication whether the piece can be placed
                can_be_placed: bool = False

                # Perform the check whether the piece can be placed
                # If it's the first piece of the row just place it
                if position == 0:
                    can_be_placed = True
                else:
                    # Differentiate between odd and even positions of the row
                    if position % 2 != 0:
                        # IF the position is odd the piece needs to flipped upside down
                        piece.flip()

                        # Check if the piece fits with its upper and left neighbor
                        if (Piece.two_pieces_match(
                            piece, placed_pieces[row][position - 1], 0, 2) and
                            Piece.two_pieces_match(
                                piece, placed_pieces[row - 1][position - 1], 1, 1)):
                            can_be_placed = True
                    else:
                        # Check if the piece fits with its left neighbor
                        if Piece.two_pieces_match(piece,
                                                  placed_pieces[row][position - 1],
                                                  0, 2):
                            can_be_placed = True

                # Check whether the piece can be placed
                if can_be_placed:
                    # Initialize the lists of pieces for the next function call
                    placed_pieces_new: list[Piece] = []
                    for row_puzzle in placed_pieces:
                        placed_pieces_new.append(row_puzzle.copy())

                    placed_pieces_new[row].append(piece)
                    remaining_pieces_new: list[Piece] = [
                        p for p in remaining_pieces if p != piece]

                    # Check whether the next row is reached
                    if position + 1 == width_row:
                        row_new: int = row + 1
                        position_new: int = 0
                    else:
                        row_new: int = row
                        position_new: int = position + 1

                    # Check whether there are no more pieces to place
                    if len(remaining_pieces_new) == 0:
                        # Return a found solution
                        return placed_pieces_new

                    # If there are still pieces left continue with the calculation
                    solution: list[list[Piece]] = self.find_solution(
                        row_new, position_new, placed_pieces_new,
                        remaining_pieces_new)

                    # Check whether the recursive function has found a solution
                    if solution is not None:
                        return solution

                # Flip the piece if it is currently upside down
                if piece.get_is_upside_down():
                    piece.flip()

                # Rotate the piece to get the next possibility
                piece.rotate()

        # Return None if no solution was found
        return None
