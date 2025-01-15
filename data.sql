-- Вставка данных в таблицу activities
INSERT INTO activities (id, name, parent_id, created_at, updated_at)
VALUES
    ('a1f37e1d-d6b8-4c6c-812d-1d3e2926f1e1', 'Еда', NULL, NOW(), NOW()), -- activity_1_id
    ('b2e49f2d-e7c9-4d7d-923e-2e4f3837f2f2', 'Мясная продукция', 'a1f37e1d-d6b8-4c6c-812d-1d3e2926f1e1', NOW(), NOW()), -- activity_2_id
    ('c3f5a03e-f8da-4e8e-a34e-3f5f4948f3f3', 'Молочная продукция', 'a1f37e1d-d6b8-4c6c-812d-1d3e2926f1e1', NOW(), NOW()),
    ('d4f6b14f-g9eb-4f9f-b45e-4f6f5a59f4f4', 'Автомобили', NULL, NOW(), NOW()), -- activity_4_id
    ('e5f7c25g-h1fc-5gaf-c56f-5g7f6b6af5g5', 'Грузовые', 'd4f6b14f-g9eb-4f9f-b45e-4f6f5a59f4f4', NOW(), NOW()), -- activity_5_id
    ('f6f8d36h-i2gd-6hbg-d67g-6h8f7c7bg6h6', 'Запчасти', 'd4f6b14f-g9eb-4f9f-b45e-4f6f5a59f4f4', NOW(), NOW());

-- Вставка данных в таблицу buildings
INSERT INTO buildings (id, county, region, city, district, micro_district_or_street, number, postal_code, latitude, longitude, created_at, updated_at)
VALUES
    ('a7f9e47i-j3he-7icg-e78h-7i9f8d8ch7i7', 'Orange County', 'California', 'Los Angeles', 'Downtown', 'Main Street', '123', 90001, 34.052235, -118.243683, NOW(), NOW()), -- building_1_id
    ('b8g1f58j-k4if-8jdg-f89i-8j1g9e9di8j8', 'Kings County', 'New York', 'Brooklyn', 'Williamsburg', 'Bedford Avenue', '456', 11211, 40.708116, -73.957070, NOW(), NOW()),
    ('c9h2g69k-l5jg-9keh-g90j-9k2h1f1ej9k9', 'Cook County', 'Illinois', 'Chicago', 'The Loop', 'State Street', '789', 60601, 41.881832, -87.623177, NOW(), NOW()),
    ('d1i3h7al-m6kh-aifl-h01k-a3i2g2fk0a1a', 'Harris County', 'Texas', 'Houston', 'Midtown', 'Bagby Street', '101', 77002, 29.752255, -95.370727, NOW(), NOW()),
    ('e2j4i8bm-n7li-bjgm-i12l-b4j3h3gl1b2b', 'Maricopa County', 'Arizona', 'Phoenix', 'Camelback East', 'Camelback Road', '202', 85016, 33.507620, -112.065708, NOW(), NOW()); -- building_5_id

-- Вставка данных в таблицу organizations
INSERT INTO organizations (id, name, building_id, activity_id, created_at, updated_at)
VALUES
    ('f3k5j9cn-o8mj-cjhn-j23m-c5k4i4hm2c3c', 'Рога и Копыта', 'a7f9e47i-j3he-7icg-e78h-7i9f8d8ch7i7', 'b2e49f2d-e7c9-4d7d-923e-2e4f3837f2f2', NOW(), NOW()), -- organization_1_id
    ('g4l6kado-p9nk-dkio-k34n-d6l5j5in3d4d', 'Автосервис', 'e2j4i8bm-n7li-bjgm-i12l-b4j3h3gl1b2b', 'e5f7c25g-h1fc-5gaf-c56f-5g7f6b6af5g5', NOW(), NOW()); -- organization_2_id

-- Вставка данных в таблицу phone_numbers
INSERT INTO phone_numbers (id, number, organization_id, created_at, updated_at)
VALUES
    ('h5m7lcep-q1ok-eljp-l45o-e7m6k6jo4e5e', '777 777 777', 'f3k5j9cn-o8mj-cjhn-j23m-c5k4i4hm2c3c', NOW(), NOW()), -- phone_1_id
    ('i6n8mdfq-r2pl-fmkq-m56p-f8n7l7kp5f6f', '0 000 000 0', 'g4l6kado-p9nk-dkio-k34n-d6l5j5in3d4d', NOW(), NOW());
