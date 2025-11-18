-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2025 at 08:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecotech`
--

-- --------------------------------------------------------

--
-- Table structure for table `asignacion_emp`
--

CREATE TABLE `asignacion_emp` (
  `USER_ID` int(12) NOT NULL,
  `empleado_id` int(12) NOT NULL,
  `proyecto_id` int(12) NOT NULL,
  `fecha_asignacion` date NOT NULL,
  `rol` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `asignacion_emp`
--

INSERT INTO `asignacion_emp` (`USER_ID`, `empleado_id`, `proyecto_id`, `fecha_asignacion`, `rol`) VALUES
(8, 7, 1, '0000-00-00', 'Jefe'),
(10, 7, 4, '0000-00-00', 'Mantenedor'),
(11, 6, 1, '0000-00-00', 'Gerente'),
(12, 7, 4, '0000-00-00', 'Gerente'),
(14, 10, 6, '0000-00-00', 'Tecnico');

-- --------------------------------------------------------

--
-- Table structure for table `departamento`
--

CREATE TABLE `departamento` (
  `USER_ID` int(12) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `gerente_empleado_id` int(12) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `departamento`
--

INSERT INTO `departamento` (`USER_ID`, `nombre`, `gerente_empleado_id`, `descripcion`) VALUES
(1, 'Informatica', 2, 'Departamento de IoT y Ciberseguridad.'),
(2, 'Mecanica', 1, 'Equipos fijos de mantenimiento.'),
(3, 'Electricidad', 4, 'Materiales de electricidad en laboratorios.'),
(4, 'Prueba', 8, 'prueba');

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

CREATE TABLE `empleado` (
  `USER_ID` int(12) NOT NULL,
  `run` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` int(50) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `salario` int(12) NOT NULL,
  `departamento_id` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `empleado`
--

INSERT INTO `empleado` (`USER_ID`, `run`, `nombre`, `direccion`, `telefono`, `correo`, `fecha_inicio`, `salario`, `departamento_id`) VALUES
(6, '12', 'Pancho', '1 Norte 1450', 944775588, 'pancho@pc.cl', '2015-05-01', 2500000, 3),
(7, '1', 'Javier', '5 Norte 550', 2147483647, 'javier@jc.cl', '2025-10-01', 1500000, 2),
(10, '30', 'Test', 'TEST', 12031, 'test@test.test', '2000-03-10', 20000, 4);

-- --------------------------------------------------------

--
-- Table structure for table `indicador`
--

