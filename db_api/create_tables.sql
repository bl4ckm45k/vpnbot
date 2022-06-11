create table tg_users
(
    id      bigserial PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    active  boolean DEFAULT FALSE,
    server_id INTEGER NULL,
    key_id  INTEGER NULL DEFAULT NULL
);

alter table tg_users
    owner to postgres;

create table vpn_servers
(
    id      bigserial PRIMARY KEY,
    country VARCHAR(20) NOT NULL,
    api_link VARCHAR(255) NOT NULL UNIQUE,
    UNIQUE (api_link, country)

)
alter table vpn_servers
    owner to postgres;
