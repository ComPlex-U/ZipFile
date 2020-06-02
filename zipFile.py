from zipfile import ZipFile

file_path = "\Redes-2.zip"

with ZipFile(file_path, "r") as zip_:
    zip_.printdir()
    zip_.extractall()