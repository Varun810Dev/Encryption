from setuptools import setup, find_packages

setup(
    name="varcrypt",
    version="2.0.0",
    author="Varun810Dev",
    description="Super Unicode Encryption & Decryption Tool with colorful CLI and file support",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'varcrypt=varcrypt.main:run',
        ],
    },
    python_requires='>=3.7',
)