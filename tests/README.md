# Tests

The very complex app **must** have tests for a couple reasons:

- best practices example
- I write bad code that breaks in all the ways. I'd prefer to know when my app breaks and not have it break in the middle of a demo because "*this change is low impact and definitely won't affect anything*"

## Running the tests

The tests can be run in two couple ways:

```console
# with the alias defined in Pipfile
pipenv run tests

# by calling pytest using pipenv
pipenv run python -m pytest
```
