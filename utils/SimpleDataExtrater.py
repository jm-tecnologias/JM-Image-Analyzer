from PIL import Image
from PIL.ExifTags import TAGS

class SimpleDataExtrater:
    def extrator(self, path):
        metaDataSouce = {}
        img = Image.open(path)

        exifData = img._getexif()
        if exifData:
            for tag_id, value in exifData.items():
                tag = TAGS.get(tag_id, tag_id)
                # metaDataSouce = {
                #     tag: value
                # }

                metaDataSouce[tag] = value

        return metaDataSouce

# sde = SimpleDataExtrater()
#
# print(sde.extrator('../assets/photo.jpg'))