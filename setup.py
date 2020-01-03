import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='python_learning',  

     version='1.0.0',

     scripts=['py1/py1/py1.py'] ,

     author="ricksy",

     author_email="ricksy@mailbox.org",

     description="A reverse text utility package",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/ricksy",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],
     project_urls={  
         'Bug Reports': 'https://github.com/ricksy/python_learning/issues',
         'Source': 'https://github.com/ricksy/python_learning/',
     },
 )

