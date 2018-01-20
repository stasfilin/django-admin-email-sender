from setuptools import setup, find_packages

setup(
    name='django-admin-email-sender',
    packages=find_packages(),
    package_data={'admin_email_sender': ['templates/*.*']},
    include_package_data=True,
    zip_safe=False,
    version='0.0.1',
    description='Django Admin Email Sender',
    author='https://github.com/stasfilin',
    author_email='stasfilinmusic@gmail.com',
    url='https://github.com/stasfilin/django-admin-email-sender.git',
    download_url='',
    keywords=['django', 'sender', 'django-admin-email-sender', 'admin', 'email'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
)
