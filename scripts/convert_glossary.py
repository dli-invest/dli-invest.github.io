"""
Converts a tex glossary into a format jupyterbook can understand

Extended from https://tex.stackexchange.com/questions/529971/how-do-i-sort-all-of-the-glossary-entries-in-a-tex-file
"""

import argparse
import os
import re
import webbrowser
from collections import OrderedDict

commands = (r"\\newglossaryentry", r"\\newabbreviation", r"\\newacronym")
startcmd_regex = re.compile(
    r"(?:" + r"|".join(commands) + r")\s*\r?\n?\s*\{(.+?)\}\s*\r?\n?\s*\{"
)
brace_regex = re.compile(r"(?<!\\)(?:\\\\)*(\{|\})")


class UnreachableError(Exception):
    def __init__(self, *args, **kwargs):
        webbrowser.open("https://xkcd.com/2200/")
        super().__init__(
            "The code is in what I thought was an unreachable state.", *args, **kwargs
        )


class ParseError(Exception):
    pass


def scan_file(fname):
    """
    Scan a file and separate it into entries and outer code.

    Parameters
    ----------
    fname : str
        The file name.

    Raises
    ------
    ParseError
        If the end of an entry cannot be found.
    UnreachableError
        If a state is reached that should be unreachable.

    Returns
    -------
    entries : dict
        The entries.
        entries[None] always containes the collected outer code.

    """
    with open(fname, "r", errors="ignore") as rf:
        text = rf.read()
    open_braces = 0
    entries = {None: ""}
    label = None
    while text:
        if label is None:
            # Look for next entry.
            match = startcmd_regex.search(text)
            if match is None:
                piece = text.strip()
                if piece:
                    entries[label] += piece + "\n"
                text = ""
            else:
                piece = text[0 : match.start()].strip()
                if piece:
                    entries[label] += piece + "\n"
                label = match.group(1)
                if label in entries:
                    entries[label] += "\n"
                else:
                    entries[label] = ""
                entries[label] += match.group(0).lstrip()
                open_braces = 1
                text = text[match.end() :]
        else:
            # Look for next brace.
            match = brace_regex.search(text)
            if match is None:
                raise ParseError(
                    "I could not find all closing braces in "
                    + "'{}' ({} open braces)!".format(label, open_braces)
                )
            else:
                entries[label] += text[: match.end()]
                text = text[match.end() :]
                brace = match.group(1)
                if brace == "{":
                    open_braces += 1
                elif brace == "}":
                    open_braces -= 1
                else:
                    raise UnreachableError
                if open_braces == 0:
                    # This entry is done.
                    label = None
                elif open_braces < 0:
                    raise UnreachableError
    return entries


def sort_entries(source, *, label_sort=False):
    """
    Sort all the entries in the source file and returns and dict

    Parameters
    ----------
    source : str
        The name of the source file.
    label_sort : bool, optional
        If True, the entries are sorted by their label, otherwise they are
        sorted by their definition (including the definition command).
        The default is False.

    Raises
    ------
    ValueError
        If the source file cannot be found.

    Returns
    -------
    None.

    """
    present_files = os.listdir()
    if source not in present_files:
        raise ValueError("I cannot find the file '{}'!".format(source))
    entries = scan_file(source)
    return entries


def dict_with_descr(entries: dict):
    new_entries = {}
    for key in entries:
        if key == None:
            continue
        else:
            glossary_entry = entries[key]
            split_content = glossary_entry.split("description", 1)[1]
            # replace { } and \t \n
            cleaned_content = re.sub("{|}|\\t|\\n|=", "", split_content)
            # to extract words from string
            description = cleaned_content
            new_entries[key] = description

    return new_entries


def make_glossary(descriptions: dict):
    gloss_open = r"```{glossary}"
    gloss_end = r"```"
    body = ""
    # sort keys first
    for desc_key in sorted(descriptions.keys()):
        body = body + f"{desc_key}\n\t{descriptions[desc_key]}"
        body = body + "\n\n"
    return f"{gloss_open}\n{body}\n{gloss_end}"


def main():
    parser = argparse.ArgumentParser(description="Sort the glossary entries in a file.")
    parser.add_argument("-l", "--label-sort", action="store_true")
    parser.add_argument("source", help="The source file.")
    args = parser.parse_args()
    entries = sort_entries(args.source, label_sort=args.label_sort)
    descriptions = dict_with_descr(entries)
    glossary_str = make_glossary(descriptions)
    print(glossary_str)


if __name__ == "__main__":
    main()