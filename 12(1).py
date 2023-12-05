#que 12.1
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Sample Transactions
transactions = [
    ['Milk', 'Onion', 'Nutmeg','Kidney Beans','Eggs','Yougurt'],
    ['Dill', 'Onion', 'Nutmeg','Kidney Beans','Eggs','Yougurt'],
    ['Milk', 'Apple','Kidney Beans','Eggs'],
    ['Milk', 'Unicorn', 'Corn','Kidney Beans','Yougurt'],
    ['Corn', 'Onion', 'Onion','Kidney Beans','Ice cream','Eggs']
]

# Convert transactions to a one-hot encoded DataFrame
te = TransactionEncoder()
one_hot_encoded = te.fit(transactions).transform(transactions)
df = pd.DataFrame(one_hot_encoded, columns=te.columns_)

# Generate frequent itemsets
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display the association rules
print(rules)

