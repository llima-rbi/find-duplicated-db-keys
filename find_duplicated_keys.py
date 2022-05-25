import re
import os

FILE_NAME = "i18ncustom.ddl"

def main():
    if not os.path.exists(FILE_NAME):
        print "File not found!"
        return

    with open(FILE_NAME, "rb") as f:
        i18n_data = f.read()

    unique_keys = []
    for line in [line for line in i18n_data.split("\n") if line.startswith("INSERT INTO")]:
        language = line.split("VALUES (")[1].split(",")[0]
        key = " ".join(re.findall("[a-zA-Z_0-9]+", line.split(" ")[8]))

        unique_key = (language, key)
        if unique_key in unique_keys:
            print "Duplicated key found! Languange: [{}]; Key: [{}]".format(language, key)

        unique_keys.append(unique_key)

main()


