#!/bin/bash
echo ======== pyarmor obfuscate ========
sleep 1s
pyarmor obfuscate --recursive --output obfuscate/minst_data_expansion_o src/minst_data_expansion/__init__.py
echo ======== setup sdist and bdist_wheel ========
sleep 1s
python ./setup.py bdist_wheel #--plat-name="linux_x86_64" --py-limited-api=cp36
echo ======== twine upload ========
sleep 1s
python -m twine upload --skip-existing -u="__token__" -p="pypi-AgEIcHlwaS5vcmcCJGQ5NmVhZTA1LWZmZGMtNDRmNi1iYzRlLTQyMGNjNmUwNDJiMAACR3sicGVybWlzc2lvbnMiOiB7InByb2plY3RzIjogWyJtaW5zdC1kYXRhLWV4cGFuc2lvbi1vIl19LCAidmVyc2lvbiI6IDF9AAAGIFkKE90_tohtTn6qkx7N7vBH-_DJBrDDTuZ9X53EXCfl" dist/*