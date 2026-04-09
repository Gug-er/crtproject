from pathlib import Path
import shutil

TEMPLATES_DIR = Path(__file__).parent / 'templates'


def generate_project(template: str, name: str, base_path: Path):

    template_path = TEMPLATES_DIR / template
    project_path = base_path / name

    if not template_path.is_dir():
        raise FileNotFoundError(f'Template {template} does not exist')
    if project_path.exists():
        raise FileExistsError(f'Project {project_path} already existы')

    shutil.copytree(template_path, project_path)

    print(f'Created project {name}')