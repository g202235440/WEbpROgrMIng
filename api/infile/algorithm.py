from sqlalchemy.orm import Session
import api.cruds.task as task_crud  # assuming your CRUD functions are in this module

# ROE 계산 함수
def calculate_roe(net_profit: float, equity: float):
    if equity > 0:
        roe = (net_profit / equity) * 100
    else:
        roe = 0
    return roe

# ROA 계산 함수
def calculate_roa(net_profit: float,total_assets: float):
    if total_assets > 0:
        roa = (net_profit / total_assets) * 100
    else:
        roa = 0
    return roa

# D/E 비율 계산 함수
def calculate_de_ratio(total_debt: float, total_equity: float):
    if total_equity > 0:
        de_ratio = total_debt / total_equity
    else:
        de_ratio = 0
    return de_ratio

# 점수 계산 함수
def calculate_score(task):
    """
    주어진 기업의 재무 지표를 바탕으로 점수를 계산합니다.
    점수는 100점 만점으로 계산됩니다.
    """
    score = 0

    # 기준 설정 및 가중치
    roe_threshold = 15
    roa_threshold = 15
    de_ratio_threshold = 0.5

    roe_weight = 0.2
    roa_weight = 0.2
    de_ratio_weight = 0.1

    # ROE 계산
    roe = calculate_roe(task.enpCrtmNpf, task.enpTcptAmt)

    # ROA 계산
    roa = calculate_roa(task.enpCrtmNpf, task.enpTastAmt)

    # D/E 비율 계산
    de_ratio = calculate_de_ratio(task.enpTdbtAmt, task.enpTcptAmt)

    # ROE 점수
    roe_score = min(roe / roe_threshold, 1) * 100
    score += roe_score * roe_weight

    # ROA 점수
    roa_score = min(roa / roa_threshold, 1) * 100
    score += roa_score * roa_weight

    # D/E 비율 점수
    de_ratio_score = (1 - min(de_ratio / de_ratio_threshold, 1)) * 100
    score += de_ratio_score * de_ratio_weight

    return score

# kell 함수 정의
def kell(db: Session):
    # 'done' 상태의 모든 작업 가져오기
    tasks = task_crud.get_tasks_with_done(db)
    
    # 각 작업에 대해 점수 계산
    results = []
    for task in tasks:
        score = calculate_score(task)
        results.append({
            'task_id': task.id,
            'title': task.title,
            'score': score
        })
    
    return results