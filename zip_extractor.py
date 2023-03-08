import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)
        
        
if __name__ == "__main__":
    extract_archive(r"C:\Users\lucasmaia\Desktop\Udemy\compressed.zip", 
                    r"C:\Users\lucasmaia\Desktop\Udemy")