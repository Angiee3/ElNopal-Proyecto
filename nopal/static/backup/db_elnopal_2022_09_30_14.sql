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
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
) ENGINE = InnoDB AUTO_INCREMENT = 35 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
  `status` varchar(10) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `observation` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_buy_user_id_38266fc6_fk_management_provider_id` (`user_id`),
  CONSTRAINT `invoice_buy_user_id_38266fc6_fk_management_provider_id` FOREIGN KEY (`user_id`) REFERENCES `management_provider` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# ------------------------------------------------------------
# SCHEMA DUMP FOR TABLE: invoice_detailsale
# ------------------------------------------------------------

DROP TABLE IF EXISTS `invoice_detailsale`;
CREATE TABLE `invoice_detailsale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int unsigned NOT NULL,
  `total` int NOT NULL,
  `status` varchar(10) NOT NULL,
  `product_id` bigint DEFAULT NULL,
  `sale_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_detailsale_product_id_20252ffd_fk_management_product_id` (`product_id`),
  KEY `invoice_detailsale_sale_id_bafb59e8_fk_invoice_sale_id` (`sale_id`),
  CONSTRAINT `invoice_detailsale_product_id_20252ffd_fk_management_product_id` FOREIGN KEY (`product_id`) REFERENCES `management_product` (`id`),
  CONSTRAINT `invoice_detailsale_sale_id_bafb59e8_fk_invoice_sale_id` FOREIGN KEY (`sale_id`) REFERENCES `invoice_sale` (`id`),
  CONSTRAINT `invoice_detailsale_chk_1` CHECK ((`amount` >= 0))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
  `status` varchar(10) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `observation` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_sale_user_id_0f4d39af_fk_store_user_id` (`user_id`),
  CONSTRAINT `invoice_sale_user_id_0f4d39af_fk_store_user_id` FOREIGN KEY (`user_id`) REFERENCES `store_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
  `image` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `brand_id` bigint DEFAULT NULL,
  `subcategory_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `management_product_brand_id_bb713917_fk_management_brand_id` (`brand_id`),
  KEY `management_product_subcategory_id_49f8da34_fk_managemen` (`subcategory_id`),
  CONSTRAINT `management_product_brand_id_bb713917_fk_management_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `management_brand` (`id`),
  CONSTRAINT `management_product_subcategory_id_49f8da34_fk_managemen` FOREIGN KEY (`subcategory_id`) REFERENCES `management_subcategory` (`id`),
  CONSTRAINT `management_product_chk_1` CHECK ((`stock` >= 0))
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
# SCHEMA DUMP FOR TABLE: store_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `store_user`;
CREATE TABLE `store_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `tDocument` varchar(21) NOT NULL,
  `nDocument` int NOT NULL,
  `phone` varchar(10) NOT NULL,
  `dateBirth` date NOT NULL,
  `email` varchar(254) NOT NULL,
  `user_admin` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

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
  (41, 'Can add Subcategoría', 11, 'add_subcategory');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    42,
    'Can change Subcategoría',
    11,
    'change_subcategory'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (
    43,
    'Can delete Subcategoría',
    11,
    'delete_subcategory'
  );
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (44, 'Can view Subcategoría', 11, 'view_subcategory');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (45, 'Can add Producto', 12, 'add_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (46, 'Can change Producto', 12, 'change_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (47, 'Can delete Producto', 12, 'delete_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (48, 'Can view Producto', 12, 'view_product');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (49, 'Can add Usuario', 13, 'add_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (50, 'Can change Usuario', 13, 'change_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (51, 'Can delete Usuario', 13, 'delete_user');
INSERT INTO
  `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
  (52, 'Can view Usuario', 13, 'view_user');
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
    'pbkdf2_sha256$320000$tPQfy62XWpOfaRV48to1at$IncvIJrW0CEs2i51sGzssMPdlKwAsZSfPsJYSr0GQ8A=',
    '2022-09-30 17:11:57.007064',
    1,
    'Administrador',
    '',
    '',
    '',
    1,
    1,
    '2022-09-30 17:11:44.797372'
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
  (12, 'management', 'product');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (10, 'management', 'provider');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (11, 'management', 'subcategory');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (6, 'sessions', 'session');
INSERT INTO
  `django_content_type` (`id`, `app_label`, `model`)
