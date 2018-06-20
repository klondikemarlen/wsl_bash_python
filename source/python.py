import subprocess
import sys


def convert_to_linux_path(path):
    print("Before convert:", repr(path))
    path = path.replace("\\", "/")  # Must come before the rest.
    path = path.replace("C:", "/mnt/c")
    path = path.replace(" ", "\ ")
    path = path.replace("(", "\\(")
    path = path.replace(")", "\\)")
    print("After convert:", repr(path))
    return path


def convert_all_paths_to_linux(paths):
    return [convert_to_linux_path(path) for path in paths]


if __name__ == "__main__":
    print("System arguments:", sys.argv)
    args = convert_all_paths_to_linux(sys.argv[1:])
    print("Converted args:", args)
    cmd = "bash -c 'python3 {}'".format(' '.join(args))
    print(cmd)
    process = subprocess.run(cmd, stderr=subprocess.STDOUT)
    print(process)
