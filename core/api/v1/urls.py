from ninja import Router

from core.api.v1.courses.handlers import router as course_router
from core.api.v1.members.handlers import router as member_router
from core.api.v1.reviews.handlers import router as review_router


router = Router(
    tags=['v1'],
)

course_router.add_router('', review_router)
router.add_router('courses/', course_router)
router.add_router('members/', member_router)
