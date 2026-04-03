import os
from plyer import filechooser


class FileProcessor:

    def getPath(self):
        pasta = filechooser.choose_dir()
        path = ''
        if pasta:
            path = pasta[0]
            # label.config(text=path)
            # if label == source:
            #     load(path)
        return path

    def load(self):
        data_source = {}
        valid_extensions = ('.jpg', '.jpeg', '.png')

        count = 1
        path = self.getPath()
        data_source[0] = {
            'srcPath': path
        }

        if not path:
            return
        else:
            for file in os.listdir(path):

                if file.lower().endswith(valid_extensions):
                    full_path = os.path.join(path, file)
                    # adicionar ao dicionário
                    data_source[count] = {
                        'absolutePath': full_path,
                        'file':file
                    }
                    count += 1

        return data_source

