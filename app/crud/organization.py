from math import cos, pi

from core.config import settings
from core.models import Activity, Building, Organization
from sqlalchemy import ColumnExpressionArgument, func, literal, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from crud.base import BaseCRUD


class OrganizationCRUD(BaseCRUD[Organization]):
    model = Organization

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_loaded_organization_by_expression(
        self, expression: ColumnExpressionArgument
    ) -> Organization | None:
        """
        Return organization with loaded relations
        :param expression: where expression
        :return: organization or none
        """
        organization = await self.session.scalar(
            select(Organization)
            .options(
                selectinload(Organization.building),
                selectinload(Organization.activity).selectinload(
                    Activity.childrens, recursion_depth=3
                ),
            )
            .where(expression)
        )

        return organization

    async def get_organizations_in_circular_area(
        self,
        center_latitude: float,
        center_longitude: float,
        radius: float,
    ) -> list[Organization]:
        """
        Return organizations in circular area
        the Haversine formula is used in the calculations
        https://en.wikipedia.org/wiki/Haversine_formula
        :param center_latitude: central latitude
        :param center_longitude: central longitude
        :param radius: radius of search
        :return: list of organizations
        """
        delta_latitude = radius / settings.earth_radius_in_km * (180 / pi)
        delta_longitude = (
            radius
            / (settings.earth_radius_in_km * abs(cos(center_latitude * (pi / 180))))
            * (180 / pi)
        )

        latitude_range = (
            center_latitude - delta_latitude,
            center_latitude + delta_latitude,
        )
        longitude_range = (
            center_longitude - delta_longitude,
            center_longitude + delta_longitude,
        )

        latitude_diff = func.radians(Building.latitude - literal(center_latitude)) / 2
        longitude_diff = (
            func.radians(Building.longitude - literal(center_longitude)) / 2
        )

        sin_lat_diff = func.sin(latitude_diff)
        sin_lon_diff = func.sin(longitude_diff)

        haversine_core = func.pow(sin_lat_diff, 2) + (
            func.cos(func.radians(Building.latitude))
            * func.cos(func.radians(literal(center_latitude)))
            * func.pow(sin_lon_diff, 2)
        )

        haversine_distance = (
            settings.earth_radius_in_km
            * 2
            * func.atan2(
                func.sqrt(haversine_core),
                func.sqrt(1 - haversine_core),
            )
        )

        organizations = await self.session.scalars(
            select(Organization)
            .join(Building)
            .options(
                selectinload(Organization.building),
                selectinload(Organization.activity).selectinload(
                    Activity.childrens, recursion_depth=3
                ),
            )
            .where(
                Building.latitude.between(*latitude_range),
                Building.longitude.between(*longitude_range),
                haversine_distance <= literal(radius),
            )
        )

        return list(organizations)

    async def get_organizations_in_rect_area(
        self,
        min_latitude: float,
        max_latitude: float,
        min_longitude: float,
        max_longitude: float,
    ) -> list[Organization]:
        """
        Return organizations in rectangle area
        :param min_latitude: minimal latitude
        :param max_latitude: maximal latitude
        :param min_longitude: minimal longitude
        :param max_longitude: maximal longitude
        :return: list of organizations
        """
        organizations = await self.session.scalars(
            select(Organization)
            .join(Building)
            .options(
                selectinload(Organization.building),
                selectinload(Organization.activity).selectinload(
                    Activity.childrens, recursion_depth=3
                ),
            )
            .where(
                Building.latitude.between(min_latitude, max_latitude),
                Building.longitude.between(min_longitude, max_longitude),
            )
            .distinct()
        )

        return list(organizations)
