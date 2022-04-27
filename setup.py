import setuptools

from gupshup import __version__

test_dependencies = ["aiosqlite", "sqlalchemy", "asyncpg"]

setuptools.setup(
    name="mautrix",
    version=__version__,
    url="https://github.com/bramenn/gupshup-io",

    author="Alejandro Herrera",
    author_email="bramendev@gmail.com",

    description="An asynchronous client/server for gupshup.",

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3,<4",
    ],
    extras_require={
        "lint": ["black==22.1.0", "isort"],
        "test": ["pytest", "pytest-asyncio"],
    },
    python_requires="~=3.8",

)