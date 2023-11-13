import pandas as pd

# output.csv 파일 읽기
file='F:\프로젝트\초고주파레이더\data0913\913merged_csv.csv'
df = pd.read_csv(file)

# 'repeated_tired_average', 그리고 'number' 열 값에 따라 정렬
df_sorted = df.sort_values(by=['repeated_tired_average', 'number'])

# output_merge.csv 파일로 저장
df_sorted.to_csv('F:\프로젝트\초고주파레이더\data0913\output_merge.csv', index=False)