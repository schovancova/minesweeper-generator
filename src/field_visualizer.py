# -*- coding: utf-8 -*-
"""Minesweeper field visualization class"""
import matplotlib.pyplot as plt
from matplotlib.table import Table

from src.field_generator import MINE

COLORS = ["blue", "green", "red"]
FONT_SIZE = 20


class FieldVisualizer:
    """Visualization of the field"""
    def __init__(self, data, rows, cols, mines):
        self.data = data
        self.rows = rows
        self.cols = cols
        self.mines = mines

    def draw_field(self):
        """Draws the field"""
        self._create_table()
        plt.show()

    @staticmethod
    def _get_color(value):
        """Determines color of a field

        Args:
            value (int): Clue number

        Returns:
            string: appropriate color for the field
        """
        if value < len(COLORS):
            return COLORS[value - 1]
        return COLORS[-1]

    def _create_table(self):
        """Creates a table for displaying the entire field using matplotlib table."""
        _, axis = plt.subplots()
        axis.set_axis_off()
        table = Table(axis, bbox=[0, 0, 1, 1])
        try:
            width, height = 1.0 / self.rows, 1.0 / self.cols
        except ZeroDivisionError:
            # No table is going to be drawn, cols or rows is 0
            return
        current_col = 0
        while current_col < self.cols:
            for current_row in range(0, self.rows):
                value = self.data[current_row][current_col]
                cell = table.add_cell(current_col, current_row, width, height,
                                      text=value or "", loc='center')
                if value != MINE:
                    text_color = self._get_color(value)
                    cell.get_text().set_color(text_color)
                cell.get_text().set_fontsize(FONT_SIZE)
            current_col += 1
        title = f"Game, W: {self.rows}, H: {self.cols}, Mines: {self.mines}"
        axis.set_title(title)
        axis.add_table(table)
