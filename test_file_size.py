import os


def test_file_size():
    picture_size = os.path.getsize('./resources/sampleFile.jpeg')
    assert picture_size == 4096

    print(os.path.abspath('./resources/sampleFile.jpeg'))


os.path.dirname(os.path.abspath('./resources/sampleFile.jpeg'))

current_dir = os.path.dirname(os.path.abspath(__file__))
resources = os.path.join(current_dir, 'resources')
print(resources)
resources_tmp = os.path.join(current_dir, 'resources', 'tmp')
print(resources_tmp)

