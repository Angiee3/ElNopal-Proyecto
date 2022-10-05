/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`, `permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`, `codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 69 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_user_groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`, `group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: auth_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`, `permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`, `model`)
) ENGINE = InnoDB AUTO_INCREMENT = 18 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: django_migrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 21 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: django_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: invoice_buy
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoice_buy`;
CREATE TABLE `invoice_buy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `payment` varchar(11) NOT NULL,
  `finalPrice` int NOT NULL,
  `observation` varchar(15) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_buy_user_id_38266fc6_fk_management_provider_id` (`user_id`),
  CONSTRAINT `invoice_buy_user_id_38266fc6_fk_management_provider_id` FOREIGN KEY (`user_id`) REFERENCES `management_provider` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 6 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: invoice_detailbuy
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoice_detailbuy`;
CREATE TABLE `invoice_detailbuy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int unsigned NOT NULL,
  `total` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `buy_id` bigint DEFAULT NULL,
  `product_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_detailbuy_buy_id_e219648e_fk_invoice_buy_id` (`buy_id`),
  KEY `invoice_detailbuy_product_id_2df9cb3f_fk_management_product_id` (`product_id`),
  CONSTRAINT `invoice_detailbuy_buy_id_e219648e_fk_invoice_buy_id` FOREIGN KEY (`buy_id`) REFERENCES `invoice_buy` (`id`),
  CONSTRAINT `invoice_detailbuy_product_id_2df9cb3f_fk_management_product_id` FOREIGN KEY (`product_id`) REFERENCES `management_product` (`id`),
  CONSTRAINT `invoice_detailbuy_chk_1` CHECK ((`amount` >= 0))
) ENGINE = InnoDB AUTO_INCREMENT = 7 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: invoice_detailsale
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoice_detailsale`;
CREATE TABLE `invoice_detailsale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int unsigned NOT NULL,
  `total` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint DEFAULT NULL,
  `sale_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_detailsale_product_id_20252ffd_fk_management_product_id` (`product_id`),
  KEY `invoice_detailsale_sale_id_bafb59e8_fk_invoice_sale_id` (`sale_id`),
  CONSTRAINT `invoice_detailsale_product_id_20252ffd_fk_management_product_id` FOREIGN KEY (`product_id`) REFERENCES `management_product` (`id`),
  CONSTRAINT `invoice_detailsale_sale_id_bafb59e8_fk_invoice_sale_id` FOREIGN KEY (`sale_id`) REFERENCES `invoice_sale` (`id`),
  CONSTRAINT `invoice_detailsale_chk_1` CHECK ((`amount` >= 0))
) ENGINE = InnoDB AUTO_INCREMENT = 12 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: invoice_sale
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoice_sale`;
CREATE TABLE `invoice_sale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `client` varchar(50) NOT NULL,
  `nDocument` varchar(20) NOT NULL,
  `address` varchar(254) NOT NULL,
  `typeSale` varchar(9) NOT NULL,
  `finalPrice` int NOT NULL,
  `payment` varchar(11) NOT NULL,
  `observation` varchar(15) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 9 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_backup
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_backup`;
CREATE TABLE `management_backup` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `file` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_brand
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_brand`;
CREATE TABLE `management_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 4 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_category
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_category`;
CREATE TABLE `management_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_product
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_product`;
CREATE TABLE `management_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `description` longtext NOT NULL,
  `stock` int unsigned DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `name_unitMeasurement` varchar(30) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `brand_id` bigint DEFAULT NULL,
  `subcategory_id` bigint DEFAULT NULL,
  `unitMeasurement_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `management_product_brand_id_bb713917_fk_management_brand_id` (`brand_id`),
  KEY `management_product_subcategory_id_49f8da34_fk_managemen` (`subcategory_id`),
  KEY `management_product_unitMeasurement_id_0349f6c0_fk_managemen` (`unitMeasurement_id`),
  CONSTRAINT `management_product_brand_id_bb713917_fk_management_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `management_brand` (`id`),
  CONSTRAINT `management_product_subcategory_id_49f8da34_fk_managemen` FOREIGN KEY (`subcategory_id`) REFERENCES `management_subcategory` (`id`),
  CONSTRAINT `management_product_unitMeasurement_id_0349f6c0_fk_managemen` FOREIGN KEY (`unitMeasurement_id`) REFERENCES `management_unit` (`id`),
  CONSTRAINT `management_product_chk_1` CHECK ((`stock` >= 0))
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_provider
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_provider`;
CREATE TABLE `management_provider` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_subcategory
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_subcategory`;
CREATE TABLE `management_subcategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `management_subcatego_category_id_a4264a4b_fk_managemen` (`category_id`),
  CONSTRAINT `management_subcatego_category_id_a4264a4b_fk_managemen` FOREIGN KEY (`category_id`) REFERENCES `management_category` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: management_unit
