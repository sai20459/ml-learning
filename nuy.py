import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# df = pd.DataFrame(randn(5,4),["a","b","c","d","e"],["w","x","y","z"])
# conditional
# print(pf[pf > 0])
# return only true values
# print(pf[pf["w"] > 0][["x","y"]]) 
# returns x colums

# print(pf[(pf["w"]>0) & (pf["y"]>1)])
# print(pf[(pf["w"]>0) | (pf["y"]>1)])


# index
# newind = "ca ny wy or co".split()

# pf["states"] = newind
# pf.set_index(newind)
# print(pf)

# outside=["g1","g1","g1","g2","g2","g2"]
# inside=[1,2,3,4,5,6]
# hier_index=list(zip(outside,inside))
# hier_index= pd.MultiIndex.from_tuples(hier_index)
# df =pd.DataFrame(randn(6,2),hier_index,['a',"b"])
# df.index.names = ["group","num"]

# print(df.loc["g2"].loc[5]["b"])
# cross-section
# print(df.xs(1,level="num"))

# fill na && dropna
# d ={"A":[1,2,np.nan],"B":[5,np.nan,np.nan],"C":[1,2,3]}
# df =pd.DataFrame(d)
# print(pd.DataFrame(d).dropna(thresh=1))
# df =pd.DataFrame(d).fillna(value="FILL VALUE")
# print(df["A"].fillna(value=df["A"].mean()))

# data = {"company": ["goog", "goog", "msft", "msft", "fb", "fb"],
#         "person": ["sam", "charles", "amy", "vanessa", "carl", "sarah"],
#         "sales": [220, 120, 340, 124, 324, 350]}

# group by
# print(pd.DataFrame(data).groupby(["company"]).describe())

# join,merge,concat
# df1 = pd.DataFrame(
#     {
#         "A": ["A0", "A1", "A2", "A3"],
#         "B": ["B0", "B1", "B2", "B3"],
#         "C": ["C0", "C1", "C2", "C3"],
#         "D": ["D0", "D1", "D2", "D3"],
#     },
#     index=[0, 1, 2, 3],
# )


# df2 = pd.DataFrame(
#     {
#         "A": ["A4", "A5", "A6", "A7"],
#         "B": ["B4", "B5", "B6", "B7"],
#         "C": ["C4", "C5", "C6", "C7"],
#         "D": ["D4", "D5", "D6", "D7"],
#     },
#     index=[4, 5, 6, 7],
# )


# df3 = pd.DataFrame(
#     {
#         "A": ["A8", "A9", "A10", "A11"],
#         "B": ["B8", "B9", "B10", "B11"],
#         "C": ["C8", "C9", "C10", "C11"],
#         "D": ["D8", "D9", "D10", "D11"],
#     },
#     index=[8, 9, 10, 11],
# )

# print(pd.concat([df1,df2,df3],axis=1))
# print(df1,df2,how="inner",on="key")
# print(df1,df2,how="inner",on=["key1","key2"])
# left.join(right,how="outer")

# print(pd.DataFrame({"col2":[1,2,3,4],"col2":[444,555,666,444],"col3":["abc","def","ghi","xyz"]})["col2"].nunique())
# print(pd.DataFrame({"col2":[1,2,3,4],"col2":[444,555,666,444],"col3":["abc","def","ghi","xyz"]})["col2"].unique())

# df = pd.DataFrame({"col1":[1,2,3,4],"col2":[444,555,666,444],"col3":["abc","def","ghi","xyz"]})
# print(df[(df["col1"]>2) & (df["col2"]==444)])

# def times2(x):
#     return x*2

# print(df["col1"].apply(times2))

# print(df["col2"].apply(lambda x: x*2))
# print(df.drop('col1',axis=1))
# print(df.sort_values(by="col2"))

# print(df.isnull())

# data = {
#    "A": ["foo","bar","foo","bar","foo","bar"],
#    "B": ["one","two","one","two","one","two"],
#    "C": ["X","Y","X","Y","X","Y"],
#    "D":[1,2,3,5,4,1]
# }

# df = pd.DataFrame(data)
# print(df.pivot_table(values="D",index=["A","B"],columns=["C"]))
# df = pd.read_csv("example.csv")
# df.to_csv("my_output",index=False)
# print(pd.read_csv("my_output"))

# df= pd.read_excel("Excel_Sample.xlsx",sheet_name="sheet1")

