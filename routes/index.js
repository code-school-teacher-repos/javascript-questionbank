
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'JS Question Bank' });
});


module.exports = router;

// "<p>Objective:</p><p>(.*?)</p>"
// (<div id="questionStem"(?s).*?</div>)
// (<div id="questionStem"(?s).*?</div>)|(<div id="mainSlide"(?s).*?</div>)
// (<div id="questionStem"(?s).*?</div>)|(<div id="mainSlide"(?s).*)?(?=<div id="explanationDiv")
// (<div id="questionStem"(?s).*?</div>)|((<div id="explanationDiv"(?s).*)?(?=<div id="growlMessage"))|((<div id="application"(?s).*)?(?=<div id="explanationDiv"))
//
// ((<div id="application"(?s).*)?(?=<div id="explanationDiv"))
// ((<div id="explanationDiv"(?s).*)?(?=<div id="growlMessage"))
// (<div id="questionStem"(?s).*?</div>)
// <p>(SubObjective:</p><p>(.*?))</p>