import pyvips
import os


def createOutputFolder(resized_image_path):
    os.mkdir(os.path.dirname(resized_image_path))


def change_profile(source_image_path, destination_image_path, profile):
    image = pyvips.Image.new_from_file(source_image_path, access='sequential')
    result = image.icc_transform(profile)
    createOutputFolder(destination_image_path)
    result.write_to_file(destination_image_path)
