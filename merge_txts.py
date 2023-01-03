import os

# Specify the directory path
directory = '/path/to/directory'

# Get the files in the directory
files = os.listdir(directory)

# Loop through each file
for file in files:
  # Get the full path of the file
  file_path = os.path.join(directory, file)
  # If the file extension is '.txt'
  if file.endswith('.txt'):
    # Read the file and write its content to 'final.txt'
    with open(file_path, 'r') as f:
      content = f.read()
      with open('final.txt', 'a') as final:
        final.write(content)
