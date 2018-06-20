import cx_Freeze

cx_Freeze.setup(
    name="source\python",
    version="0.1",
    description="",
    executables=[cx_Freeze.Executable("source\python.py")]
)
