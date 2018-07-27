sphinx-apidoc -f -o %~dp0\docs %~dp0
sphinx-build -b html %~dp0 %~dp0\docs\htmldocs