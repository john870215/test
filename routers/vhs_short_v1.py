from fastapi import APIRouter

from sql_app.database import get_db

router = APIRouter(
    prefix="/vhs", tags=["vhs"], responses={400: {"detail": "Not found"}}
)


@router.get("/users/{user_id}")
async def get_user_data(user_id: str):
    """
    get user by id
    """
    return


@router.patch("/users/{user_id}/assign")
async def user_assign_agreement(user_id: str):
    """
    get user by id
    update user agreement
    """
    return


@router.post("/users/{user_id}/redeems")
async def charge_redeems(user_id: str):
    """
    get user by id
    get redeems by code
    add redeem transaction table
    add charge point table
    update user's point
    update redeems count -1
    """
    return


@router.get("/users/{user_id}/gened_videos")
async def user_gened_videos(user_id):
    """
    get user by id
    find videos by user id
    """
    return


@router.get("/gen_flow/pub_videos")
async def get_pub_videos():
    """
    get all is public videos
    """
    return


@router.get("/gen_flow/pub_voices")
async def get_pub_voices():
    """
    get all is public voices and tones
    """
    return


@router.post("/gen_flow/tts")
async def tts_voices():
    """
    insert tts detail in voicelib and tone
    tts return link
    """
    return


@router.post("/gen_flow/users/{user_id}/videos")
async def user_upload_videos(user_id: str):
    """
    user upload self videos
    """
    return


@router.post("/gen_flow/users/{user_id}/voices")
async def user_upload_voices(user_id: str):
    """
    user upload self voices
    """
    return


@router.get("/gen_flow/lipsync/cost")
async def get_predict_gen_video_cost():
    """
    need video link, voice link, user id
    predict how many points, that lipsync will cost

    return user data, predict cost
    """
    return


@router.post("/gen_flow/lipsync/final")
async def gen_lipsync_videos():
    """
    gen the lipsync
    """
    return


@router.post("/lipsync/callback")
async def check_lipsync_gen_video_status():
    """
    find who gen
    push to the user
    """
    return
