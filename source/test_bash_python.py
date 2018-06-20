fake_input = "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2018.1.4\helpers\pydev\pydevconsole.py"

import python
print(repr(fake_input))

assert python.covert_to_linux_path(fake_input).startswith("/mnt/c/Program\ Files\ \(x86\)/")
