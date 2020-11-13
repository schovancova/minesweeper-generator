# -*- coding: utf-8 -*-
"""Minesweeper field generation class"""
import random
import sys

MINE = "X"


class FieldGenerator:
    """Algorithmic part of field generation"""
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines

    def validate_size(self):
        """Determine whether a board with given requirements can be drawn"""
        if self.rows < 0 or self.cols < 0 or self.mines < 0:
            sys.exit(f"Negative arguments are not allowed")
        if self.mines > self.rows * self.cols:
            sys.exit(f"Unable to place {self.mines} mines into {self.cols}x{self.rows} size field")

    def get_field_data(self):
        """Gets field data"""
        empty_field = self._create_field()
        mines = self._set_mines(empty_field)
        return self._set_clues(mines)

    def _create_field(self):
        """Creates field filled with 0's initially"""
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def _set_mines(self, field):
        """Randomly places mines around the field

        Args:
            field (list of lists): Empty field containing 0's

        Returns:
            list of lists: Field with randomly placed mines
        """
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if field[row][col] != MINE:
                mines_placed += 1
                field[row][col] = MINE
        return field

    def _set_clues(self, field):
        """Calculates and fills in the clues.
        Clues are calculated based on presence of mines in adjacent tiles (in all 8 directions).

        Args:
            field (list of lists): Field containing 0-n mines

        Returns:
            list of lists: Field mines and clues
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if field[row][col] == MINE:
                    continue
                # Check N
                if row > 0 and field[row - 1][col] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check S
                if row < self.rows - 1 and field[row + 1][col] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check E
                if col < self.cols - 1 and field[row][col + 1] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check W
                if col > 0 and field[row][col - 1] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check NW
                if row > 0 and col > 0 and field[row - 1][col - 1] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check NE
                if row > 0 and col < self.cols - 1 and field[row - 1][col + 1] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check SW
                if row < self.rows - 1 and col > 0 and field[row + 1][col - 1] == MINE:
                    field[row][col] = field[row][col] + 1
                # Check SE
                if row < self.rows - 1 and col < self.cols - 1 and field[row + 1][col + 1] == MINE:
                    field[row][col] = field[row][col] + 1
        return field
