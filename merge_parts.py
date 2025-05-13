from PyPDF2 import PdfMerger
import os

# Your PDF folder path (Windows-friendly format)
pdf_folder = r"C:\Users\Marwan\Downloads"

# Filenames for output
revision_output = os.path.join(pdf_folder, "Revision Sheet Merged.pdf")
ms_output = os.path.join(pdf_folder, "Mark Schemes Merged.pdf")

# Helper function to get sorted PDFs by type
def get_sorted_pdfs(folder, ms=False):
    pdfs = []
    for i in range(1, 10):  # Part1 to Part9
        name = f"Part{i} Ms.pdf" if ms else f"Part{i}.pdf"
        full_path = os.path.join(folder, name)
        if os.path.exists(full_path):
            pdfs.append(full_path)
        else:
            print(f"⚠️ Missing: {full_path}")
    return pdfs

# Merge revision sheets
revision_merger = PdfMerger()
for pdf in get_sorted_pdfs(pdf_folder, ms=False):
    revision_merger.append(pdf)
revision_merger.write(revision_output)
revision_merger.close()
print(f"✅ Revision sheets merged: {revision_output}")

# Merge mark schemes
ms_merger = PdfMerger()
for pdf in get_sorted_pdfs(pdf_folder, ms=True):
    ms_merger.append(pdf)
ms_merger.write(ms_output)
ms_merger.close()
print(f"✅ Mark schemes merged: {ms_output}")