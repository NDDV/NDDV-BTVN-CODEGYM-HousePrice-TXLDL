#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('house_price_dống-da.xlsx')
df.info()

#%%
df[:9]
#%%
#Phát hiện các dòng, cột chứa dữ liệu khuyết thiếu
df.isna()

# %%
#Xóa bỏ hết tất cả những dòng dữ liệu không có thông tin về giá
df_price = df.copy()
df_price = df_price[df_price['price'].notna()]
df_price
# %%
df_2 = df.loc[:,['land_certificate','house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor']]
df_2

# %%
#Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu của land_certificate bằng =”không có thông tin”, house_direction, balcony_direction, toilet, bedroom, Floor  bằng giá trị có tần số xuất hiện lớn nhất của các thuộc tính đó,
df_2['land_certificate'].fillna('không có thông tin', inplace=True)

house_direction = df_2['house_direction'].value_counts().idxmax()
df_2['house_direction'].fillna(house_direction, inplace=True)

balcony_direction = df_2['balcony_direction'].value_counts().idxmax()
df_2['balcony_direction'].fillna(balcony_direction, inplace=True)

toilet = df_2['toilet'].value_counts().idxmax()
df_2['toilet'].fillna(toilet, inplace=True)

bedroom = df_2['bedroom'].value_counts().idxmax()
df_2['bedroom'].fillna(bedroom, inplace=True)

floor = df_2['floor'].value_counts().idxmax()
df_2['floor'].fillna(floor, inplace=True)

df_2
# %%
#Lọc thông tin những bất động sản ở trong ngõ thành bộ dữ liệu nhà ngõ
df_nhango = df[df['type_of_land']=='Đất thổ cư']
df_nhango
# %%
#Tính toán giá/m2  ( đơn vị triệu/m2) với loại hình nhà ngõ
df_nhango['giá/m2'] = df_nhango['price']/df_nhango['area']
df_nhango

#%%
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
# %%
import seaborn as sns  # import thư viện seaborn để vẽ biểu đồ
sns.boxplot(x=df['area'])
# %%
df['giá/m2'] = df['price']/df['area']
sns.boxplot(x=df['area'])


#%%
from sklearn.preprocessing import MinMaxScaler
#chuẩn hóa dữ liệu với phương pháp Min-Max Scaling
sns.kdeplot(data=df['giá/m2'])

# %%
scaler = MinMaxScaler()
df_s = scaler.fit_transform(df['giá/m2'])

df_s = pd.DataFrame(df_s)
#%%
sns.kdeplot(data=df_s)