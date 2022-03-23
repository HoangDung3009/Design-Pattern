import random


class Agent(object):
    def getWeapon(self, weapon): pass

    def mission(self): pass


# Terrorist
class Agent_T(Agent):

    def __init__(self):
        self.__mission = "Plant C4 or defeat CT"
        self.__weapon = ""

    def getWeapon(self, weapon):
        self.__weapon = weapon

    def mission(self):
        print("Agent T: weapon: " + self.__weapon + ", mission: " + self.__mission)


# Counter-Terrorist
class Agent_CT(Agent):
    def __init__(self):
        self.__mission = "Defuse C4 or defeat T"
        self.__weapon = ""

    def getWeapon(self, weapon):
        self.__weapon = weapon

    def mission(self):
        print("Agent CT: weapon: " + self.__weapon + ", mission: " + self.__mission)


class AgentFactory:
    def __init__(self):
        self.__listAgent = {}

    def getAgent(self, agentType):
        agent = Agent()

        if agentType in self.__listAgent:
            agent = self.__listAgent[agentType]
        else:
            if agentType == "terrorist":
                agent = Agent_T()
                self.__listAgent[agentType] = agent
                print("Agent_T Created")
            elif agentType == "counter-terrorist":
                agent = Agent_CT()
                self.__listAgent[agentType] = agent
                print("Agent_CT created")

        return agent


factory = AgentFactory()
agentType = ["terrorist", "counter-terrorist"]
weaponType = ["DE", "M4A1", "AK47", "AWP", "Knife"]
for i in range(10):
    r = random.choice(agentType)
    w = random.choice(weaponType)
    player = factory.getAgent(r)
    player.getWeapon(w)
    player.mission()


