import click
from typing import List

def split_txt_file(file_path: str, max_chars: int = 12000) -> List[str]:
    """
    Splits the content of a text file into parts with a maximum number of characters.

    :param file_path:   The path of the input text file.
    :param max_chars:   The maximum number of characters allowed in each part.
    :return:            A list of strings containing the parts.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    parts = []
    while content:
        part = content[:max_chars]
        parts.append(part)
        content = content[max_chars:]
    
    return parts

def save_parts(parts: List[str], output_prefix: str = 'part_') -> None:
    """
    Saves the parts to separate text files with a given prefix.

    :param parts:           A list of strings containing the parts.
    :param output_prefix:   The prefix for the output files.
    """
    for i, part in enumerate(parts):
        output_file = f"{output_prefix}{i}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(part)

@click.command()
@click.argument('input_file', default='input_file.txt', type=click.Path(exists=True))
@click.option('--max_chars', default=12000, help='The maximum number of characters per part (default: 4000)')
def main(input_file: str, max_chars: int) -> None:
    """
    Splits a text file into parts with a maximum number of characters and saves them as separate files.

    :param input_file:  The path of the input text file.
    :param max_chars:   The maximum number of characters allowed in each part.
    """
    parts = split_txt_file(input_file, max_chars)
    save_parts(parts)

if __name__ == '__main__':
    main()