from setuptools import setup

setup(
    name='OBTTestTask',
    version='0.1.0.dev1',
    packages=['TestTask', 'TestTask.app', 'TestTask.app.migrations', 'TestTask.TestTask'],
    url='https://github.com/MrKobrand/OBTTestTask/tree/develop',
    license='',
    author='Alexander Rublev',
    author_email='aarvlg@mail.ru',
    description='Test task for applicants for the vacancy of a '
                'Python developer at Open Business Technologies (Volgograd)',
    install_requires=['django==2.2', 'm3-django-compat==1.9.2', 'm3-objectpack==2.2.47'],
    project_urls={
        'Source': 'https://github.com/MrKobrand/OBTTestTask/tree/develop',
        'Tracking': 'https://github.com/MrKobrand/OBTTestTask/issues',
    },
    python_requires='>=3',
    classifiers=[
        'Development Status :: 2 - Development',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='m3 bars objectpack django development'
)