CREATE TABLE `indicador` (
  `id` int(12) NOT NULL,
  `tipo_indicador` varchar(255) NOT NULL,
  `fecha_valor` date NOT NULL,
  `valor` int(12) NOT NULL,
  `fecha_consulta` date NOT NULL,
  `usuario_id` int(12) NOT NULL,
  `fuente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indicador`
--

INSERT INTO `indicador` (`id`, `tipo_indicador`, `fecha_valor`, `valor`, `fecha_consulta`, `usuario_id`, `fuente`) VALUES
(1, 'DOLAR', '2007-04-10', 535, '0000-00-00', 1, 'mindicador.cl'),
(3, 'EURO', '2004-05-10', 760, '2025-11-18', 1, 'mindicador.cl'),
(4, 'DOLAR', '2025-03-10', 928, '2025-11-18', 1, 'mindicador.cl'),
(5, 'EURO', '2005-06-20', 713, '2025-11-18', 3, 'https://mindicador.cl/api/euro/20-06-2005'),
(6, 'EURO', '2004-04-30', 748, '2025-11-18', 4, 'https://mindicador.cl/api/euro/30-04-2004'),
(7, 'UF', '2000-06-20', 15437, '2025-11-18', 4, 'https://mindicador.cl/api/uf/20-06-2000');

-- --------------------------------------------------------

--
-- Table structure for table `proyecto`
--

CREATE TABLE `proyecto` (
  `USER_ID` int(12) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` text NOT NULL,
  `fecha_inicio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `proyecto`
--

INSERT INTO `proyecto` (`USER_ID`, `nombre`, `descripcion`, `fecha_inicio`) VALUES
(1, 'IoT Sede', 'Instalacion de dispositivos.', '2025-10-01'),
(4, 'Fibra Sedes', 'Comunica Sedes mediante fibra.', '2025-10-01'),
(6, 'Prueba', 'Test', '2025-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `tiempo`
--

CREATE TABLE `tiempo` (
  `USER_ID` int(12) NOT NULL,
  `empleado_id` int(12) NOT NULL,
  `proyecto_id` int(12) NOT NULL,
  `fecha` date NOT NULL,
  `horas` int(12) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tiempo`
--

INSERT INTO `tiempo` (`USER_ID`, `empleado_id`, `proyecto_id`, `fecha`, `horas`, `descripcion`) VALUES
(6, 6, 1, '0202-02-02', 1, '222'),
(7, 6, 1, '0000-00-00', 50, 'Tareas amplias.'),
(8, 6, 4, '2025-01-01', 72, 'Horas extra en proyecto de Sedes-'),
(9, 10, 6, '2025-11-09', 50, 'test');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(12) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(120) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tipo_usuario` enum('Administrador','Usuario') NOT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password_hash`, `nombre`, `apellidos`, `email`, `tipo_usuario`, `fecha_registro`) VALUES
(1, 'pancho', '$2b$12$1kQvXS.zT.JVrBXNPOfyWe0mwEkdzDOepEw/XMKfPvx4XlLlkkwX2', 'Francisco', 'Jara Bernal', 'francisco.jara30@inacapmail.cl', 'Usuario', '2025-10-22 12:24:54'),
(2, 'Pepe', '$2b$12$8X/xvLFuOu2Nz.CuEyeEhef4GWQnfUUy7k4WTKjjK0RZsjM3yfR02', 'Pepe', 'Rojas', 'rojas@pepe.cl', 'Administrador', '2025-10-22 12:28:34'),
(3, 'yuki', '$2b$12$TFyp4JYtfleQmTsfEKxUregsSi/CQa/nL9weu6.u2FepNvShRBENW', 'Kokoa', 'Hoshi', 'kokoa@gmail.com', 'Administrador', '2025-11-14 22:34:16'),
(4, 'test', '$2b$12$uT1kBVHCMMUczN/fb8Y7EOHzigFXmCxCw1e3JaGQQ9sGCpdFJwnue', 'Test', 'Test', 'test', 'Usuario', '2025-11-14 22:38:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asignacion_emp`
--
ALTER TABLE `asignacion_emp`
  ADD PRIMARY KEY (`USER_ID`),
  ADD KEY `empleado_id` (`empleado_id`),
  ADD KEY `proyecto_id` (`proyecto_id`);

--
-- Indexes for table `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`USER_ID`);

--
-- Indexes for table `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`USER_ID`);

--
-- Indexes for table `indicador`
--
ALTER TABLE `indicador`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`USER_ID`);

--
-- Indexes for table `tiempo`
--
ALTER TABLE `tiempo`
  ADD PRIMARY KEY (`USER_ID`),
  ADD KEY `empleado_id` (`empleado_id`),
  ADD KEY `proyecto_id` (`proyecto_id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asignacion_emp`
--
ALTER TABLE `asignacion_emp`
  MODIFY `USER_ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `departamento`
--
ALTER TABLE `departamento`
  MODIFY `USER_ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `empleado`
--
ALTER TABLE `empleado`
  MODIFY `USER_ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `indicador`
--
ALTER TABLE `indicador`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `USER_ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tiempo`
--
ALTER TABLE `tiempo`
  MODIFY `USER_ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `asignacion_emp`
--
ALTER TABLE `asignacion_emp`
  ADD CONSTRAINT `asignacion_emp_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`USER_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `asignacion_emp_ibfk_2` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`USER_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tiempo`
--
ALTER TABLE `tiempo`
  ADD CONSTRAINT `tiempo_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`USER_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tiempo_ibfk_2` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`USER_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
