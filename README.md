# Heavy Uploader
Python script for uploading and managing content on the Heavy Cloud Service (https://enzienaudio.com)

### Installing

`$ pip install hv-uploader`

### Upgrading

`$ pip install hv-uploader -U`

(Note: this will also update any dependencies)

---
## Development

### Creating and uploading new package version

`$ pip install twine`

`$ rm -rf ./dist/`

`$ python setup.py sdist bdist_wheel`

`$ twine upload dist/* `
