# Dead_Link_Checker

## Contributing

### [Dead Link Checker (Release 0.1)](https://github.com/sonechca/Dead_Link_Checker)

## How to contribute

- 1 : Fork Dead Link Checker repository
- 2 : Clone the repository: "git clone https://github.com/sonechca/Dead_Link_Checker.git"
- 3 : Create a branch for your working that fix bug or improve DLChecker
- 4 : Install requirement libraries. Check [README](https://github.com/sonechca/Dead_Link_Checker/blob/master/README.md)
- 4 : Create a Pull Request: "git push origin 'new branch name'"

## Formatting

[Python Black](https://pypi.org/project/black/): This tool need to use this source formatter

Require Library:
'''bash
pip install black
'''
One-Step command:

```bash
bash format.sh
```

The program has Visual Studio Code integration, saving the file with automatically run the formatter on link-check.py

## Linting

[Flake8](https://flake8.pycqa.org/en/latest/index.html): This tool need to use this Linter.

Require Library:
'''bash
pip install flake8
'''

One-Step command:

```bash
bash linter.sh
```

## Editor/IDE Integration

You can check the [settings.json](https://github.com/sonechca/Dead_Link_Checker/blob/master/.vscode/settings.json)
It will show you the list of what I provide a way to integrate them into our editor or IDE so that we get the benefits while we are writing code

## Test Tool

Dead Link Check use testing framework "Pytest". You can contribute to add test more based on "file" or "link". Test files are in Tests folder You can test after creating your test. CI will check the your Pull Request before I merged your PR.
You need to install pytest typing below:

```bash
pip install pytest
```

Before Pull Request, you need to check your test. Pytest will check your file have error or not
command below:

```bash
pytest file_name
```
