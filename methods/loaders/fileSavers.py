import csv

class FileSavers:
    def __init__(self):
        pass

    def saveContent(self, content, file_name, columns):
        with open(file_name, "w") as file:
            if file_name.endswith(".csv"):
                file.write(",".join(columns) + "\n")

                csv_string = "\n".join([",".join(map(str, row)) for row in content])
                file.write(csv_string)
            else:
                file.write(content)