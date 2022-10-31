from typing import List
import heapq as hp



def init_g()->List[List[int]]:
    """
    this fucntion is used to initialize the graph. Each color is represented as number for convience 
    took 4*4 (n*n) as graph to start with 4 colors (m) 
    """
    graph =  [[1,2,1,1],
         [2,1,1,3],
         [1,2,4,1],
         [2,3,3,3]]
    return graph


def greedy_approach(graph)->dict:
    """
    This function use heap data structure to maintain the highest number of color ,
     so that next color can be taken from thie
    """
    dict = {}

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            val = graph[i][j]
            num = dict.get(graph[i][j],0) + 1
            dict[val]=num
            hp.heapify(list(dict.items()))
    return dict

def first_move(graph)->List[List[int]]:
    """
    In this we are assuming we are moving towards right , i.e. [0][0] to [0] [1] 
    """
    
    graph[0][0] = graph[0][1]
    return graph

def interate_and_replace(graph,heap_val):
    """
    This function will iterate over the graph and replace the next element that is followed
    """
    Keymax = max(zip(heap_val.values(), heap_val.keys()))[1]
# For Max element proceed to move

    for i  in range(len(graph)) :
        for j in range(len(graph)):
            if (graph[i][j] ==1):
                row,col = i,j

    for i  in range(row) :
        for j in range(col):
            graph[i][j] = Keymax
    return graph

def main():
    graph = init_g()
    print(" Original graph Before Move " , graph)
    heap_val = greedy_approach(graph)
    graph = first_move(graph)
    print(" Graph First Move " , graph)
    graph =interate_and_replace(graph,heap_val)
    print(" Graph Second Move " , graph)

if __name__=="__main__":
    main()