from pypdf import PdfReader, PdfWriter
def trim_interface():
    choice = int(input("[0] Delete pages continuously\n[1] Delete pages with specific indices\n$> "))
    file_string = input("name of PDF file in current folder to edit: ")
    pages = []
    file = PdfReader(f"./{file_string}")
    writer = PdfWriter()
    print(f"The file has {len(file.pages)} pages")
    if choice == 0:
        page_start = int(input("Starting index (page index from 1): "))
        page_end = int(input("End index (page index from 1): "))
        for i in range(page_start-1, page_end):
            pages.append(i)
    else:
        while True:
            index_s = input("Enter page number to delete (X to eXit): ")
            if index_s == "X": break
            pages.append(int(index_s))
    print(f"Deleting pages of the following indices: {pages}")
    input("Press ENTER to confirm and continue...")
    for page in file.pages:
        if page.page_number in pages: continue
        writer.add_page(page)
        print(f"Added original page {page.page_number} to PDF writer")
    with open(f"{file_string[:-4]}.trim.pdf", "wb") as fp:
        writer.write(fp)
if __name__ == "__main__":
    while True:
        trim_interface()
        choice = input("Continue trimming other PDF files? [y/N]")
        if choice == "y": pass
        elif choice == "N":
            print("Goodbye.")
            exit(0)