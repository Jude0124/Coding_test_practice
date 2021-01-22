import re
import pandas as pd
def solution(files):
    
    Head,Number = [],[]
    for i in range(len(files)):
        Head.append(re.match(r"\D+",files[i]).group().upper())
        Number.append(int(re.search(r"\d{1,5}",files[i]).group()))
        
    df = pd.DataFrame()
    df["Filename"],df["HEAD"],df["NUMBER"]= [i for i in files],Head,Number    
    df = df.sort_values(by=["HEAD","NUMBER"])  
    return [files[i] for i in list(df.index)]

# dataframe 사용하지 않고 sorted 만 이용하기
def solution2(files):
    a = sorted(files, key = lambda file : int(re.findall(r'\d+', file)[0]))
    return sorted(a, key = lambda file : re.split(r'\d+', file.lower())[0])