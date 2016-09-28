# cqa-analysis

<h3>DATA</h3>
Data is too large for github to store, please download from google drive, following the link below

https://drive.google.com/open?id=0BxDbPR2yNrupTmQyX0JZX3lsNms

<h3>API description</h3>

* all questions under the same tage：http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name=[name]&limit=[limit]
  # [name] tage name
* question content：http://apis.guokr.com/ask/question/[qid].json
  # [qid] question id
* answer content：http://apis.guokr.com/ask/answer/[aid].json
  # [aid] answer id
* all answers for one question：http://apis.guokr.com/ask/answer.json?retrieve_type=by_question&question_id=[qid]&limit=[limit]
* all questiones by one user：http://apis.guokr.com/ask/question.json?retrieve_type=by_user&ukey=[ukey]&limit=[limit]
  # [ukey] user id
* all answers by one user：http://apis.guokr.com/ask/answer.json?retrieve_type=by_user&ukey=[ukey]&limit=[limit]
* all supporters for one answer: http://www.guokr.com/apis/ask/answer_supporting.json?retrieve_type=by_answer&answer_id=[aid]&limit=[limit]



<h3>Setup</h3>

Operating System: Ubuntu 16.04

package grey_harvest installation guidance:

terminal commandline code:

1. sudo apt-get install build-essential libssl-dev libffi-dev python-dev
2. pip install cryptography
3. sudo apt-get install libxml2-dev libxslt1-dev
4. pip install grey_harvest

