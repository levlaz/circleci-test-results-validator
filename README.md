# CircleCI Test Results Validator

If you are [uploading test results to CircleCI](https://circleci.com/docs/2.0/language-python/#upload-and-store-test-results) but they are not showing up in the dashboard, then the most common cause is that the xml file that you are uploading to the test results service is not valid Junit Style XML.

This utility can be used to easily validate that the test results that you are uploading to CircleCI are valid Junit XML.

## Usage

### Requirements

Right now this is kind of a hodge podge of things.

* Java
* Node
* Python

To install everything do this:

```
npm install
pipenv install
```

On the circle side, make sure you are uploading your test results as an artifact.

### Running the Validator

First get into a `pipenv shell`

1. Make sure you have a valid `$CIRCLE_TOKEN` exported as an environment variable.
2. Run python get_test_results.py `$URL`

Be sure to replace `$URL` with a URL to the build that you want to validate the test results for.