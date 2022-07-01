from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def bfs(image, sr, sc, newColor):
            q = deque()
            q.append((sr, sc))
            ori = image[sr][sc]

            visited = [[False] * len(image[0]) for i in range(len(image))]

            while len(q) > 0:
                r, c = q.pop()
                image[r][c] = newColor
                visited[r][c] = True

                if 0 <= r-1 < len(image) and image[r - 1][c] == ori and not visited[r - 1][c]:
                    q.append((r-1, c))

                if 0 <= r+1 < len(image) and image[r + 1][c] == ori and not visited[r + 1][c]:
                    q.append((r+1, c))

                if 0 <= c-1 < len(image[0]) and image[r][c - 1] == ori and not visited[r][c - 1]:
                    q.append((r, c-1))

                if 0 <= c+1 < len(image[0]) and image[r][c + 1] == ori and not visited[r][c + 1]:
                    q.append((r, c+1))

        bfs(image, sr, sc, newColor)
        return image