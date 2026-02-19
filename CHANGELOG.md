<h1 align = "center">CHANGELOG</h1>

<div align = "justify">

All notable changes to this project will be documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [PEP0440](https://peps.python.org/pep-0440/)
styling guide. For full details, see the [commit logs](https://github.com/sharkutilities/pandas-wizard/commits).

## `PEP0440` Styling Guide

<details>
<summary>Click to open <code>PEP0440</code> Styilng Guide</summary>

Packaging for `PyPI` follows the standard PEP0440 styling guide and is implemented by the **`packaging.version.Version`** class. The other
popular versioning scheme is [`semver`](https://semver.org/), but each build has different parts/mapping.
The following table gives a mapping between these two versioning schemes:

<div align = "center">

| `PyPI` Version | `semver` Version |
| :---: | :---: |
| `epoch` | n/a |
| `major` | `major` |
| `minor` | `minor` |
| `micro` | `patch` |
| `pre` | `prerelease` |
| `dev` | `build` |
| `post` | n/a |

</div>

One can use the **`packaging`** version to convert between PyPI to semver and vice-versa. For more information, check
this [link](https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html).

</details>

## Release Note(s)

The release notes are documented, the list of changes to each different release are documented. The `major.minor` patch are indicated
under `h3` tags, while the `micro` and "version identifiers" are listed under `h4` and subsequent headlines.

<details>
<summary>Click to open <code>Legend Guidelines</code> for the Project CHANGELOG.md File</summary>

  * 🎉 - **Major Feature** : something big that was not available before.
  * ✨ - **Feature Enhancement** : a miscellaneous minor improvement of an existing feature.
  * 🛠️ - **Patch/Fix** : something that previously didn’t work as documented – or according to reasonable expectations – should now work.
  * ⚙️ - **Code Efficiency** : an existing feature now may not require as much computation or memory.
  * 💣 - **Code Refactoring** : a breakable change often associated with `major` version bump.

</details>

### Bronze Knuts `v1.0.0` Release

We are pleased to announce the release of **`forexrates v1.0.0`** (code named *Bronze Knuts*, smallest currency in the
wizarding world of Harry Potter). This is the first stable release bringing the following new features to the community.

Foreign exchange rates is a fundamental factor in determining various macroeconomics and financial factors of a country. There
are plenty of API (both paid, freeware) available. The module provides a uniform structure to fetch the data from various
sources making it easy to switch between different vendors with ease without needing to change underlying functions.

  * 🎉 Provide a *unified* structure with inheritence and abstraction to logically bucketize and fetch data from an API.
  * 🎉 An IO submodule which deals with converting data from one data type to another, this is useful so that the module can
    be directly consumed within your system with ease providing flexibility and robust control.

The module is integrated with [aivenio/macrodb `v1.1.1`](https://github.com/aivenio/macrodb/releases/tag/v1.1.1) and CI/CD
pipeline is available that can be used to directly insert into database. The following supported websites are available:

<div align = "center">

| Website Badge | Logger Code |
| :---: | :---: |
| [![ERAPI](https://img.shields.io/badge/ExchangeratesIO-stable-blue?logo=python&style=plastic)](https://exchangeratesapi.io/) | `ERAPI` |

</div>

</div>
