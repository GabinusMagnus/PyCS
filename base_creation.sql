DROP TABLE IF EXISTS test;

CREATE TABLE test
(
    login VARCHAR(50),
    mdp VARCHAR(50),
    accessoire VARCHAR(50)
);

INSERT INTO test (login, mdp, accessoire) VALUES ('Lui', 'mdp_test', 'Il aime les choux.');
INSERT INTO test (login, mdp, accessoire) VALUES ('Elle', 'test_mdp', "Elle n'aime pas les choux.");