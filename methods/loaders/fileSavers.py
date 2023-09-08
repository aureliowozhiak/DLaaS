# import csv


class FileSavers:
    def __init__(self):
        pass

    def save_content(self, content, file_name, columns=[], sep=","):
        with open(f"output/{file_name}", "w", encoding="utf-8") as file:
            if file_name.endswith(".csv"):
                file.write(sep.join(columns) + "\n")

                content_list = [sep.join(map(str, row)) for row in content]
                csv_string = "\n".join(content_list)
                file.write(csv_string)
            else:
                file.write(content)
