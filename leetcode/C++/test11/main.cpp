#include <iostream>
#include <queue>
#include <string>

using namespace std;
const int c_size=11;

struct posion
{
    int px,py,bx,by;
    posion(int x, int y, int bx, int by) :px(x), py(y), bx(bx), by(by) {}
};
int state[c_size][c_size][c_size][c_size];
int orders[4][2] = { {0,1},{0,-1},{-1,0},{1,0} };
char map[c_size][c_size];
//void init(){
//for(int i=0;i<c_size;i++)    for(int j=0;j<c_size;j++)    for(int k=0;k<c_size;k++)    for(int l=0;l<c_size;l++)    state[i][j][k][l]=0;}

int person_x,person_y,box_x,box_y,destination_x,destination_y;
int n,m;

bool check(int x,int y){

    return 0<=x<n && 0<=y<m && map[x][y]!='#';
}

//bool check(int x,int y){

//    return ((0<=x<n) && (0<=y<m) && (map[x][y]!='#'));
//}

bool check(int x,int y){
    if(x<0||x>=n ||0>y||y>=m||map[x][y]=='#')
        return false;
    else
        return true;
}
bool check(int x,int y){
    if(x<0||x>=n ||0>y||y>=m||map[x][y]=='#')
        return false;
    else
        return true;
}

int bfs(){
    state[person_x][person_y][box_x][box_y]=1;
    posion pos(person_x,person_y,box_x,box_y);


    queue<posion> queue1;
    queue1.push(pos);
    while(queue1.size()){
        pos = queue1.front();
        queue1.pop();
        if(pos.bx==destination_x && pos.by == destination_y)    return state[pos.px][pos.py][pos.bx][pos.by]-1;

        for(int i=0;i<4;i++){
            int dx = orders[i][0];
            int dy = orders[i][1];
            if(!check(pos.px+dx,pos.py+dy))
                continue;
            if(pos.px+dx==pos.bx && pos.py+dy==pos.by){
                if(!check(pos.bx+dx,pos.by+dy))
                    continue;
                if(state[pos.px+dx][pos.py+dy][pos.bx+dx][pos.by+dy])
                    continue;
                state[pos.px+dx][pos.py+dy][pos.bx+dx][pos.by+dy] = state[pos.px][pos.py][pos.bx][pos.by]+1;
                queue1.push(posion(pos.px+dx,pos.py+dy,pos.bx+dx,pos.by+dy));
            }
            else{
                if(state[pos.px+dx][pos.py+dy][pos.bx][pos.by])
                    continue;
                state[pos.px+dx][pos.py+dy][pos.bx][pos.by] = state[pos.px][pos.py][pos.bx][pos.by]+1;
                queue1.push(posion(pos.px+dx,pos.py+dy,pos.bx,pos.by));
            }

        }
    }
    return -1;

}

int main()
{
//    init();
    scanf("%d%d",&n,&m);
    for (int i = 0; i < n; i++)
        {
            scanf("%s", map[i]);
        }

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++){
            if(map[i][j]=='X'){person_x=i;person_y=j;}
            if(map[i][j]=='@'){destination_x=i;destination_y=j;}
            if(map[i][j]=='*'){box_x=i;box_y=j;}

        }
//    n=3;m=6;
//    map = {{".S#..E"},{".#.0.."},{"......"}};

    cout<<bfs();

}
