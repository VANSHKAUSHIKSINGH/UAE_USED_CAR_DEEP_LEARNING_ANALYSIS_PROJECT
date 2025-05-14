import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT"
AUTHOR_USER_NAME = "VANSHKAUSHIKSINGH"
SRC_REPO = "USED_CAR_PREDICTION"
AUTHOR_EMAIL = "vansh.k0907@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A small python package for CNN app",
    long_description_content = "text/markdown",
    url = f"https://github.com/VANSHKAUSHIKSINGH/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT",
    project_urls = {
        "Bug Tracker": f"https://github.com/VANSHKAUSHIKSINGH/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT/issue",
        
    },
    package_dir=  {"": "src"},
    packages = setuptools.find_packages(where="src")
)