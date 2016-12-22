"""
Read user agents from list (local file) and select one for the request.
"""
import random

def user_agent_list(user_agent_list_path):
    """Read user agents from list (local file). """
    with open(user_agent_list_path, "r") as f:
        agent_list = f.readlines()
    return agent_list

def select_user_agents(agent_list, n):
    """Select random user agent from pre-loaded list of agents. """
    n_agents = len(agent_list)
    agents = []
    i = 0
    while i < n:
        agents.append(agent_list[random.randint(0, n_agents-1)].replace("\n", "").replace("\"", ""))
        i += 1
    return agents
