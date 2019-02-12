from setuptools import setup

setup(
    name="Shotty",
    version='0.1',
    author='Kevin Edwards',
    description="SnapshotAlyzer 300000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/kevinedwards/Shotty",
    install_requires=[
         'click',
         'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
    
)
