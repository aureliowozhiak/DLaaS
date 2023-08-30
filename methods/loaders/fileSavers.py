import csv

class FileSavers:
    def __init__(self):
        pass

    def saveContent(self, content, file_name, columns=[], sep=","):
        with open(f"output/{file_name}", "w") as file:
            if file_name.endswith(".csv"):
                file.write(sep.join(columns) + "\n")

                csv_string = "\n".join([sep.join(map(str, row)) for row in content])
                file.write(csv_string)
            else:
                file.write(content)