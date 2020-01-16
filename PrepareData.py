import os
import zipfile



path = "/home/russell/XCity"
pathExport = "/home/russell/XCity/Export"
zipFiles = []
for file in os.listdir(path):
    if file.endswith(".zip"):
        print(os.path.join(path, file))
        zipFiles.append(os.path.join(path, file))
print(zipFiles)
print("Unzipping files")
for i in zipFiles:
    with zipfile.ZipFile(i, 'r') as zip_ref:
        zip_ref.extractall(pathExport)
