
# Elevator project_py
'''
# 엘리베이터 객체 구성
class Elevator = {
    limit: 엘리베이터 정원 (코드 1차 작업후 구현)
    condition: 엘리베이터 상태(상승, 하강)
    elevator: [] _내부 탑승자 리스트
    location: 엘리베이터의 위치 (default : 1)

    ente : [] _탑승층 리스트
    oute : [] _목적층 리스트

    # 리스트 추가 예정
}
el = Elevator()

# 전체 코드 간략 정리
    1. 탑승 인원 전체정보를 한번에 입력 받음
    2. el.condition = "up"상태일때 처리할 인원은 처리
    3. 처리할 인원 제외 나머지 인원은 보류 및 최고층 이동
    4. 최고층에서 탑승 인원수용 후, down상태에서 나머지 인원 처리

# 부가설명
    1. 입력은 “탑승층/목적층“형식으로 받음.
    2. 각각 탑승층과 목적층은 class Elevator에서 정의한 el.ente와 el.oute에 각각 append함
    3. el.limit = 16 으로 정의 하되, 추후 고려
    4. el.condition = None (출력단계에서 사용)
    5. 각각의 인원에는 입력받은 순서대로 index값을 부여함 (출력단계에서 사용, 시간측정에도 사용)
    6. el.condition = "stop" 상태는 이번 소스코드에서는 생각하지 않음

# 상세 설명
1. 엘리베이터가 1층에서 상승한다.
    1. ente < oute를 만족하는 인원을 모두 탑승시킨다.
    2. ente > oute를 만족하는 인원 중에서, ente 값이 가장 큰 사람을 제외하고 나머지 인원은 보류.
    3. ente의 최댓값까지 상승함. (el.location == oute[x]를 만족시킬때마다 oute에서 해당값을 없앤다.)
2. 엘리베이터의 ente 최댓값 위치 도달.
    1. ente 최댓값을 만족시키는 인원을 모두 탑승시킴. (el.location == oute[x]를 만족시킬때마다 oute에서 해당값을 없앤다.)
3. 엘리베이터가 {ente최댓값}층에서 하강한다.
    1. ente > oute를 만족하는 남은 인원을 모두 하강중에 처리함.
    2. el.ente 와 el.oute 리스트가 비어있으면 엘리베이터 운행을 종료
4. 리스트 정리 및 결과 출력,
    1. # 추후 입력


'''

class Elevator:
    limit : 16
    order_up = []
    order_down = []

    ent = []
    out = []

    ente = []
    oute = []

    elevator = 0
    condition = None
    location = 1

from time import sleep
el = Elevator()
e_t = 0
o_t = 0
print("--------------------------------------------")
while True:
    order = input("탑승하려는층/내리려는층(끝내려면 'end'입력) : ")
    if(order=='end'):
        break
    else:
          order = order.split("/")
          el.ente.append(int(order[0]))
          el.oute.append(int(order[1]))

print("탑승 목록 : ",el.ente)
print("목적지 목록 : ",el.oute)

el.ente.sort()
el.oute.sort(reverse=True)

def run_elevator():
    def el_up():
        for ak in range(el.location, el.ente[0]):
            e_t += 1
            up_status = f"현재 위치 : {ak}층"
            sleep(1)
            print(up_status,end="\r")
        el.condition = "stop"
        el.location = el.ente[0]

    def el_down():
        for ak in range(el.location, el.ente[0]):
            e_t += 1
            down_status = f"현재 위치 : {ak}층"
            sleep(1)
            print(down_status,end="\r")
        el.condition = "stop"
        el.location = el.ente[0]

    while True:
        if(el.ente[0]>el.location):
            el.condition = "up"

        if(el.ente[0]<el.location):
            el.condition = "down"
        else:
            el.elevator = el.elevator + 1
            el.ente.pop[0]
            if(el.ente[0]>el.location):
                el.condition = "up"
                el.location = el.ente[0]
                el.elevator + 1
                if(el.oute[0]==el.location):
                    el.elevator = el.elevator - 1
                else:
                    pass
            if(el.ente[0]<el.location):
                el.condition = "down"
                el.location = el.ente[0]
                

'''
def run_elavator():
    while True:
        def el_up():
            for ak in range(el.location, or_e):
                e_t += 1
                up_status = f"현재 위치 : {ak}층"
                sleep(1)
                print(up_status,end="\r")
            el.condition = "stop"

        def el_down():
            for ak in range(el.location, or_e):
                e_t += 1
                down_status = f"현재 위치 : {ak}층"
                sleep(1)
                print(down_status,end="\r")
            el.condition = "stop"

        if(type(or_e)is int):
            or_e = int(order)
            if(or_e>el.location):
                el.ent.append(or_e)
                el.condition = "up"
                el.elavator = el.elavator + 1

            if(or_e<el.location):
                el.ent.append(or_e)
                el.condition = "down"
                el.elavator = el.elavator + 1


        if(type(or_o)is int):
            or_o = int(order)
            if(or_o>el.location):
                el.out.append(or_o)
                el.condition = "up"
                el.elavator = el.elavator - 1
  
            if(or_o<el.location):
                el.out.append(or_o)
                el.condition = "down"
                el.elavator = el.elavator - 1
 



        else:
            if(order=='end'):
                pass # print()
'''
