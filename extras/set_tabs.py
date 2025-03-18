#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doc
"""
import logging
import argparse

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-f",
        "--file",
        help="What file to even tabs on.",
        action="store",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-s",
        "--symbols",
        help="What symbols to match tabs on",
        action="store",
        type="list",
        default=["#menu", "#!"],
    )

    parser.add_argument(
        "-o",
        "--output",
        help=(
            "Where the resulting changed file is stored. "
            "Defaults to overwrite input file."
        ),
        action="store",
        type="file",
        required=False,
    )

    args = parser.parse_args()
    lines = []
    with open(args.file) as file:
        print("reading file...")
        longest_line = ""
        longest_line_no = 0
        no_menu_entry = 0
        lines = []
        for line_number, line in enumerate(file, start=0):
            if line.find("#menu") != -1 or line.find("#!") != -1:
                if line.find("#menu") != -1:
                    lines.append(line.split("#menu"))
                    lines[-1].append("#menu")
                elif line.find("#!") != -1:
                    lines.append(line.split("#!"))
                    lines[-1].append("#!")
                    print("\nline:%s\n" % (line))

                if len(lines[line_number][0]) > len(longest_line):
                    longest_line = lines[line_number][0]
                    longest_line_no = line_number
            else:
                lines.append(line)
                no_menu_entry += 1

        print("no of entries with no menu: %i" % (no_menu_entry))
        print("longest line (%i): %s" % (len(longest_line), longest_line))
        print("it was at line %i" % (longest_line_no))

    for index, line in enumerate(lines):
        if isinstance(line, list):
            len_difference = len(longest_line) - len(line[0])
            lines[index] = line[0] + " " * len_difference + line[2] + line[1]

    for i in lines:
        if isinstance(i, list):
            print("found list")
            print(i)

    with open(args.file, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
