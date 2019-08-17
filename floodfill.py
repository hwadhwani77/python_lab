def floodFill(image, sr, sc, newColor):
    h, w = len(image), len(image[0])
    visited={}
    pivot = image[sr][sc]

    def explore(i, j):
        if i <0 or j < 0 or i > (h-1) or j > (w-1) or image[i][j] != pivot:
            return

        if(i, j) not in visited:
            visited[(i,j)] = True
            image[i][j] =newColor
        else:
            return 

        explore(i+1,j)
        explore(i-1, j)
        explore(i, j+1)
        explore(i, j-1)
    explore(sr, sc)

    return image

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1 
# newColor = 2
# print(floodFill(image, sr, sc, newColor))

def canVisitAllRooms(rooms):
    visited = set()
    to_visit = [0]

    while to_visit:
        room = to_visit.pop()
        if room in visited: continue
        visited.add(room)
        to_visit.extend(rooms[room])
    return len(visited) == len(rooms)

print(canVisitAllRooms([[1],[2],[3],[]]))