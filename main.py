# -*- coding: utf-8 -*-
"""Main module"""
import argparse
from src.field_generator import FieldGenerator
from src.field_visualizer import FieldVisualizer


def main():
    """Function for parsing arguments and visualizing the minesweeper field"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-rows', type=int, required=True)
    parser.add_argument('-cols', type=int, required=True)
    parser.add_argument('-mines', type=int, required=True)
    args = parser.parse_args()

    # generate field and draw it
    generator = FieldGenerator(**vars(args))
    generator.validate_size()
    field_data = generator.get_field_data()
    FieldVisualizer(data=field_data, **vars(args)).draw_field()


if __name__ == '__main__':
    main()
