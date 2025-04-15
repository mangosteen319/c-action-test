import os, subprocess

# Settings
TEST_DIR = "."
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0     #in seconds
RUN_TIMEOUT = 10.0

# Create absolute path
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile the program
print("Building...")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path], 
                            stdout=subprocess.PIPE,


Skip navigation
Search



Sign in

                            stderr=subprocess.PIPE,
                            timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed.", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

# Check to see if the program compiled successfully
if ret.returncode != 0:
    print("Compilation failed.")
    exit(1)

# Run the compiled program
print("Running...")
try:
    ret = subprocess.run([app_path],
                            stdout = subprocess.PIPE,
                            timeout = RUN_TIMEOUT)
except Exception as e:
    print("ERROR: Runtime failed.", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode('utf-8')
print("Output:", output)

# All tests passed! Exit gracefully
print("All tests passsed!")
exit(0)
