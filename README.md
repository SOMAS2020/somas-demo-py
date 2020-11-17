## What am I looking at?

The Python MWE.

## Structure

### `clients`
Well, clients.

### `server`
Code for the server

### `common`
Shared stuff, like types and base classes


## Setting up
### Python
- >= 3.8

### Optional but you _should_ have this because the CI will definitely do this
- Install [`mypy`](https://mypy.readthedocs.io/en/stable/getting_started.html)
- Install `mypy` langserver on your editor (hopefully VSCode)

### Running the code
- `make init`
- `make run`

## Thoughts on Python

- `mypy` makes stuff type-safe. Try installing it and breaking some types. If you set up your editor properly to use the language server, it should redline upon save. Otherwise, run `mypy .` (This will be the command run by the C.I.)
- Python modules are known to be wonky (hence the `sys.path.append` stuff at some files requiring imports in parent directories). The workaround is ugly, but fine.
- Honestly, Python is easy to set up and easy to learn (if you don't know it)
- There are problems with coding it with 40+ people, but if the `BaseClient` has strongly enforced types, you shouldn't be able to merge stuff with failing types :-)

