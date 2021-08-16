# How to contribute

## Communication

- Issues: [GitHub](https://github.com/authzed/authzed-py/issues)
- Email: [Google Groups](https://groups.google.com/g/authzed-oss)
- Discord: [Zanzibar Discord](https://discord.gg/jTysUaxXzM)

All communication must follow our [Code of Conduct].

[Code of Conduct]: CODE-OF-CONDUCT.md

## Creating issues

If any part of the project has a bug or documentation mistakes, please let us know by opening an issue.
All bugs and mistakes are considered very seriously, regardless of complexity.

Before creating an issue, please check that an issue reporting the same problem does not already exist.
To make the issue accurate and easy to understand, please try to create issues that are:

- Unique -- do not duplicate existing bug report.
  Deuplicate bug reports will be closed.
- Specific -- include as much details as possible: which version, what environment, what configuration, etc.
- Reproducible -- include the steps to reproduce the problem.
  Some issues might be hard to reproduce, so please do your best to include the steps that might lead to the problem.
- Isolated -- try to isolate and reproduce the bug with minimum dependencies.
  It would significantly slow down the speed to fix a bug if too many dependencies are involved in a bug report.
  Debugging external systems that rely on this project is out of scope, but guidance or help using the project itself is fine.
- Scoped -- one bug per report.
  Do not follow up with another bug inside one report.

It may be worthwhile to read [Elika Etemad’s article on filing good bug reports][filing-good-bugs] before creating a bug report.

Maintainers might ask for further information to resolve an issue.

[filing-good-bugs]: http://fantasai.inkedblade.net/style/talks/filing-good-bugs/

## Contribution flow

This is a rough outline of what a contributor's workflow looks like:

- Create an issue
- Fork the project
- Create a branch from where to base the contribution -- this is almost always `main`
- Push changes into a branch of your fork
- Submit a pull request
- Respond to feedback from project maintainers

Creating new issues is one of the best ways to contribute.
You have no obligation to offer a solution or code to fix an issue that you open.
If you do decide to try and contribute something, please submit an issue first so that a discussion can occur to avoid any wasted efforts.

## Legal requirements

In order to protect both you and ourselves, all commits will require an explicit sign-off that acknowledges the [DCO].

Sign-off commits end with the following line:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

This can be done by using the `--signoff` (or `-s` for short) git flag to append this automatically to your commit message.
If you have already authored a commit that is missing the signed-off, you can amend or rebase your commits and force push them to GitHub.

[DCO]: /DCO

## Common tasks

### Adding and updating dependencies

This project uses [Poetry] for managing dependencies.
By default, Poetry will create a [virtualenv] for you.
Optionally, we recommend using [pyenv] if you need to manage Python versions as well as virtualenvs.

Adding a new dependency can be done with `poetry add` command:

```sh
poetry add library
```

Updating all dependencies can be done with `poetry update` command:

```sh
poetry update
```

For more instructions, see the [Poetry documentation].

[poetry]: https://python-poetry.org
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[pyenv]: https://github.com/pyenv/pyenv
[poetry documentation]: https://python-poetry.org/docs/cli

### Updating generated Protobuf code

All [Protobuf] code is managed using [buf].
The [shebang] at the top of `buf.gen.yaml` contains the [Buf Registry ref] that will be generated.
You can regenerate the code by executing `buf.gen.yaml`:

[Protobuf]: https://developers.google.com/protocol-buffers/
[buf]: https://docs.buf.build/installation
[shebang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[Buf Registry ref]: https://buf.build/authzed/api/history

```sh
./buf.gen.yaml
```
