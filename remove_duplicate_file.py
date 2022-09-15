# Hashing in Python
import hashlib

example_text = "Duplython is amazing".encode('utf-8')
print(hashlib.md5(example_text).hexdigest())

# Hashing File
import hashlib

file = open('learn.txt', 'rb').read()
print(hashlib.md5(file).hexdigest())

# Hashing File
import hashlib

block_size = 1024
hash = hashlib.md5()
with open('learn.txt', 'rb') as file:
    block = file.read(block_size)
    while len(block) > 0:
        hash.update(block)
        block = file.read(block_size)
    print(hash)

# import os
import os

print(os.listdir())
# os.remove('learn.txt')
print(os.listdir())

# ---------------------------------------------------------------------------------------------------

# =====[ Generate Hash ]=====
import time
import os
from hashlib import sha256


class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd();
        self.File_hashes = []
        self.Cleaned_dirs = [];
        self.Total_bytes_saved = 0
        self.block_size = 65536;
        self.count_cleaned = 0

    def welcome(self)->None:
        print('***************************************************************')
        print('*********************      DUPLYTHON     **********************')
        print('***************************************************************\n\n')
        print('---------------------      WELCOME       ----------------------')
        time.sleep(3)
        print('\nCleaning .........................')

    def main(self)->None:
        self.welcome()

if __name__ == '__main__':
    App = Duplython()
    App.main()
    # print(App.main())
# =====[ Generate Hash ]=====

# ---------------------------------------------------------------------------------------------------

# =====[ Generate Hash ]=====
import time
import os
from hashlib import sha256


class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd();
        self.File_hashes = []
        self.Cleaned_dirs = [];
        self.Total_bytes_saved = 0
        self.block_size = 65536;
        self.count_cleaned = 0

    def welcome(self) -> None:
        print('******************************************************************')
        print('********************        DUPLYTHON      ************************')
        print('********************************************************************\n\n')
        print('--------------------        WELCOME        ------------------------')
        time.sleep(3)
        print('\nCleaning .................')

    def generate_hash(self, Filename: str) -> str:
        Filehash = sha256()
        try:
            with open(Filename, 'rb') as File:
                fileblock = File.read(self.block_size)
                while len(fileblock) > 0:
                    Filehash.update(fileblock)
                    fileblock = File.read(self.block_size)
                Filehash = Filehash.hexdigest()
            return Filehash
        except:
            return False

    def main(self) -> None:
        self.welcome()


if __name__ == '__main__':
    App = Duplython()
    App.main()
# =====[ Generate Hash ]=====

# ---------------------------------------------------------------------------------------------------

# =====[ Generate Hash ]=====
import time
import os
from hashlib import sha256


class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd();
        self.File_hashes = []
        self.Cleaned_dirs = [];
        self.Total_bytes_saved = 0
        self.block_size = 65536;
        self.count_cleaned = 0

    def welcome(self) -> None:
        print('******************************************************************')
        print('********************        DUPLYTHON      ***********************')
        print('******************************************************************\n\n')
        print('--------------------        WELCOME        -----------------------')
        time.sleep(3)
        print('\nCleaning .................')

    def generate_hash(self, Filename: str) -> str:
        Filehash = sha256()
        try:
            with open(Filename, 'rb') as File:
                fileblock = File.read(self.block_size)
                while len(fileblock) > 0:
                    Filehash.update(fileblock)
                    fileblock = File.read(self.block_size)
                Filehash = Filehash.hexdigest()
            return Filehash
        except:
            return False

    def clean(self) -> None:
        all_dirs = [path[0] for path in os.walk('.')]
        for path in all_dirs:
            os.chdir(path)
            All_Files = [file for file in os.listdir() if os.path.isfile(file)]
            for file in All_Files:
                filehash = self.generate_hash(file)
                if not filehash in self.File_hashes:
                    if filehash:
                        self.File_hashes.append(filehash)
                        # print(file)
                else:
                    byte_saved = os.path.getsize(file);
                    self.count_cleaned += 1
                    self.Total_bytes_saved += byte_saved
                    os.remove(file);
                    filename = file.split('/')[-1]
                    print(filename, '.. cleaned ')
            os.chdir(self.home_dir)

    def main(self) -> None:
        self.welcome();
        self.clean()


if __name__ == '__main__':
    App = Duplython()
    App.main()
# =====[ Generate Hash ]=====

# ---------------------------------------------------------------------------------------------------

# =====[ Generate Hash ]=====
import time
import os
import shutil
from hashlib import sha256


class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd();
        self.File_hashes = []
        self.Cleaned_dirs = [];
        self.Total_bytes_saved = 0
        self.block_size = 65536;
        self.count_cleaned = 0

    def welcome(self) -> None:
        print('******************************************************************')
        print('********************        DUPLYTHON      ***********************')
        print('******************************************************************\n\n')
        print('--------------------        WELCOME        -----------------------')
        time.sleep(3)
        print('\nCleaning .................')

    def generate_hash(self, Filename: str) -> str:
        Filehash = sha256()
        try:
            with open(Filename, 'rb') as File:
                fileblock = File.read(self.block_size)
                while len(fileblock) > 0:
                    Filehash.update(fileblock)
                    fileblock = File.read(self.block_size)
                Filehash = Filehash.hexdigest()
            return Filehash
        except:
            return False

    def clean(self) -> None:
        all_dirs = [path[0] for path in os.walk('.')]
        for path in all_dirs:
            os.chdir(path)
            All_Files = [file for file in os.listdir() if os.path.isfile(file)]
            for file in All_Files:
                filehash = self.generate_hash(file)
                if not filehash in self.File_hashes:
                    if filehash:
                        self.File_hashes.append(filehash)
                        # print(file)
                else:
                    byte_saved = os.path.getsize(file);
                    self.count_cleaned += 1
                    self.Total_bytes_saved += byte_saved
                    os.remove(file);
                    filename = file.split('/')[-1]
                    print(filename, '.. cleaned ')
            os.chdir(self.home_dir)

    def cleaning_summary(self) -> None:
        mb_saved = self.Total_bytes_saved / 1048576
        mb_saved = round(mb_saved, 2)
        print('\n\n------------    FINISHED CLEANING    ------------')
        print('File cleaned  : ', self.count_cleaned)
        print('Total Space saved : ', mb_saved, 'MB')
        print('-----------------------------------------------')

    def main(self) -> None:
        self.welcome();
        self.clean();
        self.cleaning_summary()


if __name__ == '__main__':
    App = Duplython()
    App.main()

# =====[ Generate Hash ]=====
# with open('learn.txt', 'w') as f:
#     f.write('Create a new text file!')


