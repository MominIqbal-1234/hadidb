from setuptools import setup, find_packages



VERSION = '0.1'
DESCRIPTION = "HadiDB is a lightweight, extremely horizontally scalable database written in Python."


# Setting up
setup(
    name="HadiDB",
    version=VERSION,
    author="mominiqbal1234",
    author_email="<mominiqbal1214@gmail.com>",
    description=DESCRIPTION,
    long_description="""
    # HadiDB
    HadiDB is a lightweight, extremely horizontally scalable database written in Python

    # How to install hadidb

    ```python
    pip install hadidb
    ```
    # Documentation
    open Github repository for the WebRaft Python library. The link is included in the package's documentation to provide
    users with access to the source code and additional information about the library.
    <br>
    https://github.com/MominIqbal-1234/hadidb



    Check Our Site : https://mefiz.com/about </br>
    Developed by : Momin Iqbal

    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["django","djangorestframework","PyJWT","fastapi","flask","bottle",'cryptography',"user-agents","django-user-agents"],
    keywords=['webraft','WebRaft''python', 'django', 'jwt', 'jwt for django','create api key','read api key','create token','read token','user agent django','ip info python','user agent python','jwt flask','jwt bottle','jwt fastapi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)