from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Daily variation of the stock price
# bellow tags indicates:
# had the stock price increased or decreased in the previous day
# 1 = increased, 0 = decreased
# had the stock high negotiation volume in the previous day
# 1 = high, 0 = low
# had the stock price high value when the market was closed
# 1 = high, 0 = low

stock1 = [1, 0, 1]  # AAPL
stock2 = [0, 1, 0]  # GOOGL
stock3 = [1, 1, 1]  # MSFT
stock4 = [0, 0, 1]  # AMZN
stock5 = [1, 1, 0]  # TSLA
stock6 = [0, 1, 1]  # FB

train_data = [stock1, stock2, stock3, stock4, stock5, stock6] 
train_tags = [1, 1, 1, 0, 0, 0]  # 1 = increased, 0 = decreased

#with lenear SVC
model = LinearSVC()
model.fit(train_data, train_tags)

# Test data
new_stock1 = [1, 0, 0]  # AAPL
new_stock2 = [0, 1, 1]  # GOOGL
new_stock3 = [1, 1, 0]  # MSFT

train_test = [new_stock1, new_stock2, new_stock3]
real_tags = [1, 0, 1]  # 1 = increased, 0 = decreased
predictions = model.predict(train_test)

#eavluate the model
accuracy = accuracy_score(real_tags, predictions)
print("accuracy rate %.2f%%" % (accuracy * 100))
