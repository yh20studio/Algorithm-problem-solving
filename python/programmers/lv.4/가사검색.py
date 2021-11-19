# link : https://programmers.co.kr/learn/courses/30/lessons/60060
# Lv : 4, 2020 KAKAO BLIND RECRUITMENT
# Category : Trie(트라이)

# 단어마다 ?라는 prefix 형태가 있으므로 탐색트리인 트라이 구조를 활용한다.
# 이때 시간을 더 줄이기 위한 방법으로 word의 길이마다 트라이 구조를 만들어 주었다.
# 모두 "?" 라면 Trie를 만들면서 word의 개수를 저장해놨던 count를 사용한다.
# 접두사 "?" 라면 word를 거꾸로 Trie 구조를 만든 것에서 search를 시작한다.
# 접미사 "?" 라면 word를 그대로 Trie 구조를 만든 것에서 search를 시작한다.

import sys
sys.setrecursionlimit(100001)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.count = 0
        
class Trie():
    
    def __init__(self):
        self.root = Node(None)
        self.count = 0
       
    def makeTrie(self, word):
        curr_node = self.root
        self.count += 1
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]
            curr_node.count += 1
        curr_node.data = word
        
    def search(self, word, full_length):
        count = 0
        curr_node = self.root
        
        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return count
            
        if curr_node.data != None:
            count += 1
        
        else:
            # 단어가 다 끝났음에도 "?"가 있어서 나머지를 탐색해야할 경우
            if full_length != len(word):
                count += curr_node.count
    
        return count        
        
def solution(words, queries):
    answer = []
    front_trie = {}
    back_trie = {}    
    
    for word in words:
        if len(word) not in front_trie.keys():
            front_trie[len(word)] = Trie()
            back_trie[len(word)] = Trie()
        
        front_trie[len(word)].makeTrie(word)
        back_trie[len(word)].makeTrie(word[::-1])
    
    for query in queries:
        if len(query) not in front_trie:
            answer.append(0)
        
        # 모두 "?"인 경우
        elif query.count('?') == len(query):
            answer.append(front_trie[len(query)].count)
        
        # 접두사 "?"
        elif query[0] == "?":
            cnt = query.count('?')
            back_query = query[::-1]
            answer.append(back_trie[len(back_query)].search(back_query[:len(back_query)- cnt], len(back_query)))
        # 접미사 "?"
        elif query[-1] == "?":
            cnt = query.count('?')
            answer.append(front_trie[len(query)].search(query[:len(query)- cnt], len(query)))
        # "?"가 없는 경우
        else:
            answer.append(front_trie[len(query)].search(query, len(query)))
        
    return answer