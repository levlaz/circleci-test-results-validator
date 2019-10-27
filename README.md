![CircleCI](https://img.shields.io/circleci/build/github/levlaz/circleci-test-results-validator)
![Docker Automated build](https://img.shields.io/docker/automated/levlaz/circleci-test-results-validator)

# CircleCI Test Results Validator

If you are [uploading test results to CircleCI](https://circleci.com/docs/2.0/language-python/#upload-and-store-test-results) but they are not showing up in the dashboard, then the most common cause is that the xml file that you are uploading to the test results service is not valid Junit Style XML.

This utility can be used to easily validate that the test results that you are uploading to CircleCI are valid Junit XML.

## Usage

On the circle side, make sure you are uploading your test results as an artifact.

### Running with Docker 

The simplest way to to use this tool is to use the pre-built docker container. 

```
docker run -e "CIRCLE_TOKEN=$YOUR_CIRCLECI_API_TOKEN" -e "URL=$YOUR_BUILD_URL" levlaz/circleci-test-results-valdiator
```

### Running Manually 

Right now this is kind of a hodge podge of things.

* Java
* Node
* Python

To install everything do this:

```
npm install
pip install -r requirements.txt
```

1. Make sure you have a valid `$CIRCLE_TOKEN` exported as an environment variable.
2. Run `python validate.py $URL`

Be sure to replace `$URL` with a URL to the build that you want to validate the test results for.
