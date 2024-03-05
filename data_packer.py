import os
import shutil
import zipfile
from py7zr import SevenZipFile


class DataPacker:
    def __init__(self, data, archive_format='zip'):
        self.data = data
        self.archive_format = archive_format
    
    def pack_data(self, filename):
        if self.archive_format == 'zip':
            with zipfile.ZipFile(filename, 'w') as zip_file:
                for i, row in enumerate(self.data, 1):
                    zip_file.writestr(f'data_{i}.csv', ','.join(map(str, row)))
        elif self.archive_format == '7z':
            with SevenZipFile(filename, 'w') as seven_zip_file:
                for i, row in enumerate(self.data, 1):
                    seven_zip_file.writestr(f'data_{i}.csv', ','.join
                                            (map(str, row)))
        else:
            raise ValueError("Unsupported archive format")

    def split_and_pack_data(self, max_size, output_dir):
        chunk_size = max_size // (len(self.data) // 2)
        temp_dir = os.path.join(output_dir, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
       
        chunks = [self.data[i:i+chunk_size] for i in range(0, len(self.data),
                                                           chunk_size)]
        for i, chunk in enumerate(chunks, 1):
            filename = os.path.join(temp_dir,
                                    f'data_{i}.{self.archive_format}')
            self.pack_data(filename)
       
        shutil.make_archive(output_dir, 'zip', temp_dir)
        shutil.rmtree(temp_dir)
