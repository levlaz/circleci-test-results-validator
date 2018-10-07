var validator = require('xsd-schema-validator');
var fs = require('fs');
const WORKING_DIR = 'test-results'

fs.readdir(WORKING_DIR, function(err, items) {

    for (var i = 0; i < items.length; i++) {

        console.log("checking: " + items[i])

        validator.validateXML(
            { file: WORKING_DIR + "/" + items[i] },
            'junit.xsd',
            function (err, result) {
                if (err) {
                    throw err;
                }

                result.valid;
            })
    }
})