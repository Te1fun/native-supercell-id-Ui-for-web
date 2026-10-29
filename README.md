# Supercell ID UI

my try at recreating the supercell id signup + profile ui. i wanted it to look as close to the original as possible (layout, colors, icons, animations, sounds). its just one html file, no framework or anything

theres no backend so the email and code only get checked for format, nothing gets sent

## files

- `supercell-id.html` - the whole thing
- `build_assets.py` - script that gets the images and sounds ready
- `assets/` - not in the repo, you make it yourself

## setup

the images and sounds are from supercell so i cant upload them. you need a folder with the hashed files and the `AssetManifest.json`. the script reads the manifest and renames every file to its real name

```
python build_assets.py <folder_with_hash_files> AssetManifest.json assets
```

only needs python 3. it doesnt print anything, if a file is missing it just skips it so check the assets folder after

then open `supercell-id.html`. if the sounds dont play use

```
python -m http.server 8000
```

and go to `localhost:8000/supercell-id.html`

## notes

- missing images are just left out, page still works
- sounds can be turned off with `SOUND=false` in the script
- english and spanish

not affiliated with supercell, everything belongs to them. dont upload their assets to your fork
