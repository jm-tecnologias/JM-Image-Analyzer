# import os
# from plyer import filechooser
#
# class FileProcessor:
#
#     def getPath(self):
#         pasta = filechooser.choose_dir()
#         path = ''
#         if pasta:
#             path = pasta[0]
#             # label.config(text=path)
#             # if label == source:
#             #     load(path)
#         return path
#
#     def load(self):
#         data_source = {}
#         valid_extensions = ('.jpg', '.jpeg', '.png')
#
#         count = 1
#         path = self.getPath()
#         data_source[0] = {
#             'srcPath': path
#         }
#
#         if not path:
#             return
#         else:
#             for file in os.listdir(path):
#
#                 if file.lower().endswith(valid_extensions):
#                     full_path = os.path.join(path, file)
#                     # adicionar ao dicionário
#                     data_source[count] = {
#                         'absolutePath': full_path,
#                         'file':file
#                     }
#                     count += 1
#
#         return data_source
#
#
#
import os
from tkinter import filedialog
import datetime


class FileProcessor:

    def getPath(self):

        path = filedialog.askdirectory()

        if path:
            return path

        return None

    def get_folder_size(self, path):
        """Retorna o tamanho total da pasta em bytes"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def get_creation_date(self, path):
        """Retorna a data de criação da pasta em formato DD/MM/AAAA"""
        timestamp = os.path.getctime(path)
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%d/%m/%Y")

    def load(self):

        data_source = {}
        valid_extensions = ('.jpg', '.jpeg', '.png')

        path = self.getPath()

        if not path:
            return {}

        # pasta selecionada
        data_source[0] = {
            'srcPath': path
        }

        count = 1

        for file in os.listdir(path):

            if file.lower().endswith(valid_extensions):

                full_path = os.path.join(path, file)

                data_source[count] = {
                    'absolutePath': full_path,
                    'file': file
                }

                count += 1

        return data_source
#
# import os
# from tkinter import filedialog
# import datetime
#
# class FileProcessor:
#
#     def getPath(self):
#         path = filedialog.askdirectory()
#         if path:
#             return path
#         return None
#
#
#
#     def load(self):
#         data_source = {}
#         valid_extensions = ('.jpg', '.jpeg', '.png')
#
#         path = self.getPath()
#         if not path:
#             return {}
#
#         # info da pasta
#         folder_size = self.get_folder_size(path)
#         creation_date = self.get_creation_date(path)
#
#         data_source[0] = {
#             'srcPath': path,
#             'folderSize': folder_size,
#             'createdAt': creation_date
#         }
#
#         count = 1
#         for file in os.listdir(path):
#             if file.lower().endswith(valid_extensions):
#                 full_path = os.path.join(path, file)
#                 data_source[count] = {
#                     'absolutePath': full_path,
#                     'file': file
#                 }
#                 count += 1
#
#         return data_source