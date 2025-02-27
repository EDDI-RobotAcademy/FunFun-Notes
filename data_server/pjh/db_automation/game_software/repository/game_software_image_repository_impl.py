import os

from game_software.entity.game_software_image import GameSoftwareImage
from game_software.repository.game_software_image_repository import GameSoftwareImageRepository


class GameSoftwareImageRepositoryImpl(GameSoftwareImageRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, gameSoftware, image):
        print(f"current working directory: {os.getcwd()}")
        uploadDirectory = os.path.join('../../../nuxt/notes/ui/assets/images/uploadImages')
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, image.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

            destination.flush()
            os.fsync(destination.fileno())

        return GameSoftwareImage.objects.create(gameSoftware=gameSoftware, image=image)
