#!/usr/bin/env python3
import os
import subprocess
import sys

argc = len(sys.argv)
argv = sys.argv
if argc > 1:
    target = argv[1]
    if target == "run":
        print("[run] running...")
        os.chdir("dotnet_client")
        subprocess.run(["./bin/Debug/netcoreapp3.1/game"])
        os.chdir("..")
        sys.exit()
print("[build] building...")
os.chdir("dotnet_client")
subprocess.run(["dotnet","build"])
print("[run] running...")
subprocess.run(["./bin/Debug/netcoreapp3.1/game"])
os.chdir("..")
