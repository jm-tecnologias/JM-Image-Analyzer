from reportlab.platypus import Flowable, Image


class ClickableImage(Flowable):

    def __init__(self, path, width, height, url):
        super().__init__()
        self.img = Image(path, width=width, height=height)
        self.width = width
        self.height = height
        self.url = url

    def draw(self):

        self.img.drawOn(self.canv, 0, 0)

        # 🔥 link externo padrão (abre browser)
        self.canv.linkURL(
            self.url,
            (0, 0, self.width, self.height),
            relative=1,
            kind="URI"
        )