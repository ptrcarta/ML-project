#! /bin/bash

LIST_DIR='proj_list'
url='https://openreview.net/notes'\
'?invitation=ICLR.cc%2F2019%2FConference%2F-%2FBlind_Submission'\
'&limit=10000&details=replyCount%2Ctags&offset='

OFFSET=0
curl ${url}${OFFSET} >$LIST_DIR/tmp1.json
OFFSET=1000
curl ${url}${OFFSET} >$LIST_DIR/tmp2.json

# merge the two lists in the json together
jq ' .notes | .[]' $LIST_DIR/tmp1.json $LIST_DIR/tmp2.json\
    | jq -s '.' >$LIST_DIR/list.json

#cleanup temp files
rm $LIST_DIR/tmp1.json $LIST_DIR/tmp2.json
