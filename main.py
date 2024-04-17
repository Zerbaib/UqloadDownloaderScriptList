from lib.uqload_dl.uqload import UQLoad

dirPath = input("Enter the path to the directory where the files are located: ")
serieName = input("Enter the name of the series: ")
seasonNumber = int(input("Enter the season number: "))
i = 1

try:
    with open('link.txt', 'r') as file:
        links = file.readlines()

    for link in links:
        print()
        fileName = f"{serieName} EP{i} S{seasonNumber}"
        i += 1
        try:
            uqload = UQLoad(url=link.strip(), output_dir=dirPath, output_file=fileName)
            uqload.download()
        except ValueError as e:
            print(f"[ERROR] Error during downloading video: {link.strip()}")
            print(f"[ERROR] Reason (if available): {e}")

except FileNotFoundError:
    print("[ERROR] Error: 'link.txt' file not found!")
