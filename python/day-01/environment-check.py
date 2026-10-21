import platform
import sys

print("Python environment check")
print("------------------------")
print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Operating system:", platform.system())
print("Platform details:", platform.platform())