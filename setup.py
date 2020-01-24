import setuptools

setuptools.setup(name='crop-transparent-image',
                 version='0.1',
                 description='Trim unnecessary transparent padding from your images',
                 # TODO: Uncomment after uploading project to github
                 # url='http://github.com/crazyhitty/crop-transparent-image',
                 author='Kartik Sharma',
                 author_email='kartik.sharma.og@gmail.com',
                 # TODO: Uncomment after adding license to project
                 # license='MIT',
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 install_requires=['Pillow'])
