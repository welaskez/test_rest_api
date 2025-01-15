-- Вставка данных в таблицу activities
INSERT INTO activities (id, name, parent_id, created_at, updated_at)
VALUES
    ('811868e5-6256-4ebb-8315-893e2c6acd8a', 'Еда', NULL, NOW(), NOW()), -- activity_1_id
    ('9bda502d-ee20-4744-ad9a-55644cf9d867', 'Мясная продукция', '811868e5-6256-4ebb-8315-893e2c6acd8a', NOW(), NOW()), -- activity_2_id
    ('d629068c-791a-47e0-b178-6cdd9f6066b2', 'Молочная продукция', '811868e5-6256-4ebb-8315-893e2c6acd8a', NOW(), NOW()),
    ('a2e0a640-4e73-4560-b22c-0e9860c426d6', 'Автомобили', NULL, NOW(), NOW()), -- activity_4_id
    ('13ecd60b-1ff7-4662-bbbf-dc948d523a6f', 'Грузовые', 'a2e0a640-4e73-4560-b22c-0e9860c426d6', NOW(), NOW()), -- activity_5_id
    ('579f8b49-c381-455c-b4b3-2627bc8f01c3', 'Запчасти', 'a2e0a640-4e73-4560-b22c-0e9860c426d6', NOW(), NOW());

-- Вставка данных в таблицу buildings
INSERT INTO buildings (id, county, region, city, district, micro_district_or_street, number, postal_code, latitude, longitude, created_at, updated_at)
VALUES
    ('e8b3773e-e499-4f0e-b205-e45a4016d0ba', 'Orange County', 'California', 'Los Angeles', 'Downtown', 'Main Street', '123', 90001, 34.052235, -118.243683, NOW(), NOW()), -- building_1_id
    ('999e93fd-408e-41ca-b5c6-40cbc74e9176', 'Kings County', 'New York', 'Brooklyn', 'Williamsburg', 'Bedford Avenue', '456', 11211, 40.708116, -73.957070, NOW(), NOW()),
    ('1a59130f-6f63-4f6a-b259-f5b812a7793b', 'Cook County', 'Illinois', 'Chicago', 'The Loop', 'State Street', '789', 60601, 41.881832, -87.623177, NOW(), NOW()),
    ('8865fafe-6c1e-4d73-80ae-78d9cfa8effb', 'Harris County', 'Texas', 'Houston', 'Midtown', 'Bagby Street', '101', 77002, 29.752255, -95.370727, NOW(), NOW()),
    ('21b8b4e6-5842-476a-bff9-0cf632dc141a', 'Maricopa County', 'Arizona', 'Phoenix', 'Camelback East', 'Camelback Road', '202', 85016, 33.507620, -112.065708, NOW(), NOW()); -- building_5_id

-- Вставка данных в таблицу organizations
INSERT INTO organizations (id, name, building_id, activity_id, created_at, updated_at)
VALUES
    ('f533055c-3a38-4215-aae3-8f301bd69ab9', 'Рога и Копыта', 'e8b3773e-e499-4f0e-b205-e45a4016d0ba', '9bda502d-ee20-4744-ad9a-55644cf9d867', NOW(), NOW()), -- organization_1_id
    ('ab21f9e3-56af-4a4b-b7e4-222bde7129fc', 'Автосервис', '21b8b4e6-5842-476a-bff9-0cf632dc141a', '13ecd60b-1ff7-4662-bbbf-dc948d523a6f', NOW(), NOW()); -- organization_2_id

-- Вставка данных в таблицу phones
INSERT INTO phones (id, number, organization_id, created_at, updated_at)
VALUES
    ('cd41f6b9-4c13-4ffb-a873-7bd4e2c68888', '777 777 777', 'f533055c-3a38-4215-aae3-8f301bd69ab9', NOW(), NOW()), -- phone_1_id
    ('d7e63af9-69bf-4f58-bb2e-88213b715c9a', '0 000 000 0', 'ab21f9e3-56af-4a4b-b7e4-222bde7129fc', NOW(), NOW());
