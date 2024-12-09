from dotenv import load_dotenv
import pandas as pd
from upbankapi import Client, NotAuthorizedException
from io import StringIO
from os import environ

load_dotenv()
client = Client()
transactions = client.account(environ["UP_ACCOUNT"]).transactions()

f = StringIO("created_at,settled_at,amount,description\n" +
             "\n".join(f"{t.created_at},{t.settled_at},{t.amount},{t.long_description}" for t in transactions))
df = pd.read_csv(f)
with open(environ["OUTPUT"], "w") as outp:
    df.to_html(buf=outp, index=False)
