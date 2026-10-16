from typing import TypedDict
from langgraph.graph import StateGraph, START, END
#1. state 정의 처음부터 끝까지 변하는 값을 저장하고 있다.
class AgentState(TypedDict):
    value: list[int]
    name : str
    result : int
#2. Node 정의
def first_node(state:AgentState) -> dict:
    total = sum(state['value'])
    return {'result' : total}
#3. 그래프 정의
build = StateGraph(AgentState)
build.add_node("first_node", first_node)
build.add_edge(START, "first_node")
build.add_edge("first_node", END)
#4. 그래프 컴파일 & 실행
# build.compile()
graph = build.compile()