VALUES
  (13, 'store', 'user');

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
    '2022-09-30 17:10:34.870430'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    2,
    'auth',
    '0001_initial',
    '2022-09-30 17:10:35.594474'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    3,
    'admin',
    '0001_initial',
    '2022-09-30 17:10:35.797344'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    4,
    'admin',
    '0002_logentry_remove_auto_add',
    '2022-09-30 17:10:35.818711'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    5,
    'admin',
    '0003_logentry_add_action_flag_choices',
    '2022-09-30 17:10:35.828080'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    6,
    'contenttypes',
    '0002_remove_content_type_name',
    '2022-09-30 17:10:36.021017'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    7,
    'auth',
    '0002_alter_permission_name_max_length',
    '2022-09-30 17:10:36.132382'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    8,
    'auth',
    '0003_alter_user_email_max_length',
    '2022-09-30 17:10:36.172493'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    9,
    'auth',
    '0004_alter_user_username_opts',
    '2022-09-30 17:10:36.188521'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    10,
    'auth',
    '0005_alter_user_last_login_null',
    '2022-09-30 17:10:36.275764'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    11,
    'auth',
    '0006_require_contenttypes_0002',
    '2022-09-30 17:10:36.275764'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    12,
    'auth',
    '0007_alter_validators_add_error_messages',
    '2022-09-30 17:10:36.291802'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    13,
    'auth',
    '0008_alter_user_username_max_length',
    '2022-09-30 17:10:36.447800'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    14,
    'auth',
    '0009_alter_user_last_name_max_length',
    '2022-09-30 17:10:36.575829'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    15,
    'auth',
    '0010_alter_group_name_max_length',
    '2022-09-30 17:10:36.607254'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    16,
    'auth',
    '0011_update_proxy_permissions',
    '2022-09-30 17:10:36.623257'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    17,
    'auth',
    '0012_alter_user_first_name_max_length',
    '2022-09-30 17:10:36.723115'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    18,
    'store',
    '0001_initial',
    '2022-09-30 17:10:36.766324'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    19,
    'management',
    '0001_initial',
    '2022-09-30 17:10:37.386698'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    20,
    'invoice',
    '0001_initial',
    '2022-09-30 17:10:38.005300'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    21,
    'invoice',
    '0002_rename_provider_buy_user_buy_observation_and_more',
    '2022-09-30 17:10:38.261147'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    22,
    'invoice',
    '0003_alter_buy_observation_alter_sale_observation',
    '2022-09-30 17:10:38.271806'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    23,
    'invoice',
    '0004_alter_buy_observation_alter_sale_observation',
    '2022-09-30 17:10:38.290210'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    24,
    'invoice',
    '0005_alter_buy_observation_alter_sale_observation',
    '2022-09-30 17:10:38.430671'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    25,
    'invoice',
    '0006_alter_buy_observation',
    '2022-09-30 17:10:38.439724'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    26,
    'invoice',
    '0007_alter_sale_observation',
    '2022-09-30 17:10:38.446313'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    27,
    'invoice',
    '0008_alter_buy_payment_alter_sale_payment',
    '2022-09-30 17:10:38.462427'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    28,
    'invoice',
    '0009_alter_detailbuy_amount_alter_detailsale_amount',
    '2022-09-30 17:10:38.485324'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    29,
    'management',
    '0002_alter_unit_options',
    '2022-09-30 17:10:38.501065'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    30,
    'management',
    '0003_unit_status',
    '2022-09-30 17:10:38.557472'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    31,
    'management',
    '0004_alter_backup_file',
    '2022-09-30 17:10:38.573078'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    32,
    'management',
    '0005_remove_product_unitmeasurement_delete_unit',
    '2022-09-30 17:10:38.751655'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    33,
    'management',
    '0006_alter_backup_file_alter_backup_name',
    '2022-09-30 17:10:38.761523'
  );
INSERT INTO
  `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
  (
    34,
    'sessions',
    '0001_initial',
    '2022-09-30 17:10:38.817923'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: django_session
# ------------------------------------------------------------

INSERT INTO
  `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
  (
    'elsrperd3jucwej9r9gg1rjf3hd4srq6',
    '.eJxVjEEOwiAQRe_C2hAoDAWX7j0DmYGpVA0kpV0Z765NutDtf-_9l4i4rSVunZc4Z3EWWpx-N8L04LqDfMd6azK1ui4zyV2RB-3y2jI_L4f7d1Cwl2_t7Gj9pEL2w6iI2SViY5VGDNYQAChnGRi05ZQ0GmYMA3rQNCGBTuL9AdkEOCE:1oeJYL:GcdDAXwc71bcT0bgcCaLIfETpOSzV8IGl-qblywY3T0',
    '2022-10-14 17:11:57.013084'
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_buy
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_detailbuy
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_detailsale
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: invoice_sale
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_backup
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_brand
# ------------------------------------------------------------

INSERT INTO
  `management_brand` (`id`, `Nombre`, `status`)
VALUES
  (1, 'Margaritas', 1);
INSERT INTO
  `management_brand` (`id`, `Nombre`, `status`)
VALUES
  (2, 'Corona Extra', 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_category
# ------------------------------------------------------------

INSERT INTO
  `management_category` (`id`, `Nombre`, `Status`)
VALUES
  (1, 'Bebidas', 1);
INSERT INTO
  `management_category` (`id`, `Nombre`, `Status`)
VALUES
  (2, 'Snacks', 1);

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_product
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_provider
# ------------------------------------------------------------

INSERT INTO
  `management_provider` (`id`, `name`, `phone`, `email`, `status`)
VALUES
  (
    1,
    'Margaritas',
    '3185405258',
    'miguesgamez@gmail.com',
    1
  );
INSERT INTO
  `management_provider` (`id`, `name`, `phone`, `email`, `status`)
VALUES
  (
    2,
    'Corona Extra',
    '3216549870',
    'brayan@gmail.com',
    1
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: management_subcategory
# ------------------------------------------------------------

INSERT INTO
  `management_subcategory` (`id`, `name`, `image`, `status`, `category_id`)
VALUES
  (
    1,
    'Licores',
    'subcategory/239-2395930_bebidas-el-duende-stella-artois-hd-png-download.png',
    1,
    1
  );
INSERT INTO
  `management_subcategory` (`id`, `name`, `image`, `status`, `category_id`)
VALUES
  (
    2,
    'Galgueria',
    'subcategory/Screenshot_2019-07-16-07-20-48-1-350x243.png',
    1,
    2
  );

# ------------------------------------------------------------
# DATA DUMP FOR TABLE: store_user
# ------------------------------------------------------------


/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
