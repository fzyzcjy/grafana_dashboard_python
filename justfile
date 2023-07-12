clean:
    rm -rf dist/*

build:
    python3 -m build

upload:
    python3 -m twine upload dist/*

publish_all: clean build upload

