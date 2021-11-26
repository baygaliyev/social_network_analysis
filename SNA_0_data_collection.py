import json
from stackapi import StackAPI
import pandas as pd
import time

SITE = StackAPI('stackoverflow')
SITE.key = "LO6xVUl4spixRohBvNU6YQ(("
ids = 43100                 # the number can be increased or decreased

ownerdata = []
tagsdata = []
countdata = []
creationdata = []
userdata = []

while ids < 51000:          # the number can be increased or decreased
    try:
        qjson = json.dumps(SITE.fetch('users/{}/questions'.format(ids)))
        time.sleep(10)
        ujson = json.dumps(SITE.fetch('users/{}'.format(ids)))
        time.sleep(10)

        qjsonload = json.loads(qjson)
        ujsonload = json.loads(ujson)

        qitems = qjsonload['items']
        uitems = ujsonload['items']

        for udict in uitems:
            date = udict['creation_date']
            for qdict in qitems:
                tags = qdict['tags']
                owner = qdict['owner']
                viewcount = qdict['view_count']
                creation = qdict['creation_date']

                tagsdata.append(tags)
                ownerdata.append(owner)
                userdata.append(date)
                countdata.append(viewcount)
                creationdata.append(creation)
    except:
        pass
    ids += 100          # the number can be increased or decreased

df0 = pd.DataFrame(ownerdata)
df1 = pd.DataFrame(userdata)
df2 = pd.DataFrame(countdata)
df3 = pd.DataFrame(creationdata)
df4 = pd.DataFrame(tagsdata)

cols = [df0, df1, df2, df3, df4]
full_cols = pd.concat(cols, axis=1, sort=False)
df = pd.DataFrame(full_cols)

# this code writes df to csv

# df.to_csv('sna_data_fullest.csv',  encoding='utf-8')
 
# the code below helps to append new raws to the existing file

with open('sna_data_fullest.csv', 'a') as fd:
    df.to_csv(fd, encoding='utf-8', header=False)
