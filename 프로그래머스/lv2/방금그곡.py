def solution(m,l):
    st = []             # 곡정보 가공할 수 있게 분리하여 리스트 저장
    et = []
    nm = []
    mel = []
    for i in l:
        tmp = i.split(",")
        st.append(tmp[0])
        et.append(tmp[1])
        nm.append(tmp[2])
        mel.append(tmp[3])
        
    for j,k in zip(["C#","D#","F#","G#","A#"],["H","I","J","K","L"]):  ## 유사 악보 치환, C# == C 로 인식하는 경우 차단
        m = m.replace(j,k)
        for w,v in enumerate(mel):
            mel[w] = v.replace(j,k)
                               
    for i in range(len(l)):                                                                 ## 재생 시간 기준으로 악보 기반 실제 재생된 음표들로 melody 반환
        et[i] = (int(et[i][0:2])-int(st[i][0:2]))*60 + (int(et[i][3:5])-int(st[i][3:5])) ## 재생시간 저장   
        mel[i] = (et[i]//len(mel[i]))*mel[i] + mel[i][0:(et[i]%len(mel[i]))]
    
    tmp = []
    for k,v in enumerate(mel):
        if m in v:
            tmp.append(k)
    if tmp != []:
        return nm[[k for k in tmp if et[k] == max([et[i] for i in tmp])][0]]  ## 일치하는 노래들중 가장 재생시간이 긴것들에서 제일 첫번째를 return
    
    return "(None)" # 없으면 None 반환