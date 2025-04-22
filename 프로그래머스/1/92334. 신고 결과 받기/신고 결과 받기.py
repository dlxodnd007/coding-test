def solution(id_list, report, k):
    
    st = set()
    for r in report:
        a, b = r.split()
        st.add((a, b))
        
    count = {name : 0 for name in id_list}
    report_set = {name : set() for name in id_list}
    
    for name1, name2, in st:
        report_set[name1].add(name2)
        count[name2] += 1
        
    ans = []
    for name in id_list:
        cnt = 0
        for n in report_set[name]:
            cnt += (count[n] >= k)
        ans.append(cnt)
    
    return ans