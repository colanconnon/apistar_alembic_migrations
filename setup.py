from setuptools import setup


setup(
    name='apistar_alembic_migrations',
    version='0.0.4',
    license='MIT',
    url="https://github.com/colanconnon/apistar_alembic_migrations",
    description='Alembic migrations for apistar',
    author='Colan Connon',
    author_email='cconnon11@gmail.com',
    packages=['apistar_alembic_migrations'],
    install_requires=[
        'alembic',
        'apistar'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)