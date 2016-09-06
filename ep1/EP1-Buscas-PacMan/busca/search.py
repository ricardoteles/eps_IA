"""
----------------------------- EP1 MAC425 ---------------------------------
    Nome: Fabio Eduardo Kaspar        NUSP: 7991166
--------------------------------------------------------------------------
"""

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    visitados = []
    stack = [[(problem.getStartState(),'',0)]]

    while len(stack) != 0:
        last_route = stack.pop() # lista de tuplas
        stateParent = last_route[-1][0] # estado em si

        if problem.isGoalState(stateParent):
            resp = []
            for x in last_route[1:]:
                resp.append(x[1])

            return resp

        if stateParent not in visitados:
            visitados.append(stateParent)
            childsAll = problem.getSuccessors(stateParent)  # lista de tuplas

            for childState in childsAll:
                route_child = last_route[:]
                route_child.append(childState)
                stack.append(route_child)                    



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    inicio = problem.getStartState()
    resp = []
    
    if not isinstance(problem, searchAgents.CornersProblem):
        problem.visited = []

    while len(problem.visited) < 4:
        visitados = []
        queue = [[(inicio,'',0)]]
       
        while len(queue) != 0:
            last_route = queue.pop(0) # lista de tuplas
            stateParent = last_route[-1][0] # estado em si

            if problem.isGoalState(stateParent):
                for x in last_route[1:]:
                    resp.append(x[1])
                if not isinstance(problem, searchAgents.CornersProblem):
                    return resp
                    
                #print(problem.visited)
                break

            if stateParent not in visitados:
                visitados.append(stateParent)
                childsAll = problem.getSuccessors(stateParent)  # lista de tuplas

                for childState in childsAll:
                    route_child = last_route[:]
                    route_child.append(childState)
                    queue.append(route_child)

        inicio = stateParent
    return resp
    

def iterativeDeepeningSearch(problem):
    """
    Start with depth = 0.
    Search the deepest nodes in the search tree first up to a given depth.
    If solution not found, increment depth limit and start over.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def getKey(lista):
    return lista[0]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    queue_ordered = [[0, (problem.getStartState(),'',0)]]

    while len(queue_ordered) != 0:
        queue_ordered = sorted(queue_ordered, key=getKey)
        last_route = queue_ordered.pop(0) # lista de tuplas
        stateParent = last_route[-1][0] # estado em si

        if problem.isGoalState(stateParent):
            resp = []
            for x in last_route[2:]:
                resp.append(x[1])
            return resp

        if stateParent not in visitados:
            visitados.append(stateParent)
            childsAll = problem.getSuccessors(stateParent)  # lista de tuplas

            for childState in childsAll:
                route_child = last_route[:]
                route_child.append(childState)
                route_child[0] += childState[2]
                queue_ordered.append(route_child)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state_initial = problem.getStartState()
    
    # [ [custoTotal, custoAcumulado, estado_inicial, estadosSucessores ... ], [proximos Caminhos] ...]
    rotas = [ [ heuristic(state_initial, problem), 0, (state_initial,'',0) ] ]
    visitados = []

    while len(rotas) != 0:
        rotas = sorted(rotas, key=getKey)
        rota_candidata = rotas.pop(0)
        stateParent = rota_candidata[-1][0]

        if problem.isGoalState(stateParent):
            resp = []
            for x in rota_candidata[3:]:
                resp.append(x[1])
            return resp

        if stateParent not in visitados:
            visitados.append(stateParent)
            childsAll = problem.getSuccessors(stateParent)  # lista de tuplas

            for childState in childsAll:
                route_child = rota_candidata[:] # copia toda a rota da raiz ao stateParent
                route_child.append(childState) # anexa o estado do filho na rota copiada
                route_child[1] += childState[2] # atualiza custo acumulado
                route_child[0] = route_child[1] + heuristic(childState[0], problem) # atualiza custo total estimado
                rotas.append(route_child) 

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch