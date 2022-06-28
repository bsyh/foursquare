
def make_train():

    import pandas as pd
    train = pd.read_csv('data/train.csv')
    # test = pd.read_csv("data/test.csv")
    # train.info()
    pd.options.display.max_rows,pd.options.display.max_columns = 1000,14

    # print(train.head(20))
    train_shape = train.shape
    country_dic={}
    selected_row_index=[]
    for row_index in range(train_shape[0]):
        this_country = train.loc[row_index].loc["country"]
        if this_country in country_dic:
            if country_dic[this_country]>=1:
                pass
            else:
                country_dic[this_country]+=1
                selected_row_index.append(row_index)
        else:
            country_dic[this_country] = 1
            selected_row_index.append(row_index)
    train_tiny = train.iloc[selected_row_index]
    # print(train_tiny.head())
    train_tiny.to_csv('data/train_tiny_1.csv',index=False)

def make_pairs():
    import pandas as pd
    train = pd.read_csv('data/pairs.csv')
    # test = pd.read_csv("data/test.csv")
    # train.info()
    pd.options.display.max_rows, pd.options.display.max_columns = 1000, 14

    # print(train.head(20))
    train_shape = train.shape

    train_tiny = train.iloc[range(10)]
    # print(train_tiny.head())
    train_tiny.to_csv('data/pairs_tiny_10.csv', index=False)


if __name__ == "__main__":
    make_pairs()