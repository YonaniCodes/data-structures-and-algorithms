# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):
    # Create a graph where each ingredient points to the recipes that depend on it
    graph = defaultdict(list)
    # indegree maps each recipe to the number of ingredients it needs
    indegree = {}
    
    # Build the graph and indegree map
    for i in range(len(recipes)):
        recipe = recipes[i]
        for ing in ingredients[i]:
            graph[ing].append(recipe)
        indegree[recipe] = len(ingredients[i])
    
    # Add all supplies to the queue
    queue = deque(supplies)
    result = []

    while queue:
        item = queue.popleft()
        
        for recipe in graph[item]:
            indegree[recipe] -= 1
            if indegree[recipe] == 0:
                queue.append(recipe)
                result.append(recipe)
    
    return result
