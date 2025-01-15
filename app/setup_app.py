from core.models import Activity, Building, Organization, Phone, User, db_helper
from core.schemas.activity import ActivityCreate
from core.schemas.building import BuildingCreate
from core.schemas.organization import OrganizationCreate
from core.schemas.phone_number import PhoneNumberCreate
from crud.activity import ActivityCRUD
from crud.building import BuildingCRUD
from crud.organization import OrganizationCRUD
from crud.phone import PhoneCRUD
from sqlalchemy import text


async def setup_db():
    async with db_helper.session_pool() as session:
        activity_crud = ActivityCRUD(session)
        building_crud = BuildingCRUD(session)
        organization_crud = OrganizationCRUD(session)
        phone_crud = PhoneCRUD(session)

        activity_1 = await activity_crud.create(
            ActivityCreate(name="Еда", parent_id=None)
        )

        activity_2 = await activity_crud.create(
            ActivityCreate(name="Мясная продукция", parent_id=activity_1.id)
        )

        await activity_crud.create(
            ActivityCreate(name="Молочная продукция", parent_id=activity_1.id)
        )

        activity_4 = await activity_crud.create(
            ActivityCreate(name="Автомобили", parent_id=None)
        )

        activity_5 = await activity_crud.create(
            ActivityCreate(name="Грузовые", parent_id=activity_4.id)
        )

        await activity_crud.create(
            ActivityCreate(name="Запчасти", parent_id=activity_4.id)
        )

        building_1 = await building_crud.create(
            BuildingCreate(
                county="Orange County",
                region="California",
                city="Los Angeles",
                district="Downtown",
                micro_district_or_street="Main Street",
                number="123",
                postal_code=90001,
                latitude=34.052235,
                longitude=-118.243683,
            )
        )

        await building_crud.create(
            BuildingCreate(
                county="Kings County",
                region="New York",
                city="Brooklyn",
                district="Williamsburg",
                micro_district_or_street="Bedford Avenue",
                number="456",
                postal_code=11211,
                latitude=40.708116,
                longitude=-73.957070,
            )
        )

        await building_crud.create(
            BuildingCreate(
                county="Cook County",
                region="Illinois",
                city="Chicago",
                district="The Loop",
                micro_district_or_street="State Street",
                number="789",
                postal_code=60601,
                latitude=41.881832,
                longitude=-87.623177,
            )
        )

        await building_crud.create(
            BuildingCreate(
                county="Harris County",
                region="Texas",
                city="Houston",
                district="Midtown",
                micro_district_or_street="Bagby Street",
                number="101",
                postal_code=77002,
                latitude=29.752255,
                longitude=-95.370727,
            )
        )

        building_5 = await building_crud.create(
            BuildingCreate(
                county="Maricopa County",
                region="Arizona",
                city="Phoenix",
                district="Camelback East",
                micro_district_or_street="Camelback Road",
                number="202",
                postal_code=85016,
                latitude=33.507620,
                longitude=-112.065708,
            )
        )

        organization_1 = await organization_crud.create(
            OrganizationCreate(
                name="Рога и Копыта",
                building_id=building_1.id,
                activity_id=activity_2.id,
            )
        )

        organization_2 = await organization_crud.create(
            OrganizationCreate(
                name="Автосервис",
                building_id=building_5.id,
                activity_id=activity_5.id,
            )
        )

        await phone_crud.create(
            PhoneNumberCreate(
                number="777 777 777",
                organization_id=organization_1.id,
            )
        )

        await phone_crud.create(
            PhoneNumberCreate(
                number="0 000 000 0",
                organization_id=organization_2.id,
            )
        )


async def clear_db():
    async with db_helper.session_pool() as session:
        for model in [Phone, Organization, Activity, Building, User]:
            await session.execute(
                text(f"TRUNCATE TABLE {model.__tablename__} RESTART IDENTITY CASCADE;")
            )
            await session.commit()
