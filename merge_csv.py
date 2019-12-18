import pandas as pd

# merged_primary = pd.read_csv("merged_primary.csv", delimiter=',', encoding="euc-kr")
# modeling_data = pd.read_csv("modeling_data.csv", delimiter=',', encoding="euc-kr")
# merged_primary.drop(['Unnamed: 0'], axis=1, inplace=True)
#
# merged_primary['위도경도'] = 0
# for i in range(len(merged_primary)):
#     merged_primary['위도경도'].loc[i] =str(merged_primary['위도'].loc[i]) +str(merged_primary['경도'].loc[i])
#
# modeling_data['위도경도'] = 0
# for i in range(len(modeling_data)):
#     modeling_data['위도경도'].loc[i] =str(modeling_data['위도'].loc[i]) +str(modeling_data['경도'].loc[i])
#
# merged_data = pd.merge(merged_primary, modeling_data, how='left', on='위도경도')
# print(merged_data)
# merged_data.to_csv("aa.csv", encoding="euc-kr",index=False)

# merge_data = pd.read_csv("aa.csv", encoding="euc-kr" )
# uniq = merge_data['위도경도'].unique()
# print(len(uniq))
#
# result_data = pd.DataFrame()
# for uni in uniq:
#     data = merge_data[merge_data['위도경도'] == uni]
#     if len(data) > 1:
#         sort_data = data.sort_values(['상태_x'], ascending=True)
#         sort_data_uniq = sort_data['학교명'].unique()
#         if len(sort_data_uniq) == 1:
#             result_data = pd.concat([result_data, sort_data.tail(1)], axis=0)
#     else:
#         result_data = pd.concat([result_data, data], axis=0)
#
# result_data.to_csv("bb.csv", encoding="euc-kr",index=False)

# merge_data2 = pd.read_csv("bb.csv", encoding="euc-kr" )
# sido_uniq = merge_data2['시도'].unique()
#
# si = pd.DataFrame()
#
# sido_list = []
# num_school = []
# num_open = []
#
# for idx, sido in enumerate(sido_uniq):
#     print(idx, sido)
#     sido_list.append(sido)
#     tmp_sido_data = merge_data2[merge_data2['시도'] == sido]
#     num_school.append(len(tmp_sido_data))
#     num_open.append(tmp_sido_data['상태_x'].value_counts().to_list()[0])
#
# si['시도'] = sido_list
# si['총학교수'] = num_school
# si['개교수'] = num_open
#
# si.to_csv("sido_school.csv", encoding="euc-kr", index=False)
import json
with open("save_sido.json", encoding="UTF-8") as f:
    Loc = json.load(f)
    print("H")