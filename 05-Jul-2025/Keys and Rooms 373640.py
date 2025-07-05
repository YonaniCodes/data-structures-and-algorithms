# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # keys= set([0])
        # for  index ,room in enumerate (rooms):
        #     if index not in keys:
        #         return False
        #     for key in room:
        #         keys.add(key)
        # return True

        visited=set()
        queue = deque([0])

        while queue:
            #pop the the first element
            room = queue.popleft()

            #if room is visited continue
            if room in visited:
                continue
            # visite the room please
            visited.add(room)

            for key in rooms[room]:
                if key  not in  visited:
                    queue.append(key)
    


        return len(visited)==len(rooms)
                


            
