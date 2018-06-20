import subprocess
import sys
from pprint import pprint
import pdb
import shlex


def convert_to_linux_path(path):
    # print("Before convert:", repr(path))
    path = path.replace("\\", "/")  # Must come before the rest.
    path = path.replace("C:", "/mnt/c")
    path = path.replace(" ", "\ ")
    path = path.replace("(", "\\(")
    path = path.replace(")", "\\)")
    # path = shlex.quote(path)
    # print("After convert:", repr(path))
    return path


def convert_all_paths_to_linux(paths):
    return [convert_to_linux_path(path) for path in paths]


def start_interpreter(cmd):
    with subprocess.Popen("bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) as proc:
        # proc.stdin.write(cmd)
        # proc.stdin.flush()
        # with proc.stdout as f:
        #     print(f.read())

        # print("Foo:", foo)
        try:
            outs, errs = proc.communicate(cmd)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
        # while True:
        #     with proc.stdin as f:
        #         line = proc.stdin.readline()
        #         if line == "exit()":
        #             break
        #         outs, errs = proc.communicate(line)
        #         if outs:
        #             pprint(outs)
        #         if errs:
        #             pprint(errs)

        print("Output:")
        pprint(outs)
        print("Errors:")
        pprint(errs)


if __name__ == "__main__":
    print("System arguments:", sys.argv)
    args = convert_all_paths_to_linux(sys.argv[1:])
    print("Converted args:", args)
    cmd = 'python3 {}'.format(' '.join(args))
    print("Command:", cmd)
    start_interpreter(cmd)
