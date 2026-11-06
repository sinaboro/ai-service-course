from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/items", tags=["items"])     # 이 파일의 주소는 모두 /items 로 시작

# 라우터에 붙인 함수들은 ex02_main.py 의 app 에 include_router 로 연결돼요
ITEMS = {1: {"name": "노트북", "price": 1200000}, 2: {"name": "마우스", "price": 15000}}


# "" = prefix 그대로 → GET /items
@router.get("", summary="상품 목록")
def list_items():
    return [{"id": k, **v} for k, v in ITEMS.items()]


@router.get("/{item_id}", summary="상품 하나")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(404, "상품이 없어요")
    return {"id": item_id, **ITEMS[item_id]}
