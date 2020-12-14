pyarmor obfuscate --recursive --output obfuscate/minst_data_expansion_o src/minst_data_expansion/__init__.py
echo python ./setup.py bdist_wheel --plat-name="win_x86_64" --py-limited-api=cp36
python ./setup.py bdist_wheel
python -m twine upload  dist/*