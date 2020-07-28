import click

@click.command()
@click.option('-a/-d', 'sort')
@click.option('-s/-i', 'typ')
@click.argument('res', nargs=1)
@click.argument('files', nargs=-1)
def run(sort=None, typ=None, res=None, files=None):
    mergeFile(sort, typ, res, files)

def mergeFile(sort, typ, res, files):
    
    print(f"{res} {files} = {len(files)}")

    if len(files) == 1:
        print(f"final {res}") #TODO Переименовать последний файл используя параметр res
        return

    result = []
    
    groupFileList = [files[i:i + 2] for i in range(0, len(files), 2)]
    
    for groupFiles in groupFileList:
        if len(groupFiles) == 1:
            result.append(groupFiles[0])
            continue
        
        fileName1, fileName2 = groupFiles
        resultFileName = "result.txt" #TODO random file name

        with open(fileName1) as file1,\
             open(fileName2) as file2,\
             open(resultFileName, "w") as resultFile:
            
            str1, str2 = convert(file1.readline(), typ), convert(file2.readline(), typ)
            
            while str1 or str2:
                print(f"{str1} | {str2}")
                
                if not str2 or str1 <= str2:
                    resultFile.write(str(str1))
                    str1 = convert(file1.readline(), typ)
                elif not str1 or str1 > str2:
                    resultFile.write(str(str2))
                    str2 = convert(file2.readline(), typ)

                resultFile.write("\n")
        result.append(resultFileName)
    mergeFile(sort, typ, res, result)

def convert(string, typ):
    if typ:
        return string

    try:
        return int(string)
    except Exception:
        pass


if __name__ == "__main__":
    run()