# ------------------------------------------------------------

DROP TABLE IF EXISTS `management_unit`;
CREATE TABLE `management_unit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` varchar(30) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_group
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_group_permissions
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_permission
# ------------------------------------------------------------

INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (5, 'Can add permission', 2, 'add_permission');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (6, 'Can change permission', 2, 'change_permission');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (8, 'Can view permission', 2, 'view_permission');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (9, 'Can add group', 3, 'add_group');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (10, 'Can change group', 3, 'change_group');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (11, 'Can delete group', 3, 'delete_group');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (12, 'Can view group', 3, 'view_group');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (13, 'Can add user', 4, 'add_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (14, 'Can change user', 4, 'change_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (15, 'Can delete user', 4, 'delete_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (16, 'Can view user', 4, 'view_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    18,
    'Can change content type',
    5,
    'change_contenttype'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    19,
    'Can delete content type',
    5,
    'delete_contenttype'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (21, 'Can add session', 6, 'add_session');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (22, 'Can change session', 6, 'change_session');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (23, 'Can delete session', 6, 'delete_session');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (24, 'Can view session', 6, 'view_session');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (25, 'Can add backup', 7, 'add_backup');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (26, 'Can change backup', 7, 'change_backup');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (27, 'Can delete backup', 7, 'delete_backup');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (28, 'Can view backup', 7, 'view_backup');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (29, 'Can add Marca', 8, 'add_brand');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (30, 'Can change Marca', 8, 'change_brand');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (31, 'Can delete Marca', 8, 'delete_brand');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (32, 'Can view Marca', 8, 'view_brand');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (33, 'Can add Categoría', 9, 'add_category');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (34, 'Can change Categoría', 9, 'change_category');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (35, 'Can delete Categoría', 9, 'delete_category');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (36, 'Can view Categoría', 9, 'view_category');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (37, 'Can add Proveedor', 10, 'add_provider');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (38, 'Can change Proveedor', 10, 'change_provider');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (39, 'Can delete Proveedor', 10, 'delete_provider');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (40, 'Can view Proveedor', 10, 'view_provider');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (41, 'Can add Unidad de Medida', 11, 'add_unit');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    42,
    'Can change Unidad de Medida',
    11,
    'change_unit'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    43,
    'Can delete Unidad de Medida',
    11,
    'delete_unit'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (44, 'Can view Unidad de Medida', 11, 'view_unit');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (45, 'Can add Subcategoría', 12, 'add_subcategory');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    46,
    'Can change Subcategoría',
    12,
    'change_subcategory'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    47,
    'Can delete Subcategoría',
    12,
    'delete_subcategory'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (48, 'Can view Subcategoría', 12, 'view_subcategory');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (49, 'Can add Producto', 13, 'add_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (50, 'Can change Producto', 13, 'change_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (51, 'Can delete Producto', 13, 'delete_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (52, 'Can view Producto', 13, 'view_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (53, 'Can add Compra', 14, 'add_buy');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (54, 'Can change Compra', 14, 'change_buy');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (55, 'Can delete Compra', 14, 'delete_buy');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (56, 'Can view Compra', 14, 'view_buy');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (57, 'Can add Venta', 15, 'add_sale');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (58, 'Can change Venta', 15, 'change_sale');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (59, 'Can delete Venta', 15, 'delete_sale');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (60, 'Can view Venta', 15, 'view_sale');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    61,
    'Can add Detalle de venta',
    16,
    'add_detailsale'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    62,
    'Can change Detalle de venta',
    16,
    'change_detailsale'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    63,
    'Can delete Detalle de venta',
    16,
    'delete_detailsale'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    64,
    'Can view Detalle de venta',
    16,
    'view_detailsale'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    65,
    'Can add Detalle de compra',
    17,
    'add_detailbuy'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    66,
    'Can change Detalle de compra',
    17,
    'change_detailbuy'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    67,
    'Can delete Detalle de compra',
    17,
    'delete_detailbuy'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    68,
    'Can view Detalle de compra',
    17,
    'view_detailbuy'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_user
# ------------------------------------------------------------

INSERT INTO
  `auth_user` (
    `id`,
    `password`,
    `last_login`,
    `is_superuser`,
    `username`,
    `first_name`,
    `last_name`,
    `email`,
    `is_staff`,
    `is_active`,
    `date_joined`
  )
VALUES
  (
    1,
    'pbkdf2_sha256$320000$f51jRoN4In1z3IMqT0BNk4$s+1HcwF0zWuiGOgRYhYmLofJQkxGYV7cs1BCxR/aR6s=',
    '2022-10-05 13:10:11.447185',
    1,
    'angie',
    '',
    '',
    '',
    1,
    1,
    '2022-10-05 10:50:17.164617'
  );
INSERT INTO
  `auth_user` (
    `id`,
    `password`,
    `last_login`,
    `is_superuser`,
    `username`,
    `first_name`,
    `last_name`,
    `email`,
    `is_staff`,
    `is_active`,
    `date_joined`
  )
VALUES
  (
    2,
    'pbkdf2_sha256$320000$Jcd2brsV8e9iTN42ywp07U$wN60xLjbVELL/iO/iN1psA/u+bmLx5S3tAbI+AclEEs=',
    '2022-10-05 13:24:38.651893',
    0,
    'Angiee',
    'Angie',
    'Pinzón',
    'anpinzon55@misena.edu.co',
    0,
    1,
    '2022-10-05 11:14:08.221643'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_user_groups
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: auth_user_user_permissions
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: django_admin_log
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: django_content_type
# ------------------------------------------------------------

INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (1, 'admin', 'logentry');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (3, 'auth', 'group');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (2, 'auth', 'permission');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (4, 'auth', 'user');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (5, 'contenttypes', 'contenttype');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (14, 'invoice', 'buy');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (17, 'invoice', 'detailbuy');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (16, 'invoice', 'detailsale');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (15, 'invoice', 'sale');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (7, 'management', 'backup');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (8, 'management', 'brand');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (9, 'management', 'category');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (13, 'management', 'product');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (10, 'management', 'provider');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (12, 'management', 'subcategory');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (11, 'management', 'unit');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (6, 'sessions', 'session');

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: django_migrations
# ------------------------------------------------------------

INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    1,
    'contenttypes',
    '0001_initial',
    '2022-10-05 10:50:01.190964'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    2,
    'auth',
    '0001_initial',
    '2022-10-05 10:50:02.132006'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    3,
    'admin',
    '0001_initial',
    '2022-10-05 10:50:02.500602'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    4,
    'admin',
    '0002_logentry_remove_auto_add',
    '2022-10-05 10:50:02.520607'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    5,
    'admin',
    '0003_logentry_add_action_flag_choices',
    '2022-10-05 10:50:02.546758'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    6,
    'contenttypes',
    '0002_remove_content_type_name',
    '2022-10-05 10:50:02.755728'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    7,
    'auth',
    '0002_alter_permission_name_max_length',
    '2022-10-05 10:50:02.990289'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    8,
    'auth',
    '0003_alter_user_email_max_length',
    '2022-10-05 10:50:03.080596'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    9,
    'auth',
    '0004_alter_user_username_opts',
    '2022-10-05 10:50:03.100550'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    10,
    'auth',
    '0005_alter_user_last_login_null',
    '2022-10-05 10:50:03.300679'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    11,
    'auth',
    '0006_require_contenttypes_0002',
    '2022-10-05 10:50:03.300679'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    12,
    'auth',
    '0007_alter_validators_add_error_messages',
    '2022-10-05 10:50:03.327570'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    13,
    'auth',
    '0008_alter_user_username_max_length',
    '2022-10-05 10:50:03.451689'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    14,
    'auth',
    '0009_alter_user_last_name_max_length',
    '2022-10-05 10:50:03.580569'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    15,
    'auth',
    '0010_alter_group_name_max_length',
    '2022-10-05 10:50:03.621821'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    16,
    'auth',
    '0011_update_proxy_permissions',
    '2022-10-05 10:50:03.648239'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    17,
    'auth',
    '0012_alter_user_first_name_max_length',
    '2022-10-05 10:50:03.786032'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    18,
    'management',
    '0001_initial',
    '2022-10-05 10:50:04.642529'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    19,
    'invoice',
    '0001_initial',
    '2022-10-05 10:50:05.290593'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    20,
    'sessions',
    '0001_initial',
    '2022-10-05 10:50:05.412008'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: django_session
# ------------------------------------------------------------

INSERT INTO
  `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
  (
    't57aq3t6hiqo4cq7dgdba6h2yv4qt8is',
    '.eJxVjMsOwiAUBf-FtSFwwQou3fsN5L4iVUOT0q6M_65NutDtmZnzMgXXpZa161xGMWcD5vC7EfJD2wbkju02WZ7aMo9kN8XutNvrJPq87O7fQcVev_URTpGIJeYkTKyQVYOHQOB8BBhi8IlyFofgXYicXBBMTMEPLMmheX8A28k3fw:1og2S1:L2nMPFpjirED6Y3utCS9pkOofh1IPXfMEx_r9vcw2I0',
    '2022-10-19 11:20:33.019402'
  );
INSERT INTO
  `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
  (
    'w6u51p96biabgbz5ydy6yxkjmctbcm0r',
    '.eJxVjMsOwiAUBf-FtSFwwQou3fsN5L4iVUOT0q6M_65NutDtmZnzMgXXpZa161xGMWcD5vC7EfJD2wbkju02WZ7aMo9kN8XutNvrJPq87O7fQcVev_URTpGIJeYkTKyQVYOHQOB8BBhi8IlyFofgXYicXBBMTMEPLMmheX8A28k3fw:1og4O6:93KNN4BLgp_Cngi4TDDXrHmLmbUqZfWnggmd_Xq4-wQ',
    '2022-10-19 13:24:38.659261'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_buy
# ------------------------------------------------------------

INSERT INTO
  `invoice_buy` (
    `id`,
    `date`,
    `payment`,
    `finalPrice`,
    `observation`,
    `status`,
    `user_id`
  )
VALUES
  (
    1,
    '2022-10-05 10:51:27.920428',
    'Efectivo',
    23456,
    'Otro',
    'Pendiente',
    1
  );
INSERT INTO
  `invoice_buy` (
    `id`,
    `date`,
    `payment`,
    `finalPrice`,
    `observation`,
    `status`,
    `user_id`
  )
VALUES
  (
    2,
    '2022-10-05 11:28:30.640609',
    'Efectivo',
    23456,
    ' ',
    'Cerrada',
    1
  );
INSERT INTO
  `invoice_buy` (
    `id`,
    `date`,
    `payment`,
    `finalPrice`,
    `observation`,
    `status`,
    `user_id`
  )
VALUES
  (
    3,
    '2022-10-05 11:47:19.360120',
    'Efectivo',
    200,
    ' ',
    'Cerrada',
    1
  );
INSERT INTO
  `invoice_buy` (
    `id`,
    `date`,
    `payment`,
    `finalPrice`,
    `observation`,
    `status`,
    `user_id`
  )
VALUES
  (
    4,
    '2022-10-05 13:37:10.071198',
    'Efectivo',
    400,
    ' ',
    'Cerrada',
    1
  );
INSERT INTO
  `invoice_buy` (
    `id`,
    `date`,
    `payment`,
    `finalPrice`,
    `observation`,
    `status`,
    `user_id`
  )
VALUES
  (
    5,
    '2022-10-05 16:34:41.447179',
    'Efectivo',
    1200,
    ' ',
    'Abierta',
    1
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_detailbuy
# ------------------------------------------------------------

INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (1, 1, 23456, 1, 1, 1);
INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (2, 1, 23456, 1, 2, 1);
INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (3, 1, 200, 1, 3, 1);
INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (4, 2, 400, 1, 4, 1);
INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (5, 1, 1000, 1, 5, 2);
INSERT INTO
  `invoice_detailbuy` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `buy_id`,
    `product_id`
  )
VALUES
  (6, 1, 200, 1, 5, 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_detailsale
# ------------------------------------------------------------

INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (1, 1, 23456, 1, 1, 1);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (3, 501, 100200, 1, 1, 3);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (4, 14, 2800, 1, 1, 4);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (5, 2, 2000, 1, 2, 4);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (6, 3, 600, 1, 1, 5);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (8, 1, 1000, 1, 2, 5);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (10, 1, 1000, 1, 2, 6);
INSERT INTO
  `invoice_detailsale` (
    `id`,
    `amount`,
    `total`,
    `status`,
    `product_id`,
    `sale_id`
  )
VALUES
  (11, 1, 200, 1, 1, 2);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_sale
# ------------------------------------------------------------

INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    1,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    23456,
    'Efectivo',
    ' ',
    'Abierta'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    2,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    101200,
    'Efectivo',
    ' ',
    'Cerrada'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    3,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    100200,
    'Efectivo',
    ' ',
    'Abierta'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    4,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    4800,
    'Efectivo',
    ' ',
    'Cerrada'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    5,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    1600,
    'Efectivo',
    ' ',
    'Abierta'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    6,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    1000,
    'Efectivo',
    'Cambio',
    'Pendiente'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    7,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    0,
    'Efectivo',
    ' ',
    'Abierta'
  );
INSERT INTO
  `invoice_sale` (
    `id`,
    `date`,
    `client`,
    `nDocument`,
    `address`,
    `typeSale`,
    `finalPrice`,
    `payment`,
    `observation`,
    `status`
  )
VALUES
  (
    8,
    '2022-10-05',
    'Cliente local',
    '1234567890',
    'Local',
    'store',
    0,
    'Efectivo',
    ' ',
    'Abierta'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_backup
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_brand
# ------------------------------------------------------------

INSERT INTO
  `management_brand` (`id`, `Nombre`, `status`)
VALUES
  (1, 'Kj', 1);
INSERT INTO
  `management_brand` (`id`, `Nombre`, `status`)
VALUES
  (2, 'Prueba', 0);
INSERT INTO
  `management_brand` (`id`, `Nombre`, `status`)
VALUES
  (3, 'Jedsdkjsnk', 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_category
# ------------------------------------------------------------

INSERT INTO
  `management_category` (`id`, `Nombre`, `Status`)
VALUES
  (1, 'Grdf', 1);
INSERT INTO
  `management_category` (`id`, `Nombre`, `Status`)
VALUES
  (2, 'Gtrfeds', 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_product
# ------------------------------------------------------------

INSERT INTO
  `management_product` (
    `id`,
    `name`,
    `price`,
    `description`,
    `stock`,
    `type`,
    `name_unitMeasurement`,
    `image`,
    `status`,
    `brand_id`,
    `subcategory_id`,
    `unitMeasurement_id`
  )
VALUES
  (
    1,
    'Kjhbgvy',
    200,
    '',
    99,
    'Masa',
    'Njnm',
    'product/Logo.png',
    1,
    1,
    1,
    NULL
  );
INSERT INTO
  `management_product` (
    `id`,
    `name`,
    `price`,
    `description`,
    `stock`,
    `type`,
    `name_unitMeasurement`,
    `image`,
    `status`,
    `brand_id`,
    `subcategory_id`,
    `unitMeasurement_id`
  )
VALUES
  (
    2,
    'Cfgvbhjnmk',
    1000,
    '',
    99,
    'Masa',
    'Njnm',
    'product/Logo.png',
    1,
    1,
    1,
    NULL
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_provider
# ------------------------------------------------------------

INSERT INTO
  `management_provider` (`id`, `name`, `phone`, `email`, `status`)
VALUES
  (1, 'Ñl,Kmjnhbugy', '321', 'ksdajks@mail.com', 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_subcategory
# ------------------------------------------------------------

INSERT INTO
  `management_subcategory` (`id`, `name`, `image`, `status`, `category_id`)
VALUES
  (1, 'Jhkl,', 'subcategory/Logo.png', 1, 2);
INSERT INTO
  `management_subcategory` (`id`, `name`, `image`, `status`, `category_id`)
VALUES
  (2, 'Lmk', 'subcategory/Logo.png', 1, 2);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_unit
# ------------------------------------------------------------

INSERT INTO
  `management_unit` (`id`, `name`, `type`, `status`)
VALUES
  (1, 'Njnm', 'Masa', 1);

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
