import os
import pathspec
import sys

def read_gitignore(gitignore_path):
    with open(gitignore_path) as f:
        gitignore_contents = f.read()

    return pathspec.PathSpec.from_lines('gitwildmatch', gitignore_contents.splitlines())

def print_structure(root, path_spec, prefix=''):
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry)
        rel_path = os.path.relpath(path, start=os.path.abspath('.'))

        if path_spec.match_file(rel_path) or '.git' in rel_path.split(os.sep):
            continue

        if os.path.isdir(path):
            print(f"{prefix}- {entry}")
            print_structure(path, path_spec, prefix=prefix + '--')
        else:
            print(f"{prefix}-- {entry}")

def main():
    print(sys.argv[1])
    project_root = os.path.abspath(sys.argv[1])
    print(project_root)
    project_name = os.path.basename(project_root)
    print(project_name)

    gitignore_path = os.path.join(project_root, '.gitignore')
    path_spec = read_gitignore(gitignore_path)

    print_structure(project_root, path_spec)

if __name__ == '__main__':
    main()
