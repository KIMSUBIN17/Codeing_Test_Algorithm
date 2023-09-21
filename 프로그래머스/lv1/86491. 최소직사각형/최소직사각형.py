def solution(sizes):
    max_w = 0 
    max_h = 0
    for w,h in sizes:
        #가로,세로 값 중 더 큰 값이 가로가 되게끔 swap
        if w<h:
            w,h = h,w 
        max_w = max(max_w,w)
        max_h = max(max_h,h)
    #가로중에서 가장 큰 값 * 세로중에서 가장 큰 값
    return max_w * max_h


'''
#다른풀이
def solution(sizes):
    answer = 0
    
    sizes = [sorted(size,reverse=True) for size in sizes]
    
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    
    width, height = max(widths), max(heights)
    
    answer = width * height
    
    return answer

'''