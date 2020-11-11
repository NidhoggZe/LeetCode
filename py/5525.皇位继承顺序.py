from typing import List


class ThroneInheritance:
    genealogy = {}
    kingName = ""

    class man:
        def __init__(self, name: str, parent):
            self.name = name
            self.parent = parent
            self.live = True
            self.children = []

    def __init__(self, kingName: str):
        ThroneInheritance.kingName = kingName
        ThroneInheritance.genealogy[kingName] = self.man(kingName, None)

    def birth(self, parentName: str, childName: str) -> None:
        parent = ThroneInheritance.genealogy[parentName]
        child = self.man(childName, parent)
        parent.children.append(child)
        ThroneInheritance.genealogy[childName] = child

    def death(self, name: str) -> None:
        ThroneInheritance.genealogy[name].live = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(res, curman):
            if curman.live:
                res.append(curman.name)
            for i in curman.children:
                dfs(res, i)
        res = []
        dfs(res, ThroneInheritance.genealogy[ThroneInheritance.kingName])
        return res


a = ThroneInheritance("king")
a.birth("king", "logan")
a.birth("king", "hosea")
a.birth("logan", "leonard")
a.birth("king", "carl")
a.birth("carl", "ronda")
print(a.getInheritanceOrder())

