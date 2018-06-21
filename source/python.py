##!/usr/bin/evn python

import subprocess
import sys
from pprint import pprint
import pdb
import shlex
import tempfile
import os
import multiprocessing


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


def start_python(pipeout):
    """Execute initial python arguments?"""
    print("System arguments:", sys.argv)
    args = convert_all_paths_to_linux(sys.argv[1:])
    print("Converted args:", args)
    cmd = ' '.join(["python3"] + args)
    print("Command:", cmd)
    pipeout.send(cmd)
    # line = None
    # while line != "exit()":
    #     line = input("Testing ...")
    #     os.write(pipeout, line.encode())


def read_subprocess_pipe(pipe):
    line = pipe.readline()
    while line:
        # print(line.decode().rstrip())
        line = pipe.readline()
        print(repr(line))


def start_interpreter(pipein, pipeout, pid=0):
    # pdb.set_trace()
    if pid == 0:
        print("111111111111111")
        # pipein.close()
        start_python(pipeout)
    else:
        print("22222222222222222")
        # external function
        # os.close(pipeout.fileno())
        # pipein = os.fdopen(pipein)
        # while True:
        # pipein.recv()
        # print(pipein.recv().encode())
        bash_proc = subprocess.Popen("bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        read_subprocess_pipe(bash_proc.stdout)

        print("Made it to input!!!")
        input = "{}\n".format(pipein.recv())
        bash_proc.stdin.write(input)

        # Read after python sending python command to bash ..
        read_subprocess_pipe(bash_proc.stdout)
        pdb.set_trace()
        line = bash_proc.stdout.readline()
        # while line:
        #     print(line.decode().rstrip())
        #     line = pipe.readline()


if __name__ == "__main__":
    pipein, pipeout = multiprocessing.Pipe()  # readpipe, writepipe
    bash_proc = multiprocessing.Process(target=start_interpreter, args=(pipein, pipeout), kwargs={'pid': 1})
    bash_proc.start()

    # external function 2?
    start_interpreter(pipein, pipeout)
    bash_proc.join()
