from glob import glob
from pathlib import Path

package_name = "jp"
package_full_name = "JUSTPACKAGE"
authors = "jason pickup"
email = "a@b.c"
python_version_min = "3.8"

files = glob("**/*", recursive=True)
files = [Path(file) for file in files if file != "concat.py" and Path(file).is_file()]
files = [file for file in files if Path(file).name != "concatenated.md"]
files = [file for file in files if Path(file).name != "README.md"]
files = [file for file in files if Path(file).name != "LICENSE"]
files = list(set(files))

concatenated = ""
for file in files:
    with open(file) as f:
        contents = f.read()
        try:
            path_from_root = file.relative_to(Path.cwd())
        except ValueError:
            path_from_root = file
        if file.suffix == ".md":
            # Indent each line of the Markdown content
            indented_contents = "\n".join(
                [f"    {line}" for line in contents.splitlines()]
            )
            concatenated += f"{path_from_root}\n```\n{indented_contents}\n```\n\n"
        else:
            if file.suffix == file.name:
                concatenated += f"{path_from_root}\n```\n{contents}\n```\n\n"
            else:
                concatenated += f"{path_from_root}\n```{file.suffix.replace('.', '')}\n{contents}\n```\n\n"
    concatenated = (
        concatenated.replace("my_package", package_name)
        .replace("My Package", package_full_name)
        .replace("Your Name", authors)
        .replace("a@b.c", email)
        .replace("3.8", python_version_min)
    )

with open("concatenated.md", "w") as f:
    f.write(concatenated)
