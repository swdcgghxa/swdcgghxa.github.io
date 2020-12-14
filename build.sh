#!/bin/bash
echo ======== pyarmor obfuscate ========
sleep 1s
pyarmor obfuscate --recursive --output obfuscate/minst_data_expansion_o src/minst_data_expansion/__init__.py
echo ======== setup -sdist and bdist_wheel ========
sleep 1s
python ./setup.py bdist_wheel #--plat-name="linux_x86_64" --py-limited-api=cp36