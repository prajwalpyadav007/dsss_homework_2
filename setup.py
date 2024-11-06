from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # List dependencies here if any

    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"
        ]
    },
    author="Prajwal",
    description="A simple math quiz game",
    license="Apache License 2.0",
    keywords="math quiz game",
    url="https://github.com/prajwalpyadav007/dsss_homework_2.git",
)