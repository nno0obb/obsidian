import re
from pathlib import Path

import git
from tqdm import tqdm

EXCLUDED_DIR_LIST = [
    "_attachments",
    "_scripts",
    "_tags",
    "_templates",
]

EXCLUDED_FILE_LIST = [
    "README.md",
    "welcome.md",
]


def get_root_path() -> Path:
    repo = git.Repo(".", search_parent_directories=True)
    root_path = repo.working_dir
    return Path(root_path)


def get_note_path_list(root_path: Path) -> list[Path]:
    note_path_list = []
    for path in root_path.glob("**/*.md"):
        if not path.is_file():
            continue

        relative_path = path.relative_to(root_path)
        if relative_path.parts[0] in EXCLUDED_DIR_LIST:
            continue

        if relative_path.name in EXCLUDED_FILE_LIST:
            continue

        note_path = path
        note_path_list.append(note_path)

    return note_path_list


def update_note(root_path: Path, note_path: Path):
    with open(note_path, "r", encoding="utf-8") as f:
        content = f.read()
        pattern = r"(>> \[!example\] Paths\n)(.*)$"
        match = re.search(pattern, content, flags=re.S)

        if match:
            paths_deleted_content = re.sub(pattern, r"\1", content, flags=re.S)
            paths = note_path.parent.relative_to(root_path).parts
            updated_paths = str()
            for idx, path in enumerate(paths):
                updated_paths += f">>{' ' * (idx * 2)} - [[🔖 {path}]]\n"
            paths_updated_content = f"{paths_deleted_content}{updated_paths}"

            with open(note_path, "w", encoding="utf-8") as g:
                g.write(paths_updated_content)


def main():
    root_path = get_root_path()
    note_path_list = get_note_path_list(root_path)
    for note_path in tqdm(note_path_list):
        update_note(root_path, note_path)


if __name__ == "__main__":
    main()
