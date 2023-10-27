import pandas as pd
import tabulate
#import os

#df = pd.read_json('us10trial_jso.json')
df = pd.read_json ('/Users/I347708/Desktop/OFB/us10trial_jso.json')

df1= df.loc[df['type'].isin(['OFFBOARDING'])]
df2= df1.sort_values(by='createdAt', ascending=False)
new_df = df2.loc[:, ['id','name','tenantId','status','maxRetry','executionCount','context']]
#new_df.to_csv('offboarding_pending.csv')

print(tabulate(new_df)

#pvtlist = df.pivot_table(index=['context'], aggfunc='size')
#print(new_df)
#pvtlist.to_csv('context_csv.csv')

#os.remove('offboarding_pending.csv'
