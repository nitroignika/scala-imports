def create_scala_imports(scala_imports_file: str):
    data = open(scala_imports_file).readlines()
    for n, line in enumerate(data):
        data[n] = line.rstrip().replace(";", "").replace("import", "").replace("static", "")
    import_string = ",".join(data).replace("  ", " ")
    final_string = "import " + import_string[1:]

    print(final_string)
    return final_string


def get_imports():
    scala_imports = create_scala_imports("imports.txt")
    with open('imports-output.txt', 'a') as imports_output:
        imports_output.truncate(0)
        imports_output.write(scala_imports)
    return 0


get_imports()
