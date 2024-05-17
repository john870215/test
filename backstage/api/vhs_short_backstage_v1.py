from fastapi import APIRouter

router = APIRouter(
    prefix="/vhs/backstage",
    tags=["backstage"],
    responses={400: {"detail": "Not found"}},
)


@router.post("/redeems")
async def add_new_redeem():
    return


@router.get("/redeems")
async def get_all_redeems():
    return
