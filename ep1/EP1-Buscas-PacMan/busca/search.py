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
    coordAtual = problem.getStartState()
    rotas = [ [(problem.getStartState(),'',0)] ]
    visitados = []

    while not problem.isGoalState(coordAtual):                     
        caminho = rotas.pop(0)
        coordAtual = caminho[-1][0]

        if coordAtual not in visitados:                            
            novasRotas = []
            visitados.append(coordAtual)

            vizinhos = problem.getSuccessors(coordAtual)

            for x in vizinhos:     
                novoCaminho = caminho[:]
                novoCaminho.append(x)

                novasRotas.append(novoCaminho)                     

            rotas = novasRotas + rotas

    resp = []
    custo = 0

    for tuplas in caminho[1:]:
        resp.append(tuplas[1])
        custo += tuplas[2]

    raw_input("Aperte a tecla")
    return resp
    
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    coordAtual = problem.getStartState()
    rotas = [[(problem.getStartState(),'',0)]]
    visitados = []

    while not problem.isGoalState(coordAtual):                     
        caminho = rotas.pop(0)
        coordAtual = caminho[-1][0]

        if coordAtual not in visitados:                            
            novasRotas = []
            visitados.append(coordAtual)

            vizinhos = problem.getSuccessors(coordAtual)

            for x in vizinhos:     
                novoCaminho = caminho[:]
                novoCaminho.append(x)

                novasRotas.append(novoCaminho)                     

            rotas =  rotas+novasRotas

    resp = []
    custo = 0

    for tuplas in caminho[1:]:
        resp.append(tuplas[1])
        custo += tuplas[2]

    raw_input("Aperte a tecla")
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

# Funcao auxiliar para ordenar a lista pelo custo
def getKey(rotas):
    return rotas[0]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    coordAtual = problem.getStartState()
    rotas = [[0, (problem.getStartState(),'',0)]]       # primeiro elem eh o custo
    visitados = []

    while not problem.isGoalState(coordAtual):                     
        rotas = sorted(rotas, key=getKey)
        caminho = rotas.pop(0)
        coordAtual = caminho[-1][0]

        if coordAtual not in visitados:                            
            novasRotas = []
            visitados.append(coordAtual)

            vizinhos = problem.getSuccessors(coordAtual)

            for x in vizinhos:     
                novoCaminho = caminho[:]    
                novoCaminho.append(x)
                novoCaminho[0] += novoCaminho[-1][2]
                novasRotas.append(novoCaminho)                     
            
            rotas =  novasRotas+rotas

    resp = []
    custo = 0

    for tuplas in caminho[2:]:
        resp.append(tuplas[1])
        custo += tuplas[2]

    raw_input("Aperte a tecla")
    return resp    


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    coordAtual = problem.getStartState()
    rotas = [[0, (problem.getStartState(),'',0)]]       # primeiro elem eh o custo
    visitados = []

    while not problem.isGoalState(coordAtual):                     
        rotas = sorted(rotas, key=getKey)
        caminho = rotas.pop(0)
        coordAtual = caminho[-1][0]

        if coordAtual not in visitados:                            
            novasRotas = []
            visitados.append(coordAtual)

            vizinhos = problem.getSuccessors(coordAtual)

            for x in vizinhos:     
                novoCaminho = caminho[:]    
                novoCaminho.append(x)
                novoCaminho[0] += (novoCaminho[-1][2]+manhattanDistance(coordAtual, (1,1)))
                novasRotas.append(novoCaminho)                     
            
            rotas =  novasRotas+rotas

    resp = []
    custo = 0

    for tuplas in caminho[2:]:
        resp.append(tuplas[1])
        custo += tuplas[2]

    raw_input("Aperte a tecla")
    return resp

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch