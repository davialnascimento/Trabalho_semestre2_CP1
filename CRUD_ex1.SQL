INSERT INTO ativos (nome, ip, tipo, criticidade, status)
VALUES ('Servidor DNS', '192.168.1.30', 'servidor', 'alta', 'ativo');

-- Listar
SELECT * FROM ativos;

-- Filtrar por tipo
SELECT * FROM ativos
WHERE tipo = 'servidor';

-- Atualizar
UPDATE ativos
SET status = 'inativo'
WHERE ip = '192.168.1.30';

-- Remover
DELETE FROM ativos
WHERE ip = '192.168.1.30';
