from pathlib import Path
import shutil

TEMPLATES_DIR = Path(__file__).parent / 'templates'


def generate_project(template: str, name: str, base_path: Path):
    base_path.mkdir(parents=True, exist_ok=True)

    template_path = TEMPLATES_DIR / template
    project_path = base_path / name

    if not template_path.exists():
        raise FileNotFoundError(f'Template {template} does not exist')
    if project_path.exists():
        raise FileExistsError(f'Project {project_path} already exists')

    shutil.copytree(template_path,
                    project_path,
                    ignore=shutil.ignore_patterns('.gitkeep'))

    print(f'Created project {name}')