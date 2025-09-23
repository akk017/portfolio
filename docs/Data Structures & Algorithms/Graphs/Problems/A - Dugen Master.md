---
title: A - Dungeon master
icon: fa-file
---

source: [problem-link](https://open.kattis.com/problems/dungeon)

You are trapped in a 3D dungeon and need to find the quickest way out! The dungeon is composed of unit cubes which may or may not be filled with rock. It takes one minute to move one unit north, south, east, west, up or down. You cannot move diagonally and the maze is surrounded by solid rock on all sides.

Is an escape possible? If yes, how long will it take?

#### Sample Input

```
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0
```

#### Sample Output

```
Escaped in 11 minute(s).
Trapped!
```

#### Approach

Use, BFS in 3D Vector to find the shorted path between S and E or As mention in video, it could solved having by each queue for every diminention. We will try to find to out an optimal one based in pros and cons.
s
One unique catch here is that array is given in 3D, so for 2D if there are 4 Vector for Iterating, 3D has 6 Vectors

\begin{pmatrix}
-1 & 0 & 0 \\
+1 & 0 & 0 \\
0 & -1 & 0 \\
0 & +1 & 0 \\
0 & 0 & -1 \\
0 & 0 & +1 \\
\end{pmatrix}


or simpily:

```cpp
constexpr int DX6[] = {-1, 1,  0, 0, 0, 0};
constexpr int DY6[] = { 0, 0, -1, 1, 0, 0};
constexpr int DZ6[] = { 0, 0,  0, 0,-1, 1};
```

Simple BFS with 3D Vectors would solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <utility>
#include <tuple>

using namespace std;

constexpr int DX6[] = {-1, 1,  0, 0, 0, 0};
constexpr int DY6[] = { 0, 0, -1, 1, 0, 0};
constexpr int DZ6[] = { 0, 0,  0, 0,-1, 1};

bool is_inside(int tx, int ty, int tz, int r, int c, int level) {
    if (tx < 0 or ty < 0 or tz < 0) return false;
    if (tx >= r or ty >= c or tz >= level) return false;
    return true;
}

void solve(int level, int r, int c) {
    using pt = tuple<int, int, int>;
    using vc = vector<char>;

    vector<vector<vector<char>>> box(r, vector<vector<char>>(c, vector<char>(level, '.')));
    vector<vector<vector<bool>>> vis(r, vector<vector<bool>>(c, vector<bool>(level)));

    pt start, end;

    for(int z=0;z<level;z++){
        for(int x=0;x<r;x++){
            for(int y=0;y<c;y++){
                char k;
                cin >> k;
                if (k == 'S') start = {x, y, z};
                if (k == 'E') end = {x, y, z};
                box[x][y][z] = k;
            }
        }
    }

    queue<pt> q;
    q.push(start);

    int res = 0;

    while (!q.empty()) {
        int size = q.size();

        while (size--){
            auto [x, y, z] = q.front(); q.pop();
            auto [ex, ey, ez] = end;

            if (x == ex and y == ey && z == ez) {
                cout << "Escaped in " << res << " minute(s)." << endl;
                return;
            }

            for(int k=0;k<6;k++){
                int dx = x + DX6[k];
                int dy = y + DY6[k];
                int dz = z + DZ6[k];

                if (is_inside(dx, dy, dz, r, c, level)){
                    if (box[dx][dy][dz] != '#' and !vis[dx][dy][dz]){
                        q.push({dx, dy, dz});
                        vis[dx][dy][dz] = true;
                    }
                }
            }
        }

        res++;
    }

    cout << "Trapped!" << endl;
}

int main() {
    while(true){
        int level, r, c;
        cin >> level >> r >> c;
        if(!level and !r and !c) break;
        solve(level, r, c);
    }
}
```


`TODO` Write the same approach using queues for each dimension.
