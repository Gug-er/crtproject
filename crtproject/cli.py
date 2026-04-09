import argparse
from pathlib import Path

from .generator import generate_project

PROJECT_PATH = Path('D:/Code/python')

def main():
    parser = argparse.ArgumentParser(
        prog = 'crtproject',
        description = 'Generate a project from a template'
    )

    parser.add_argument(
        'template',
        help = 'The template name'
    )

    parser.add_argument(
        'name',
        help = 'The name of the project'
    )

    args = parser.parse_args()

    generate_project(
        template = args.template,
        name = args.name,
        base_path = PROJECT_PATH
    )