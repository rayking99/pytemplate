from glob import glob
from pathlib import Path
import shutil


def clone(src, dst, package_name, overwrite=False):
    if overwrite:
        shutil.rmtree(dst)

    replacements = {
        "my_package": package_name,
        "My Package": " ".join(map(str.capitalize, package_name.split("_"))),
        "my package": " ".join(package_name.split("_")),
        "package_description": "A package description",
        "package": package_name,
    }
    folders = glob(f"{src}/**/", recursive=True)
    # NOT __PYCACHE__ FOLDER
    folders = [folder for folder in folders if "__pycache__" not in folder]

    for folder in folders:
        # Create corresponding directory in destination
        dest_folder = folder.replace(src, dst)
        for key, value in replacements.items():
            dest_folder = dest_folder.replace(key, value)

        Path(dest_folder).mkdir(parents=True, exist_ok=True)

        files = glob(f"{folder}/*")
        for file in files:
            if Path(file).is_dir():
                continue  # Skip directories
            with open(file, "r") as f:
                content = f.read()

            for key, value in replacements.items():
                content = content.replace(key, value)

            dest_file = file.replace(src, dst)
            for key, value in replacements.items():
                dest_file = dest_file.replace(key, value)

            with open(dest_file, "w") as f:
                f.write(content)

    gitignore_file = Path(src) / ".gitignore"
    if gitignore_file.exists():
        with open(gitignore_file, "r") as f:
            content = f.read()
        dest_file = Path(dst) / ".gitignore"
        with open(dest_file, "w") as f:
            f.write(content)


if __name__ == "__main__":
    clone(
        # GET CURRENT DIRECTORY
        str(Path(__file__).parent.parent.parent),
        "/Users/jso/code/plain",
        "plain",
        overwrite=True,
    )
