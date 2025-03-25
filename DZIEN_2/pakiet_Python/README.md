Proces zbudowania i publikacji pakietu

1. instalacja: pip install build
2. uruchomienie build: python -m build
3. założenie konta na PyPI: https://pypi.org/account/register/
4. instalacja pakietu twine: pip install twine
5. wysyłka na test PyPI: twine upload --repository testpypi dist/*
6. wysyłka na prawdziwe PyPI: twine upload dist/*
7. instalacja pakietu z PyPI: pip install textutils
