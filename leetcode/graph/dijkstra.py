# dijkstra算法实现，有向图和路由的源点作为函数的输入，最短路径最为输出
def dijkstra(graph,src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src][i]  # 初始化
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance  # 进行距离更新
                    k=d
                    pre=v
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
    return distance,path


def dijkstra_1(graph,src):
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]
    if src in nodes:
        distance = [float('inf')]*(len(nodes))
        distance[src] = 0
    else:
        return None

    path = {src:[]}
    while nodes:
        u = float('inf')
        for i in nodes:
            if distance[i] < u:
                u,u_index = distance[i],i
        nodes.remove(u_index)
        pre = u_index
        for v_index,v_value in enumerate(graph[u_index]):
            if distance[v_index] > distance[u_index] + v_value:
                distance[v_index] = distance[u_index] + v_value

                path[v_index] = [i for i in path[pre]]
                path[v_index].append(v_index)

    return distance,path





if __name__ == '__main__':
    graph_list = [ [0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]

    distance= dijkstra_1(graph_list, 1)  # 查找从源点0开始带其他节点的最短路径
    print(distance)


