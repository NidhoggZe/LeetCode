from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic = {}
        exist = {}
        for word in wordList:
            exist[word] = False
            for i in range(len(word)):
                stats = word[0:i] + '*' + word[i+1:]
                if stats not in dic:
                    dic[stats] = []
                dic[stats].append(word)

        q = deque()
        q.append(beginWord)
        step = 0
        while not len(q) == 0:
            step += 1
            n = len(q)
            for i in range(0, n):
                word = q.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    stats = word[0:i] + '*' + word[i+1:]
                    if stats not in dic:
                        continue
                    for nextword in dic[stats]:
                        if not exist[nextword]:
                            q.append(nextword)
                            exist[nextword] = True

        return 0


Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])