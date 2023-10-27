import pandas as pd
#df = pd.read_json('us10trial_jso.json')
df = pd.read_json ('/Users/I347708/Desktop/OFB/us10trial_jso.json')

df1= df.loc[df['type'].isin(['OFFBOARDING'])]
df2= df1.sort_values(by='createdAt', ascending=False)
new_df = df2.loc[:, ['id','name','tenantId','status','maxRetry','executionCount','context']]
#new_df.to_csv('offboarding_pending.csv')

pvtlist = df.pivot_table(index=['context'], aggfunc='size')
print(pvtlist)
#pvtlist.to_csv('context_csv.csv')
