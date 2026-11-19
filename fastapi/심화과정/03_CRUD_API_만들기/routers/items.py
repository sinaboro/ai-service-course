# items.py : APIRouter 로 나눈 /items 주소 모음 — 직접 실행하지 않고 ex02_main.py 가 불러 써요
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/items", tags=["items"])     # 이 파일의 주소는 모두 /items 로 시작

# 라우터에 붙인 함수들은 ex02_main.py 의 app 에 include_router 로 연결돼요
ITEMS = {1: {"name": "노트북", "price": 1200000}, 2: {"name": "마우스", "price": 15000}}


# "" = prefix 그대로 → GET /items
@router.get("", summary="상품 목록")
def list_items():
    # {"id": k, **v}: id 를 넣고, v(상품 정보 딕셔너리)의 키 · 값을 그대로 펼쳐 넣은 새 딕셔너리
    return [{"id": k, **v} for k, v in ITEMS.items()]


@router.get("/{item_id}", summary="상품 하나")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(404, "상품이 없어요")
    return {"id": item_id, **ITEMS[item_id]}            # id + 상품 정보를 펼쳐 한 딕셔너리로
