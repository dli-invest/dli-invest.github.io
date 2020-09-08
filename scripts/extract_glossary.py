import argparse
import os
import re
import webbrowser

commands = (r'\\newglossaryentry',
            r'\\newabbreviation',
            r'\\newacronym')
startcmd_regex = re.compile(r'(?:'
                            + r'|'.join(commands)
                            + r')\s*\r?\n?\s*\{(.+?)\}\s*\r?\n?\s*\{')
brace_regex = re.compile(r'(?<!\\)(?:\\\\)*(\{|\})')

class UnreachableError(Exception):
    def __init__(self, *args, **kwargs):
        webbrowser.open('https://xkcd.com/2200/')
        super().__init__("The code is in what I thought was an unreachable state.",
                         *args, **kwargs)

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
    with open(fname, 'r') as rf:
        text = rf.read()
    open_braces = 0
    entries = {None: ''}
    label = None
    while text:
        if label is None:
            # Look for next entry.
            match = startcmd_regex.search(text)
            if match is None:
                piece = text.strip()
                if piece:
                    entries[label] += piece + '\n'
                text = ''
            else:
                piece = text[0:match.start()].strip()
                if piece:
                    entries[label] += piece + '\n'
                label = match.group(1)
                if label in entries:
                    entries[label] += '\n'
                else:
                    entries[label] = ''
                entries[label] += match.group(0).lstrip()
                open_braces = 1
                text = text[match.end():]
        else:
            # Look for next brace.
            match = brace_regex.search(text)
            if match is None:
                raise ParseError("I could not find all closing braces in "
                                 + "'{}' ({} open braces)!".format(label,
                                                                   open_braces))
            else:
                entries[label] += text[:match.end()]
                text = text[match.end():]
                brace = match.group(1)
                if brace == '{':
                    open_braces += 1
                elif brace == '}':
                    open_braces -= 1
                else:
                    raise UnreachableError
                if open_braces == 0:
                    # This entry is done.
                    label = None
                elif open_braces < 0:
                    raise UnreachableError
    return entries

def sort_entries(source, target=None, *, label_sort=False):
    """
    Sort all the entries in the source file and write them to the target file.

    If target is None, the source file is backed up and target is set to source.

    Parameters
    ----------
    source : str
        The name of the source file.
    target : str, optional
        The name of the target file. The default is None.
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
    if target is None or target == source:
        target = source
        # Backup the source file in caes something goes wrong.
        source_parts = source.split('.')
        n = 0
        while True:
            source = '.'.join(source_parts[:-1]
                              + ['backup{}'.format(n),
                                 source_parts[-1]])
            if source not in present_files:
                break
            n += 1
        os.rename(target, source)
    entries = scan_file(source)
    with open(target, 'w') as wf:
        wf.write(entries[None] + '\n')
        labels = list(entries.keys())
        labels.remove(None)
        if label_sort:
            keyfun = None
        else:
            keyfun = lambda x: entries[x]
        labels.sort(key=keyfun)
        for l in labels:
            wf.write(entries[l] + '\n')

def main():
    parser = argparse.ArgumentParser(description="Sort the glossary entries in a file.")
    parser.add_argument('-l', '--label-sort', action='store_true')
    parser.add_argument('source',
                        help="The source file.")
    parser.add_argument('target', nargs='?',
                        help="The target file.")
    args = parser.parse_args()
    sort_entries(args.source, args.target, label_sort=args.label_sort)


if __name__ == '__main__':
    main()