def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    seen = {}
    most_seen_key = []
    most_seen = []
    for i in nums:
        if i in seen:
            seen[i]+=1
            min_seen = min(most_seen)
            if seen[i] >= min_seen:
                if i not in most_seen_key:
                    if len(most_seen) >= k:
                        pop_index = most_seen.index(min_seen)
                        most_seen.pop(pop_index)
                        most_seen_key.pop(pop_index)
                else:
                    pop_index = most_seen_key.index(i)
                    most_seen.pop(pop_index)
                    most_seen_key.pop(pop_index)
                most_seen.append(seen[i])
                most_seen_key.append(i)
        else:
            seen[i]=1
            if i not in most_seen_key and len(most_seen) < k:
                most_seen.append(seen[i])
                most_seen_key.append(i)
    return most_seen_key
print(topKFrequent([2,3,4,1,4,0,4,-1,-2,-1],2))