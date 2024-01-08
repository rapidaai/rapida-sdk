"""
author: prashant.srivastav
"""

import invoke


@invoke.task
def lint(ctx):
    """Run linter."""
    ctx.run("pre-commit run --all-files --show-diff-on-failure")


@invoke.task
def requirements(ctx):
    """Generate requirements.txt"""
    reqs = [
        "pipenv requirements > requirements.txt",
        "pipenv requirements --dev-only > requirements-dev.txt",
    ]
    [ctx.run(req) for req in reqs]


@invoke.task
def test(ctx):
    """Run pytest tests."""
    ctx.run(
        " ".join(
            [
                "pytest",
                "-v",
                "-s",
                "--cov-report term",
                "--cov-report xml",
                "--cov=rapida",
                "--asyncio-mode=auto",
            ],
        ),
    )


@invoke.task
def analyze(ctx):
    """Run mypy."""
    ctx.run(
        " ".join(
            [
                "mypy",
                "rapida",
                "--exclude=artifacts",
                "--ignore-missing-imports",
                "--cache-dir=/dev/null",
            ],
        ),
    )


@invoke.task
def git(ctx):
    """Run to set up git hooks"""
    ctx.run("chmod +x bin/git-commit-hook-setup.sh")
    ctx.run("sh bin/git-commit-hook-setup.sh")
    # pre-commit installed hook for lint
    ctx.run("pre-commit install")


@invoke.task
def setup(ctx):
    # setup git hooks for commit
    git(ctx)
    requirements(ctx)


@invoke.task
def package(ctx):
    """Create the python packages"""
    # generate requirements.txt from pipenv requirements
    requirements(ctx)
    # linting
    lint(ctx)
    # type checking mypy
    # analyze(ctx)
    # packaging
    ctx.run("python setup.py sdist bdist_wheel")
