import pandas as pd
import tabulate

df = pd.read_json ('/Users/I347708/Desktop/OFB/us10trial_jso.json')
df1= df.loc[df['type'].isin(['OFFBOARDING'])]
df2= df1.sort_values(by='createdAt', ascending=False)
new_df = df2.loc[:, ['id','name','tenantId','status','maxRetry','executionCount']]

print(new_df.to_markdown())
