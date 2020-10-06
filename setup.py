setup(
    name="testgame-1",
    version="1.0.0",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ivcafe413/testgame1",
    author="Team Unknown",
    author_email="ivcafe413@gmail.com",
    license="MIT",
    classifiers=[],
    packages=["game"],
    include_package_data=True,
    install_requires=[
        "pygame"
    ],
    entry_points={"console_scripts": ["testgame1=game.Runner:main"]}
)
